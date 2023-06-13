import requests
import json

url = "https://gate.nicednb.com/nice/oauth/v1.0/accesstoken?appKey=l7xx0d82676128674c7bbb40f20373bb85e4&appSecret=21f355e652a4445495b2a0923c4dd967&grantType=client_credentials&scope=oob"
headers = {
    'Content-Type': 'application/json'
}
data = {
    "appKey": "l7xx0d82676128674c7bbb40f20373bb85e4",
    "appSecret": "21f355e652a4445495b2a0923c4dd967",
    "grantType": "client_credentials",
    "scope": "oob"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.text)