from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from .models import Crawling  # myapp를 실제 앱 이름으로 바꿔주세요

def start_mk():
    companies = ["넷플릭스", "삼성전자", "LG전자"]
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    base_url = "https://www.mk.co.kr/search?word={company}&dateType=1day&startDate={startDate}&endDate={endDate}"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')  # 인증서 오류 무시 옵션 추가

    driver = webdriver.Chrome(executable_path="path/to/chromedriver", options=chrome_options)  # 옵션 적용

    for company in companies:
        print(f"Crawling news articles for {company}...")

        url = base_url.format(company=company, startDate=yesterday_str, endDate=today.strftime("%Y-%m-%d"))
        driver.get(url)

        # 더보기 버튼 클릭
        try:
            more_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".btn_area > button"))
            )
            more_button.click()
        except:
            print(f"No '더보기' button found for {company}.")
            continue

        # 크롤링
        soup = BeautifulSoup(driver.page_source, "html.parser")
        news_items = soup.select("div.result_news_wrap ul.news_list li")

        if not news_items:
            print(f"No news items found for {company}.")
            continue

        for news_item in news_items:
            title_tag = news_item.select_one(".news_ttl a")
            if title_tag is None:
                print("제목이 포함된 뉴스가 없습니다.")
                continue

            title = title_tag.text.strip()
            link = title_tag["href"]

            news_agency_tag = news_item.select_one(".result_news_info .result_news_date")
            print(news_agency_tag)
            if news_agency_tag is None:
                print("뉴스가 없습니다.")
                continue

            news_agency = news_agency_tag.text.strip().split(" ")[-1]
            date_str = news_agency_tag.text.strip().split(" ")[0]

            # 날짜 형식 변환
            news_date = datetime.strptime(date_str, "%Y.%m.%d")
            formatted_date = news_date.strftime("%Y-%m-%d")

            # 데이터 저장
            Crawling.objects.create(title=title, news_date=formatted_date, link=link, news_agency="매일경제")

        print(f"이 기업의 크롤링이 완료 되었습니다. {company}")

    print("크롤링 완료.")



class Command(BaseCommand):
    help = '매일경제 뉴스 크롤링'

    def handle(self, *args, **options):
        start_mk()