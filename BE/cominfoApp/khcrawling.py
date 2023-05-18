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
from sumy.nlp.tokenizers import Tokenizer as SumyTokenizer
import requests
import time

def start_kh():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y%m%d")
    companies = ["넷플릭스","삼성전자","현대차"]
    keywords = [["경찰조사수사","검찰조사수사","횡령배임","증여","사기","자금세탁"], 
                ["법원소송","법원판결","공정거래위원회처분시정제재","금융감독원처분행정지도"], 
                ["친환경에너지기술","탄소배출권","윤리경영","사회공헌","기업지배구조"]]

    base_url = "http://biz.heraldcorp.com/search/index.php?q={company}{keyword}"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
    chrome_options.add_argument('--ignore-certificate-errors')  # 인증서 오류 무시 옵션 추가

    driver = webdriver.Chrome("./chromedriver", options=chrome_options)  # 옵션 적용


    translator = Translator() #googletrans 번역 라이브러리 사용.

    for company in companies:
        for keyword_list in keywords:
            for keyword in keyword_list:
                
                print(f"{company} {keyword} 크롤링 시작.")
                article_url = base_url.format(company=company, keyword=keyword) # URL에 회사명과 키워드 포함
                driver.get(article_url)

                time.sleep(1)

                article_soup = BeautifulSoup(driver.page_source, 'html.parser')
                
                title_tag = article_soup.find('li', {'class': 'article_title ellipsis2'})
                #title_tag = article_soup.select_one('div.list_title.ellipsis')
                if not title_tag:
                    print(f"{article_url}에서 제목을 찾을 수 없습니다.")
                    continue

                title = title_tag.text.strip()

                content_tag = article_soup.find('div', {'class': 'article_view'})
                #content_tag = article_soup.select_one('div.list_txt.ellipsis2')
                if not content_tag:
                    print(f"{article_url}에서 내용을 찾을 수 없습니다.")
                    continue

                content = content_tag.text.strip()

                # 요약 생성
                article = Article(article_url)
                article.download()
                article.parse()
                article.nlp()
                summary = article.summary

                translated_summary = translator.translate(summary, dest='en').text
                translated_title = translator.translate(title,dest='en').text

                img_tag = article_soup.select_one('div.article_view img')
                img = img_tag['src'] if img_tag else None

                # 데이터베이스에 저장
                khDB = Khcrawling(title=translated_title, news_date=datetime.strptime(yesterday_str, "%Y%m%d"), link=article_url, news_agency="헤럴드경제", content=translated_summary, img=img, collect_date=datetime.now())
                khDB.save()

                print(f"{company} {keyword} 크롤링 완료.")

            print("마지막 기사입니다.")


class Command(BaseCommand):
    help = '헤럴드경제 뉴스 크롤링'

    def handle(self, *args, **options):
        start_kh()