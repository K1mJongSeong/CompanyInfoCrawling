#import instaloader
import re
import time
from instaloader import Instaloader, Profile
from django.utils import timezone
from googletrans import Translator
from .models import Instagram

def clean_string(s):
    # 이모지 및 특수 문자를 제거하고 반환합니다.
    return re.sub(r'[^\x00-\x7F]+', '', s)

def get_instagram_posts(username, insta_username, insta_password):
    custom_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    L = Instaloader(user_agent=custom_user_agent)
    translator = Translator()
    base_url = "https://www.instagram.com/p/"
    #L = instaloader.Instaloader()


    # 로그인
    try:
        L.load_session_from_file(insta_username)
    except FileNotFoundError:
        L.context.log("Session file not found, logging in...")
        L.login(insta_username, insta_password)
        L.save_session_to_file()

    for post in Profile.from_username(L.context, username).get_posts():
        img_url = post.url
        post_url = post.shortcode
        content = post.caption
        #content = clean_string(post.caption) if post.caption else ''
        post_date = post.date
        try:
            translated_summary = translator.translate(content, dest='en').text
        except TypeError:
            print("이 요약을 번역하지 못했습니다. 다음 뉴스로 이동합니다.")
            continue  
        title = post.title

        full_url = base_url + post_url

        print(f"내용: {content}")

        # DB저장
        ins_post = Instagram(
            title=title,
            news_date=post_date,
            link=full_url,
            en_content=translated_summary, #한글 -> 영어로 번역 시킨 후 DB 저장
            img=img_url,
            collect_date=timezone.now().date(),
            kr_content=content,
        )
        ins_post.save()


def scrape_instagram():
    username_list = ['kbsnews','jtbcnews','sbsnews','sbsnews']
    username = 'kbsnews' #크롤링할 태그네임 ,jtbcnews, kbsnews, sbsnews, sbsnews
    insta_username = 'thesoftlabs@daum.net' #인스타 로그인
    insta_password = 'thvmxmfoqtm'
    get_instagram_posts(username, insta_username, insta_password)
