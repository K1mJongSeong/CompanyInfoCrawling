from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime,timedelta
from newspaper import Article
from googletrans import Translator
from .models import Mkcrawling
import time
import nltk


nltk.download('punkt')

def start_mk2():
    translator = Translator()
    companies = ["넷플릭스", "삼성전자", "LG전자"]
    keywords = [["경찰조사수사","검찰조사수사","횡령배임","증여","사기","자금세탁"], 
                ["법원소송","법원판결","공정거래위원회처분시정제재","금융감독원처분행정지도"], 
                ["친환경에너지기술","탄소배출권","윤리경영","사회공헌","기업지배구조"]]


    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    base_url = "https://www.mk.co.kr/search?word={company}{keyword}"#&dateType=1day&startDate={startDate}&endDate={endDate}


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
    chrome_options.add_argument('--ignore-certificate-errors')  # 인증서 오류 무시 옵션 추가

    driver = webdriver.Chrome("./chromedriver", options=chrome_options)  # 옵션 적용

    for company in companies:
        for keyword_list in keywords:
            for keyword in keyword_list:
                print(f"{company} 크롤링 시작.")

                url = base_url.format(company=company, keyword=keyword) #startDate=yesterday_str, endDate=today.strftime("%Y-%m-%d"))
                driver.get(url)

                # 더보기 버튼 클릭
                try:
                    more_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn_area > button"))
                    )
                    more_button.click()
                except:
                    print(f"{company} 페이지가 더 이상 없습니다.")

                # 크롤링
                soup = BeautifulSoup(driver.page_source, "html.parser")
                news_items = soup.select("div.result_news_wrap ul.news_list li")

                print(f"news_items length: {len(news_items)}")  # 추가

                if not news_items:
                    print(f"이 기업의 뉴스가 없습니다: {company}.")
                    #continue

                for news_item in news_items:
                    title_tag = news_item.select_one("h3.news_ttl")
                    if title_tag is None:
                        print("제목이 포함된 뉴스가 없습니다.")
                        continue

                    link_tag = news_item.select_one("a.news_item")
                    if link_tag is None:
                        print("링크가 포함된 뉴스가 없습니다.")
                        continue

                    
                    driver.get(link_tag['href'])# 링크 방문
                    content_soup = BeautifulSoup(driver.page_source, "html.parser")
                    
                    content_tag = content_soup.select_one(".news_cnt_detail_wrap")# 뉴스 내용 찾기
                    if content_tag is None:
                        print("뉴스 내용이 없습니다.")
                        continue

                    
                    
                    image_tags = content_soup.select(".news_cnt_detail_wrap img")

                    date_tags = content_soup.select_one("dl.registration dd")


                    image_urls = []# 이미지 URL을 저장할 리스트 생성

                    if date_tags is not None:
                        date_str = date_tags.text.strip()
                    else:
                        print("날짜 정보가 없습니다.")

                    date = datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")

                    for image_tag in image_tags: # 이미지 태그에서 src 속성을 가져와서 리스트에 추가
                        image_url = image_tag["src"]
                        image_urls.append(image_url)

                    
                    print("이미지 URL 리스트:", image_urls)# 이미지 URL 리스트 출력

                    img = image_urls
                    print(img)
                    #content = content_tag.get_text(strip=True)  # 내용 태그에서 내용 text만 가져옴.
                    title = title_tag.text.strip() #제목 태그 잘라서 제목 text만 가져옴.
                    link = link_tag["href"] #링크 태그 잘라서 링크만 가져옴.


                    translated_title = translator.translate(title,dest='en').text

                    # 뉴스 내용 요약
                    article = Article(link_tag["href"])
                    article.download()
                    article.parse()
                    article.nlp()
                    summary = article.summary

                    translated_content = translator.translate(summary, dest='en').text

                    mkDB=Mkcrawling(title=translated_title, news_date=date, link=link, news_agency="매일경제", content=translated_content, img=img, collect_date=datetime.now())
                    mkDB.save()

                    driver.back()

                    time.sleep(7)


        print(f"이 기업의 크롤링이 완료 되었습니다. {company}")

    print("크롤링 완료.")


class Command(BaseCommand):
    help = 'Crawl news articles from Maeil Business Newspaper'

    def handle(self, *args, **options):
        start_mk2()