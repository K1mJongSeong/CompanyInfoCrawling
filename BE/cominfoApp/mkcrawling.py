import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import time

from .models import Crawling

#매일경제 뉴스 크롤링
def get_mk_article_links(date):
    base_url = "https://www.mk.co.kr/news/"
    formatted_date = date.strftime("%Y%m%d")
    url = f"{base_url}economy/?date={formatted_date}"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    article_links = []
    for link in soup.select("div.list_area > dl > dt > a"):
        article_links.append(link['href'])

    return article_links


def get_mk_article_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.select_one("div.top_title > h1").text.strip()
    date = soup.select_one("li.date").text.strip()
    content = soup.select_one("div.art_txt").text.strip()

    return title, date, content


def crawl_mk_articles(start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, "%Y%m%d")
    end_date = datetime.datetime.strptime(end_date, "%Y%m%d")
    delta = datetime.timedelta(days=1)

    while start_date <= end_date:
        print(f"Crawling articles on {start_date.strftime('%Y-%m-%d')}")
        article_links = get_mk_article_links(start_date)

        for link in article_links:
            time.sleep(1)  # 기다릴 시간 설정
            title, date, content = get_mk_article_info(link)

            # DB에 저장
            article = Crawling(title=title, news_date=date, link=link, news_agency="매일경제", content=content)
            article.save()

        start_date += delta

# 사용 예제
start_date = input("시작 날짜를 입력하세요 (YYYYMMDD 형식): ")
end_date = input("종료 날짜를 입력하세요 (YYYYMMDD 형식): ")

crawl_mk_articles(start_date, end_date)
