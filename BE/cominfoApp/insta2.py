#import instaloader
import re
import time
from instaloader import Instaloader, Profile
from django.utils import timezone
from .models import Instagram

def clean_string(s):
    # 이모지 및 특수 문자를 제거하고 반환합니다.
    return re.sub(r'[^\x00-\x7F]+', '', s)

def get_instagram_posts(username, insta_username, insta_password):
    custom_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    L = Instaloader(user_agent=custom_user_agent)
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
        content = clean_string(post.caption) if post.caption else ''
        post_date = post.date

        time.sleep(2)

        # DB저장
        ins_post = Instagram(
            title="",
            news_date=post_date,
            link=post_url,
            content=content,
            img=img_url,
            collect_date=timezone.now().date()
        )
        ins_post.save()


def scrape_instagram():
    username = 'kbsnews' #크롤링할 태그네임
    insta_username = 'thesoftlabs@daum.net' #인스타 로그인
    insta_password = 'thvmxmfoqtm'
    get_instagram_posts(username, insta_username, insta_password)
