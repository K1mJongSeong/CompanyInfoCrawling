from bs4 import BeautifulSoup
from django.utils import timezone
from .models import Instagram
import json
import requests

def get_instagram_posts(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    script_tag = soup.find('script', text=lambda t: t.startswith('window._sharedData'))
    shared_data = script_tag.string.partition('=')[-1].strip(' ;')
    json_data = json.loads(shared_data)
    
    posts = json_data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
    
    for post in posts:
        node = post['node']
        img_url = node['thumbnail_src']
        post_url = f"https://www.instagram.com/p/{node['shortcode']}/"
        content = node['edge_media_to_caption']['edges'][0]['node']['text'] if node['edge_media_to_caption']['edges'] else ''
        timestamp = node['taken_at_timestamp']
        post_date = timezone.datetime.fromtimestamp(timestamp)

        # DB 저장
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
    url = 'https://www.instagram.com/kbsnews/'
    get_instagram_posts(url)

