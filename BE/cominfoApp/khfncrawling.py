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
from googletrans import Translator
from sumy.nlp.tokenizers import Tokenizer as SumyTokenizer
import requests
import time


def start_khfn():
    translator = Translator()
    companies = ["넷플릭스","삼성전자","현대차"] #companies 배열은 나중에 DB 연결 후 컬럼 데이터를 가져오는 방식으로 변경할 예정.
    keywords = [["경찰조사수사","검찰조사수사","횡령배임","증여","사기","자금세탁"], 
                ["법원소송","법원판결","공정거래위원회처분시정제재","금융감독원처분행정지도"], 
                ["친환경에너지기술","탄소배출권","윤리경영","사회공헌","기업지배구조"]]
    base_url = "https://www.koreaherald.com/"
    url = "https://www.koreaherald.com/search/index.php?kr=&q={companies}{keywords}" #헤럴드 파이넨스
    next_url = "https://www.koreaherald.com/search/index.php?kr=&q={companies}{keywords}&sort=1&mode=list&np={page}&mp=1"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
    chrome_options.add_argument('--ignore-certificate-errors')  # 인증서 오류 무시 옵션 추가
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=capa)
    #driver = webdriver.Chrome("./chromedriver", options=chrome_options)  # 옵션 적용

    #wait = WebDriverWait(driver,30)


    for company in companies:
        for keyword_list in keywords:
            for keyword in keyword_list:
                print(f"{company}{keyword}크롤링 시작.")
                page = 1
                

                while True:
                    url = next_url.format(companies=company, keywords=keyword, page=page)
                    driver.get(url)
                    #wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'main_sec')))


                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    news_items = soup.select("div.sch_result > ul > li")
                    #articles = soup.find('div', {'class': 'main_sec'}).find_all('li')#main_sec
                    print(news_items)
                    if len(news_items) == 0:
                        print(f"{company}{keyword}에 대한 뉴스 기사가 없습니다.")
                        break

                    
                    if not news_items:
                        print(f"{company}{keyword}에 대한 뉴스 기사가 없습니다.")
                        break

                    
                    print(f"뉴스 개수: {len(news_items)}")

                    for news_item in news_items:

                        # 기사 본문 및 이미지 가져오기
                        article_response = requests.get(url)
                        article_soup = BeautifulSoup(article_response.text, 'html.parser')
                        title_tag = news_item.find('h1', {'class': 'view_tit'}).text.strip()[:255]
                        print(title_tag)#제목
                        if not title_tag:
                            print(f"{url}에서 제목을 찾을 수 없습니다.")

                        title = title_tag.text.strip()
                        #content = article_soup.find('div', {'class': 'view_con_t'}).text.strip()

                        img_table = article_soup.find('table', {'style': 'margin:auto;margin-bottom: 10px;  width: 640px; margin-top: 10px; '})
                        img_tag = img_table.find('img') if img_table else None
                        img = img_tag['src'] if img_tag else None #이미지
                        
                        link_tag = news_item.select("div.sch_result > ul > li > a")
                        for link in link_tag:
                            relative_url = link.get('href')
                            if relative_url:
                                full_url = base_url + relative_url
                                driver.get(full_url)
                            else:
                                print("링크가 포함된 뉴스가 없습니다.")

                        #제목,내용,이미지,링크,기사시간
                        # 요약 생성
                        article = Article(url)
                        article.download()
                        article.parse()
                        article.nlp()
                        summary = article.summary

                        translated_title = translator.translate(title, dest='en')
                        translated_content = translator.translate(summary, dest='en')

                        # 데이터베이스에 저장
                        khfnDB = Khfncrawling(title=translated_title, link=full_url, content=translated_content, img=img, collect_date=datetime.now(),news_agency="헤럴드 Finance")
                        khfnDB.save()

                    page += 1

                    print(f"{company}{keyword} 크롤링이 완료 되었습니다.")

            print("크롤링 완료.")

class Command(BaseCommand):
    help = '헤럴드 파이넨스 뉴스 크롤링'

    def handle(self, *args, **options):
        start_khfn()