import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .models import Mkcrawling
import time
from googletrans import Translator

def start_mk2():
    base_url = "https://www.mk.co.kr/news/stock/"
    translator = Translator()

    article_id = 10726685

    while True:
        article_url = f"{base_url}{str(article_id)}"

        article_response = requests.get(article_url)

        if article_response.status_code == 200:
            article_soup = BeautifulSoup(article_response.text, 'html.parser')

            title_tag = article_soup.find('h2', {'class': 'news_ttl'})
            if not title_tag:
                print(f"{article_url}에서 제목을 찾을 수 없습니다.")
                article_id += 1
                continue

            title = title_tag.text.strip()
            translated_title = translator.translate(title, dest='en').text

            content_tag = article_soup.find('div', {'class': 'news_cnt_detail_wrap'})
            if not content_tag:
                print(f"{article_url}에서 내용을 찾을 수 없습니다.")
                article_id += 1
                continue

            content = content_tag.text.strip()
            translated_content = translator.translate(content, dest='en').text

            # time_tag = article_soup.find('li', {'class': 'lasttime'})
            # if not time_tag:
            #     print(f"{article_url}에서 시간을 찾을 수 없습니다.")
            #     article_id += 1
            #     continue

            img_tag = content_tag.find('img')
            img_url = img_tag['src'] if img_tag else None

            time_tag = article_soup.find('div', class_='news_write_info_group').find('div', class_='info_area').find('dl', class_='registration').find('dd')
            print(time_tag)
            if not time_tag:
                print(f"{article_url}에서 시간을 찾을 수 없습니다.")
                article_id += 1
                continue

            news_time_str = time_tag.text.strip()
            news_time = datetime.strptime(news_time_str, "%Y-%m-%d %H:%M:%S")


            # 데이터베이스에 저장
            mkDB = Mkcrawling(title=translated_title,news_date=news_time, link=article_url, news_agency="매일경제", content=translated_content, collect_date=datetime.now(), img=img_url)
            mkDB.save()

            print(f"기사 {article_id} 저장 완료")

            article_id += 1
            time.sleep(2)  # 2초 간격으로 요청을 보내기 위해 추가
        else:
            print("마지막 기사입니다.")
            break
