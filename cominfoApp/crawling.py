from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from .models import Crawling
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import time
import urllib

def get_article_info(driver, keyword, crawl_date, press_list, title_list, link_list, date_list, more_news_base_url=None, more_news=False):
    chrome_options = Options()
    #headless 설정
    chrome_options.headless =True
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"
    #default는 caps["pageLoadStrategy"] = "normal"
    more_news_url_list = []
    while True:    
        page_html_source = driver.page_source
        url_soup = BeautifulSoup(page_html_source, 'lxml')
        
        more_news_infos = url_soup.select('a.news_more')
        
        if more_news:
            for more_news_info in more_news_infos:
                more_news_url = f"{more_news_base_url}{more_news_info.get('href')}"

                more_news_url_list.append(more_news_url)

        article_infos = url_soup.select("div.news_area")
        
        if not article_infos:
            break

        for article_info in article_infos:  
            press_info = article_info.select_one("div.info_group > a.info.press")
            
            if press_info is None:
                press_info = article_info.select_one("div.info_group > span.info.press")
            article = article_info.select_one("a.news_tit")
            
            press = press_info.text.replace("언론사 선정", "")
            title = article.get('title')
            link = article.get('href')

            if keyword in title:
                press_list.append(press)
                title_list.append(title)
                link_list.append(link)
                date_list.append(crawl_date)

        time.sleep(0.2)

        next_button_status = url_soup.select_one("a.btn_next").get("aria-disabled")
        
        if next_button_status == 'true':
            break
        
        time.sleep(0.2)
        next_page_btn = driver.find_element(By.CSS_SELECTOR, "a.btn_next").click() 
        
    return press_list, title_list, link_list, more_news_url_list


def get_naver_news_info_from_selenium(keyword, target_date, ds_de, sort=0, remove_duplicate=False):
    exclude_keywords = ['부고','부음']
    crawl_date = f"{target_date[:4]}.{target_date[4:6]}.{target_date[6:]}"
    driver = wd.Chrome("./chromedriver") # chromedriver 파일 경로

    encoded_keyword = urllib.parse.quote(keyword)
    url = f"https://search.naver.com/search.naver?where=news&query={encoded_keyword}&sm=tab_opt&sort={sort}&photo=0&field=0&pd=3&ds={ds_de}&de={ds_de}&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Afrom{target_date}to{target_date}&is_sug_officeid=0"
    
    more_news_base_url = "https://search.naver.com/search.naver"

    driver.get(url)
    
    press_list, title_list, link_list, date_list, more_news_url_list = [], [], [], [], []
    
    press_list, title_list, link_list, more_news_url_list = get_article_info(driver=driver, 
                                                                            keyword=keyword,
                                                                            crawl_date=crawl_date, 
                                                                            press_list=press_list, 
                                                                            title_list=title_list, 
                                                                            link_list=link_list,
                                                                            date_list=date_list,
                                                                            more_news_base_url=more_news_base_url,
                                                                            more_news=True)

    driver.close()
    
    if len(more_news_url_list) > 0:
        print(len(more_news_url_list))
        more_news_url_list = list(set(more_news_url_list))
        print(f"->{len(more_news_url_list)}")
        for more_news_url in more_news_url_list:
            driver = wd.Chrome("./chromedriver")
            driver.get(more_news_url)
            
            press_list, title_list, link_list, more_news_url_list = get_article_info(driver=driver, 
                                                                                    keyword=keyword,
                                                                                    crawl_date=crawl_date, 
                                                                                    press_list=press_list, 
                                                                                    title_list=title_list, 
                                                                                    link_list=link_list,
                                                                                    date_list=date_list)

            driver.close()
    article_df = pd.DataFrame({"날짜": date_list, "언론사": press_list, "제목": title_list, "링크": link_list})
    
    print(f"extract article num : {len(article_df)}")
    if remove_duplicate:
        article_df = article_df.drop_duplicates(['링크'], keep='first')
        print(f"after remove duplicate -> {len(article_df)}")
    
    
    # 데이터를 DB에 저장
    for idx in range(len(title_list)):
        title = title_list[idx]
        news_date = datetime.datetime.strptime(date_list[idx], "%Y.%m.%d")  # 날짜를 datetime 객체로 변환
        link = link_list[idx]
        news_agency = press_list[idx]

        if not any(keyword in title for keyword in exclude_keywords):
            # Crawling 모델 인스턴스 생성
            article = Crawling(title=title, news_date=news_date, link=link, news_agency=news_agency)

            # DB에 저장
            article.save()


def crawl_articles(company_name, start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, "%Y%m%d")
    end_date = datetime.datetime.strptime(end_date, "%Y%m%d")
    delta = datetime.timedelta(days=1)

    while start_date <= end_date:
        formatted_date = start_date.strftime("%Y%m%d")
        print(f"Crawling articles for {company_name} on {formatted_date}")
        #save_path = f"C:/Users/softlabs/Desktop/naver_news/{company_name}_{formatted_date}_articles_upScaling.xlsx"
        ds_de = start_date.strftime("%Y.%m.%d")
        get_naver_news_info_from_selenium(company_name, formatted_date, ds_de)
        start_date += delta

# 사용 예제
#company_name = "삼성전자"
company_name = input("기업 이름을 입력하세요: ")
start_date = input("시작 날짜를 입력하세요 (YYYYMMDD 형식): ")
end_date = input("종료 날짜를 입력하세요 (YYYYMMDD 형식): ")
# start_date = "20230401"
# end_date = "20230413"

crawl_articles(company_name, start_date, end_date)
