import requests
from .models import Facebook

def fetch_facebook_data(page_id, access_token):
    url = f'https://graph.facebook.com/{page_id}/posts?fields=id,message,created_time&access_token={access_token}'
    response = requests.get(url)
    data = response.json()
    print(data)
    return data


def save_facebook_data(data):
    for item in data['data']:
        meta_id = item['id']
        message = item.get('message', '')
        created_time = item['created_time']
        
        post, created = Facebook.objects.get_or_create(meta_id=meta_id)
        post.message = message
        post.created_time = created_time
        post.save()
