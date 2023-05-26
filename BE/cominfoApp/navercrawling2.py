from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime,timedelta
from newspaper import Article
from newspaper.article import ArticleException
from googletrans import Translator
from django.core.exceptions import ObjectDoesNotExist
from .models import Crawling
import requests
import schedule
import time


def first_day_of_month():
    return datetime.now().day == 1

def start_navercrawling2():
    #if first_day_of_month():
    translator = Translator()
    companies = ["넷플릭스", "삼성전자", "LG전자"]
    keywords = [["경찰조사수사","검찰조사수사","횡령배임","증여","사기","자금세탁"], 
                ["법원소송","법원판결","공정거래위원회처분시정제재","금융감독원처분행정지도"], 
                ["친환경에너지기술","탄소배출권","윤리경영","사회공헌","기업지배구조"]]

    #base_url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query={company}{keyword}"#&dateType=1day&startDate={startDate}&endDate={endDate}
    base_url2 = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query={company}{keyword}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=457&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={page}"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
    chrome_options.add_argument('--ignore-certificate-errors')  # 인증서 오류 무시 옵션 추가

    driver = webdriver.Chrome("./chromedriver", options=chrome_options)  # 옵션 적용

    #headers = {"User-Agent":"Mozilla/5.0"}

    for company in companies:
        for keyword_list in keywords:
            for keyword in keyword_list:
                print(f"{company}{keyword} 크롤링 시작.")

                page = 1
                while True:
                    url = base_url2.format(company=company, keyword=keyword, page=page)
                    driver.get(url)
                    article_soup = BeautifulSoup(driver.page_source, "lxml")
                    news_items = article_soup.select("div.news_wrap.api_ani_send")

                    if len(news_items) == 0:
                        print(f"{company}{keyword}에 대한 뉴스 기사가 없습니다.")
                        break

                    print(url)

                    print(f"뉴스 개수: {len(news_items)}")

                    # 여기서부터 뉴스의 제목, 링크, 요약 내용 등을 원하는 방식으로 크롤링하면 됩니다.
                    # 아래 코드는 뉴스의 제목과 링크를 크롤링하는 예시입니다.
                    for news_item in news_items:
                        press_info = news_item.select_one("div.info_group > span.info.press")

                        if press_info is None:
                            press_info = news_item.select_one("div.info_group > span.info.press")
                        article = news_item.select_one("div.news_wrap api_ani_send")
                        title = news_item.select_one(".news_tit").text
                        link = news_item.select_one(".news_tit")['href']

                        try: #link가 이미 DB에 있는지 확인함.
                            existing_link = Crawling.objects.get(link=link)
                        except ObjectDoesNotExist:
                            existing_link = None


                        #content_tag = news_item.select_one("article.story-news article")

                        def parse_date(date_str):
                            try:
                                if '일 전' in date_str:
                                    days_ago = int(date_str.split('일 전')[0])
                                    news_date = datetime.now() - timedelta(days=days_ago)
                                else:
                                    news_date = datetime.strptime(date_str, "%Y.%m.%d.")
                                    news_date = news_date.strftime("%Y-%m-%d")
                                return news_date
                            except ValueError:
                                return None

                        date_tag = news_item.select_one("span.info")
                        while date_tag:
                            news_date = parse_date(date_tag.get_text().strip())
                            if news_date is not None:
                                break
                            date_tag = date_tag.find_next("span", class_="info")

                        # date_tag = news_item.select_one("span.info").get_text().strip()

                        # if '일 전' in date_tag:
                        #     days_ago = int(date_tag.split('일 전')[0])
                        #     news_date = datetime.now() - timedelta(days=days_ago)
                        # else:
                        #     # Convert the date string to a datetime object
                        #     news_date = datetime.strptime(date_tag, "%Y.%m.%d.")
                        #     # Convert the datetime object back to a string in the required format
                        #     news_date = news_date.strftime("%Y-%m-%d")

                        print(f"날짜:{news_date}")
                        print(f"Title: {title}")
                        print(f"Link: {link}")
                        print("------------")
                        # 언론사 이름 크롤링
                        news_agency_tag = news_item.select_one('div.news_info div.info_group a.info.press')
                        news_agency = news_agency_tag.get_text() if news_agency_tag else None
                        #print(news_agency)


                        img_tag = news_item.select_one('a.dsc_thumb img.thumb.api_get')
                        img = img_tag.get('data-lazysrc') if img_tag else None


                        if existing_link is None:
                            # 요약 생성
                            article = Article(link)
                            try:
                                article.download()
                                article.parse()
                                article.nlp()
                            except ArticleException:
                                print(f"요약에 실패했습니다. : {link}")
                                continue

                            summary = article.summary
                            #print(f"내용:{summary}")
                            if not summary:
                                print(f"{link}에서 내용을 찾을 수 없습니다.")
                                continue

                            try:
                                translated_summary = translator.translate(summary, dest='en').text
                            except TypeError:
                                print("이 요약을 번역하지 못했습니다. 다음 뉴스로 이동합니다.")
                                continue  

                            try:
                                translated_title = translator.translate(title,dest='en').text
                            except TypeError:
                                print("이 요약을 번역하지 못했습니다. 다음 뉴스로 이동합니다.")
                                continue 

                            naverDB = Crawling(title=translated_title, 
                                            news_date=news_date, 
                                            link=link, 
                                            en_content=translated_summary, 
                                            img=img, 
                                            collect_date=datetime.now(),
                                            news_agency=news_agency,
                                            kr_content=summary)
                            naverDB.save()
                    print(f"{company}{keyword} 크롤링 완료.")
                    page += 10
        print("마지막 기사입니다.")



#매월 1일에 크롤링 작업을 수행하는 스케줄링 설정
schedule.every().day.at("17:29").do(start_navercrawling2)
# while True:
#     schedule.run_pending() #대기 중인 스케줄링 작업이 있으면 수행함.

#     time.sleep(1)


class Command(BaseCommand):
    help = '네이버 뉴스 크롤링'

    def handle(self, *args, **options):
        start_navercrawling2()