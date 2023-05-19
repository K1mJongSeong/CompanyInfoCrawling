from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from googletrans import Translator
from .models import Khcrawling
from newspaper import Article
from newspaper.article import ArticleException
from sumy.nlp.tokenizers import Tokenizer as SumyTokenizer
import requests
import time

def start_kh():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y%m%d")
    companies = ["넷플릭스","삼성전자","현대차"] #companies 배열은 나중에 DB 연결 후 컬럼 데이터를 가져오는 방식으로 변경할 예정.
    keywords = [["경찰조사수사","검찰조사수사","횡령배임","증여","사기","자금세탁"], 
                ["법원소송","법원판결","공정거래위원회처분시정제재","금융감독원처분행정지도"], 
                ["친환경에너지기술","탄소배출권","윤리경영","사회공헌","기업지배구조"]]

    base_url = "http://biz.heraldcorp.com/search/index.php?q={company}{keyword}"
    base_url2 = "http://biz.heraldcorp.com/"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
    chrome_options.add_argument('--ignore-certificate-errors')  # 인증서 오류 무시 옵션 추가

    driver = webdriver.Chrome("./chromedriver", options=chrome_options)  # 옵션 적용


    translator = Translator() #googletrans 번역 라이브러리 사용.

    for company in companies: #회사
        for keyword_list in keywords: #키워드
            for keyword in keyword_list: #회사+키워드
                
                print(f"{company} {keyword} 크롤링 시작.")
                article_url = base_url.format(company=company, keyword=keyword) # URL에 회사명과 키워드 포함
                driver.get(article_url)



                article_soup = BeautifulSoup(driver.page_source, 'html.parser')
                news_items = article_soup.select("div.list > ul > li")
                

                print(f"news_items length: {len(news_items)}")

                for news_item in news_items:
                    #title_tag = article_soup.find('li', {'class': 'article_title ellipsis2'})
                    title_tag = news_item.select_one("div.list_title.ellipsis")
                    if not title_tag:
                        print(f"{article_url}에서 제목을 찾을 수 없습니다.")
                        continue
                    
                    title = title_tag.text.strip()
                    print(title)

                    date_tags = news_item.select_one("div.l_date")
                    date = datetime.strptime(date_tags.text.strip(), "%Y.%m.%d %H:%M")

                    #content_tag = article_soup.find('div', {'class': 'article_view'})
                    content_tag = article_soup.select_one('div.list_txt.ellipsis2')

                    if not content_tag:
                        print(f"{article_url}에서 내용을 찾을 수 없습니다.")
                        continue
                    

                    link_tags = news_item.select("div.list > ul > li > a")
                    for link in link_tags:
                        relative_url = link.get('href')
                        if relative_url: 
                            full_url = base_url2 + relative_url
                            driver.get(full_url)  # 링크 방문
                        else:
                            print("링크가 포함된 뉴스가 없습니다.")

                    content_soup = BeautifulSoup(driver.page_source, "html.parser")
                    
                    content_tag = content_soup.select(".article_view")# 뉴스 내용 찾기
                    if content_tag is None:
                        print("뉴스 내용이 없습니다.")
                        continue
                    #content = content_tag.text.strip()

                    # 요약 생성
                    article = Article(full_url)
                    try:
                        article.download()
                        article.parse()
                        article.nlp()
                    except ArticleException:
                        print(f"Article download failed for URL: {full_url}, moving to next article.")
                        continue  # Skip the rest of this loop iteration and move to next news item

                    summary = article.summary
                    try:
                        translated_summary = translator.translate(summary, dest='en').text
                    except TypeError:
                        print("Translation failed for this summary, moving to next article.")
                        continue  # Skip the rest of this loop iteration and move to next news item

                    try:
                        translated_title = translator.translate(title,dest='en').text
                    except TypeError:
                        print("Translation failed for this title, moving to next article.")
                        continue  # Skip the rest of this loop iteration and move to next news item

                    # translated_summary = translator.translate(summary, dest='en').text
                    # translated_title = translator.translate(title,dest='en').text


                    img_tag = content_soup.select_one('#heraldbizimg01')
                    img = img_tag['src'] if img_tag else None
                    print('aaa')
                    print(img)

                    # 데이터베이스에 저장
                    khDB = Khcrawling(title=translated_title, news_date=date, link=full_url, news_agency="헤럴드경제", content=translated_summary, img=img, collect_date=datetime.now())
                    khDB.save()

                    #driver.back()
                                    # 다음페이지 클릭
                try:
                    more_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "a.arrow.next"))
                    )
                    link_button = more_button.get_attribute('href')
                    
                    more_button.click()
                    print('bbbbbbb')
                except:
                    print(f"{company}{keyword} 페이지가 더 이상 없습니다.")
                
                print(link_button)
                print(f"{company} {keyword} 크롤링 완료.")

            print("마지막 기사입니다.")


class Command(BaseCommand):
    help = '헤럴드경제 뉴스 크롤링'

    def handle(self, *args, **options):
        start_kh()