from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from .models import Crawling
from bs4 import BeautifulSoup
import schedule
import datetime
import pandas as pd
import time
import urllib
import threading
import concurrent.futures


#네이버

companies = ["넷플릭스", "삼성전자", "LG전자"]
keywords = [["경찰조사수사","검찰조사수사","횡령배임","증여","사기","자금세탁"], 
            ["법원소송","법원판결","공정거래위원회처분시정제재","금융감독원처분행정지도"], 
            ["친환경에너지기술","탄소배출권","윤리경영","사회공헌","기업지배구조"]]

def get_article_info(driver, keyword, crawl_date, press_list, title_list, link_list, date_list, more_news_base_url=None, more_news=False, max_page=20):

    
# 기업 리스트
    chrome_options = Options()
    #headless 설정
    chrome_options.headless =True
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"
    #default는 caps["pageLoadStrategy"] = "normal"
    more_news_url_list = []
    current_page = 1



    for company in companies:
        for keyword_group in keywords:
            for keyword in keyword_group:
                search_keyword = company + keyword

                print(f"{search_keyword} 크롤링 시작.")

                current_page = 1
                more_news_url_list = []

                while True:
                    if current_page > max_page: #20페이지까지만 While문이 돌 수 있음.
                        break

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

                        if search_keyword in title:
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

                    current_page += 1

    return press_list, title_list, link_list, more_news_url_list



def get_naver_news_info_from_selenium(keyword, target_date, ds_de, sort=0, remove_duplicate=False):
    exclude_keywords = ['부고','부음', '세일', '지구의 날']
    crawl_date = f"{target_date[:4]}.{target_date[4:6]}.{target_date[6:]}"
    driver = wd.Chrome("./chromedriver") # chromedriver 파일 경로
    
    encoded_keyword = urllib.parse.quote(keyword.encode('utf-8'))
    #encoded_keyword = urllib.parse.quote(keyword)
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

# def crawl_articles(company_name, start_date, end_date):
#     start_date = datetime.datetime.strptime(start_date, "%Y%m%d")
#     end_date = datetime.datetime.strptime(end_date, "%Y%m%d")
#     delta = datetime.timedelta(days=1)

#     while start_date <= end_date:
#         formatted_date = start_date.strftime("%Y%m%d")
#         print(f"Crawling articles for {company_name} on {formatted_date}")
#         print(datetime.datetime.now())
#         #save_path = f"C:/Users/softlabs/Desktop/naver_news/{company_name}_{formatted_date}_articles_upScaling.xlsx"
#         ds_de = start_date.strftime("%Y.%m.%d")
#         get_naver_news_info_from_selenium(company_name, formatted_date, ds_de)
#         start_date += delta


# def crawl_yesterdays_articles(company_name): #오늘 날짜를 기준으로 어제 날짜를 크롤링함.
#     today=datetime.datetime.now()
#     yesterday = today - datetime.timedelta(days=1)

#     start_date = yesterday.strftime("%Y%m%d")
#     end_date = start_date

#     crawl_articles(company_name,start_date,end_date)


def schedule_crawling(company_name, keyword_list):

    # with concurrent.futures.ProcessPoolExecutor() as executor: #멀티프로세싱 concurrent.futures 라이브러리 적용.
    #     results = list(executor.map(crawl_yesterdays_articles, company_list))

    for company in company_name:
        for keyword in keyword_list:
            print(f"Crawling {company} with keyword {keyword}")
            #get_article_info(keyword, company)
            time.sleep(3)  # 기다릴 시간 설정

        
    # next_company=next(company_name)
    # schedule.every().day.at("12:31").do(crawl_yesterdays_articles, next_company) #로직 다 완성하면 이 부분 매일 자정으로 00:00 실행될 수 있게 변경필요.

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    print("끝")
    print(datetime.datetime.now())
    return



#schedule_crawling(companies,keywords)











# def crawl_articles(company_name, start_date, end_date):
#     start_date = datetime.datetime.strptime(start_date, "%Y%m%d")
#     end_date = datetime.datetime.strptime(end_date, "%Y%m%d")
#     delta = datetime.timedelta(days=1)

#     while start_date <= end_date:
#         formatted_date = start_date.strftime("%Y%m%d")
#         print(f"Crawling articles for {company_name} on {formatted_date}")
#         #save_path = f"C:/Users/softlabs/Desktop/naver_news/{company_name}_{formatted_date}_articles_upScaling.xlsx"
#         ds_de = start_date.strftime("%Y.%m.%d")
#         get_naver_news_info_from_selenium(company_name, formatted_date, ds_de)
#         start_date += delta

# # 사용 예제
# #company_name = "삼성전자"
# company_name = input("기업 이름을 입력하세요: ")
# start_date = input("시작 날짜를 입력하세요 (YYYYMMDD 형식): ")
# end_date = input("종료 날짜를 입력하세요 (YYYYMMDD 형식): ")
# # start_date = "20230401"
# # end_date = "20230413"

# crawl_articles(company_name, start_date, end_date)
