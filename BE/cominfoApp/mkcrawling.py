import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import time
import schedule
from .models import Crawling

company_list = ["현대차"]

# 매일경제 뉴스 크롤링
def get_mk_article_links(date, company):
    base_url = "https://search.mk.co.kr/search.php?&page={page}&s_kwd={company}&s_page=news"
    formatted_date = date.strftime("%Y%m%d")
    url = f"{base_url}search/?date={formatted_date}&s_keyword={company}"

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
        for company in company_list:
            print(f"Crawling articles for {company}")
            article_links = get_mk_article_links(start_date, company)

            for link in article_links:
                time.sleep(1)  # 기다릴 시간 설정
                title, date, content = get_mk_article_info(link)

                # DB에 저장
                article = Crawling(title=title, news_date=date, link=link, news_agency="매일경제", content=content)
                article.save()

        start_date += delta

def run_mk_crawling():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    start_date = yesterday.strftime("%Y%m%d")
    end_date = start_date

    crawl_mk_articles(start_date, end_date)

# def job():
#     print("Starting the crawling job...")
#     run_mk_crawling()
#     print("Crawling job finished.")

# # 스케줄 설정: 매일 자정에 실행
# schedule.every().day.at("09:51").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(60)  # 대기 시간 60초

# run_mk_crawling()
