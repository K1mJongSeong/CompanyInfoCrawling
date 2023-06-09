from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
from .models import Khfncrawling
from newspaper import Article
from newspaper.article import ArticleException
from googletrans import Translator
from django.core.exceptions import ObjectDoesNotExist
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.html import HtmlParser
from sumy.summarizers.lsa import LsaSummarizer
import requests
import time
import schedule



def first_day_of_month():
    return datetime.now().day == 1

def start_khfn():
    #if first_day_of_month():
    translator = Translator()
    companies = ["넷플릭스","삼성전자","현대차"] #companies 배열은 나중에 DB 연결 후 컬럼 데이터를 가져오는 방식으로 변경할 예정.
    keywords = [["경찰조사수사","검찰조사수사","횡령배임","증여","사기","자금세탁"], 
                ["법원소송","법원판결","공정거래위원회처분시정제재","금융감독원처분행정지도"], 
                ["친환경에너지기술","탄소배출권","윤리경영","사회공헌","기업지배구조"]]
    base_url = "https://www.koreaherald.com/"
    url = "https://www.koreaherald.com/search/index.php?kr=&q={companies}{keywords}" #헤럴드 파이넨스
    next_url = "https://www.koreaherald.com/search/index.php?kr=&q={company}{keyword}&sort=1&mode=list&np={page}&mp=1"

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless") # 이 부분이 추가됩니다.
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.106 Safari/537.36")#114.0.5735.110
    #chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36")#114.0.5735.110
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36
    chrome_options.add_argument('--ignore-certificate-errors')  # 인증서 오류 무시 옵션 추가
    # capa = DesiredCapabilities.CHROME
    # capa["pageLoadStrategy"] = "none"

    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=capa)
    #driver = webdriver.Chrome("/usr/bin/chromedriver", options=chrome_options)  # 옵션 적용
    driver = webdriver.Chrome("./chromedriver", options=chrome_options)  # 옵션 적용

    #wait = WebDriverWait(driver,10)


    for company in companies:
        for keyword_list in keywords:
            for keyword in keyword_list:
                print(f"{company}{keyword}크롤링 시작.")
                page = 1
                time.sleep(1)
                

                while True:
                    url = next_url.format(company=company, keyword=keyword, page=page)
                    driver.get(url)
                    #wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'main_sec')))


                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    news_items = soup.select("ul.main_sec_li > li")
                    #articles = soup.find('div', {'class': 'main_sec'}).find_all('li')#main_sec
                    if len(news_items) == 0:
                        print(f"{company}{keyword}에 대한 뉴스 기사가 없습니다.")
                        break

                    print(f"뉴스 개수: {len(news_items)}")

                    for news_item in news_items:

                        # 기사 본문 및 이미지 가져오기
                        article_response = requests.get(url)
                        article_soup = BeautifulSoup(article_response.text, 'html.parser')
                        title_tag = news_item.select_one("div.main_l_t1")
                        #title_tag = news_item.find('h1', {'class': 'view_tit'}).text.strip()[:255]
                        # if not title_tag:
                        #     print(f"{url}에서 제목을 찾을 수 없습니다.")


                        title = title_tag.text.strip()
                        print(title)#제목
                        #content = article_soup.find('div', {'class': 'view_con_t'}).text.strip()

                        div_tag = article_soup.find('div', {'class': 'main_l_img'})
                        img_tag = div_tag.find('img') if div_tag else None
                        img_src = img_tag['src'] if img_tag else None


                        def fix_month_name(date_string):
                            return date_string.replace('Sept', 'Sep')

                        date_tag = news_item.select_one(".main_l_t2 span")
                        date_string = fix_month_name(date_tag.text.strip())
                        date = datetime.strptime(date_string, "%b %d, %Y")
                        
                        link_tag = news_item.select("div.sch_result > ul > li > a")
                        for link in link_tag:
                            relative_url = link.get('href')
                            if relative_url:
                                full_url = base_url + relative_url
                                driver.get(full_url)
                            else:
                                print("링크가 포함된 뉴스가 없습니다.")

                        try:
                            existing_link = Khfncrawling.objects.filter(link=full_url).first()
                        except ObjectDoesNotExist:
                            existing_link = None

                        content_soup = BeautifulSoup(driver.page_source, "html.parser")
                        #content_tag = content_soup.select("div.view_con.article")
                        content_tag = content_soup.select_one("div.view_con_t").text
                        if content_tag is None:
                            print("뉴스 내용이 없습니다.")
                            continue

                        if existing_link is None:
                            #제목,내용,이미지,링크,기사시간
                            # 요약 생성
                            # article = Article(full_url, language='en')
                            # try:
                            #     article.download()
                            #     article.parse()
                            # except ArticleException:
                            #     print(f"요약에 실패했습니다. URL: {full_url}, 다음 기사로 이동합니다.")
                            #     continue

                            # New summary generation with sumy
                            tokenizer = Tokenizer("english")
                            parser = PlaintextParser.from_string(content_tag, tokenizer=tokenizer)
                            summarizer = LsaSummarizer()
                            summary = summarizer(parser.document, 3)  # Summarize the document with 3 sentences

                            # Converting Summary from sentences to final string
                            summary = " ".join(str(sentence) for sentence in summary)

                            try:
                                translated_content = translator.translate(content_tag, dest='en').text
                            except TypeError:
                                print("이 요약을 번역하지 못했습니다. 다음 뉴스로 이동합니다.")
                                continue

                            try:
                                translated_title = translator.translate(title,dest='en').text
                            except TypeError:
                                print("이 요약을 번역하지 못했습니다. 다음 뉴스로 이동합니다.")
                                continue

                            # 데이터베이스에 저장
                            khfnDB = Khfncrawling(title=translated_title,
                                                news_date=date, 
                                                link=full_url, 
                                                en_content=translated_content, 
                                                img=img_src, 
                                                collect_date=datetime.now(),
                                                news_agency="헤럴드 Finance",
                                                kr_content=content_tag)
                            khfnDB.save()

                        page += 1

                    print(f"{company}{keyword} 크롤링이 완료 되었습니다.")

            print("크롤링 완료.")

schedule.every().day.at("00:00").do(start_khfn)

# while True:
#     schedule.run_pending()

#     time.sleep(1)

class Command(BaseCommand):
    help = '헤럴드 파이넨스 뉴스 크롤링'

    def handle(self, *args, **options):
        start_khfn()