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

    base_url = "http://biz.heraldcorp.com/view.php?ud="

    article_id = 1

    translator = Translator() #googletrans 번역 라이브러리 사용.


    while True:
        article_url = f"{base_url}{yesterday_str}000{str(article_id).zfill(3)}"

        article_response = requests.get(article_url)

        if article_response.status_code == 200:
            article_soup = BeautifulSoup(article_response.text, 'html.parser')

            title_tag = article_soup.find('li', {'class': 'article_title ellipsis2'})
            if not title_tag:
                print(f"{article_url}에서 제목을 찾을 수 없습니다.")
                article_id += 1
                continue

            title = title_tag.text.strip()

            content_tag = article_soup.find('div', {'class': 'article_view'})
            if not content_tag:
                print(f"{article_url}에서 내용을 찾을 수 없습니다.")
                article_id += 1
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

            img_tag = article_soup.find('div', {'class': 'article_view'}).find('img')
            img = img_tag['src'] if img_tag else None

            # 데이터베이스에 저장
            khDB = Khcrawling(title=translated_title, news_date=datetime.strptime(yesterday_str, "%Y%m%d"), link=article_url, news_agency="헤럴드경제", content=translated_summary, img=img, collect_date=datetime.now())
            khDB.save()

            print(f"기사 {article_id} 저장 완료")

            article_id += 1
        else:
            print("마지막 기사입니다.")
            break

class Command(BaseCommand):
    help = '헤럴드경제 뉴스 크롤링'

    def handle(self, *args, **options):
        start_kh()