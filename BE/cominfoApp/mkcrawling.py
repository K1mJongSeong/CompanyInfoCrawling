from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from .models import Crawling

def start_mk():
    companies = ["넷플릭스", "삼성전자", "LG전자"]
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    base_url = "https://www.mk.co.kr/search?word={company}&dateType=1day&startDate={startDate}&endDate={endDate}"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')  # 인증서 오류 무시 옵션 추가

    driver = webdriver.Chrome("./chromedriver", options=chrome_options)  # 옵션 적용

    for company in companies:
        print(f"{company}기업 크롤링 시작.")

        url = base_url.format(company=company, startDate=yesterday_str, endDate=today.strftime("%Y-%m-%d"))
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

            title = title_tag.text.strip() #제목 태그 잘라서 제목 text만 가져옴.
            print(title)
            link = link_tag["href"] #링크 태그 잘라서 링크만 가져옴.
            print(link)

            #news_agency_tag = news_item.select_one(".result_news_info .result_news_date")
            print("as23232323")
            # print(news_agency_tag)

            # if news_agency_tag is None:
            #     print("뉴스가 없습니다.")
            #     continue
            
            #news_agency = news_agency_tag.text.strip().split(" ")[-1]
            #date_str = news_agency_tag.text.strip().split(" ")[0]

            # 날짜 형식 변환
            # news_date = datetime.strptime(date_str, "%Y.%m.%d")
            # formatted_date = news_date.strftime("%Y-%m-%d")
            # 데이터 저장
            #Crawling.objects.create(title=title, news_date=formatted_date, link=link, news_agency="매일경제")
            mkDB=Crawling(title=title, news_date=yesterday_str, link=link, news_agency="매일경제")
            print(mkDB)
            mkDB.save()


        print(f"이 기업의 크롤링이 완료 되었습니다. {company}")

    print("크롤링 완료.")



class Command(BaseCommand):
    help = '매일경제 뉴스 크롤링'

    def handle(self, *args, **options):
        start_mk()