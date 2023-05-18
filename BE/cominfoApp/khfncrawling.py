from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from .models import Khfncrawling
from newspaper import Article
from sumy.nlp.tokenizers import Tokenizer as SumyTokenizer
import requests
import time

def start_khfn():
    keywords = [["경찰조사수사","검찰조사수사","횡령배임","증여","사기","자금세탁"], 
                ["법원소송","법원판결","공정거래위원회처분시정제재","금융감독원처분행정지도"], 
                ["친환경에너지기술","탄소배출권","윤리경영","사회공헌","기업지배구조"]]
    url = "https://www.koreaherald.com/list.php?ct=021900000000" #헤럴드 파이넨스
    next_button = "https://www.koreaherald.com//list.php?ct=021900000000&np=1&mp=1" #페이지네이션 다음 버튼

    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome("./chromedriver", options=chrome_options)  # 옵션 적용
    driver.get(url)

    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        articles = soup.find('div', {'class': 'main_sec'}).find_all('li')#main_sec
        print(articles)

        for article in articles:
            link = 'https://www.koreaherald.com' + article.find('a')['href']

            # 기사 본문 및 이미지 가져오기
            article_response = requests.get(link)
            article_soup = BeautifulSoup(article_response.text, 'html.parser')
            title = article_soup.find('h1', {'class': 'view_tit'}).text.strip()[:255]
            print(title)
            #content = article_soup.find('div', {'class': 'view_con_t'}).text.strip()

            img_table = article_soup.find('table', {'style': 'margin:auto;margin-bottom: 10px;  width: 640px; margin-top: 10px; '})
            img_tag = img_table.find('img') if img_table else None
            img = img_tag['src'] if img_tag else None

            # 요약 생성
            article = Article(link)
            article.download()
            article.parse()
            article.nlp()
            summary = article.summary

            # 데이터베이스에 저장
            khfnDB = Khfncrawling(title=title, link=link, content=summary, img=img, collect_date=datetime.now(),news_agency="헤럴드 Finance")
            khfnDB.save()

        np_val = int(next_button.split("np=")[1].split("&")[0])

        next_np_val = np_val + 1

        next_url = next_button.replace(f"np={np_val}", f"np={next_np_val}")

        driver.get(next_url)
        time.sleep(1)

        if driver.current_url == next_button:
            break

        next_button = driver.current_url
    driver.quit()

class Command(BaseCommand):
    help = '헤럴드 파이넨스 뉴스 크롤링'

    def handle(self, *args, **options):
        start_khfn()