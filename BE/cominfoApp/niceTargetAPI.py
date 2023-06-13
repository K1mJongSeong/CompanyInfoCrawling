import requests
import json

url = "https://gate.nicednb.com/nice/bizinfo/v1.0/sentinel/target?pageNum=1"
headers = {
    'Content-Type': 'application/json',
    'Authorization':'Bearer c404b1da-b7bb-492b-a5a9-c654194ec5a9',
}

data = {
    "pageNum": "64",
}

response = requests.post(url, headers=headers, data=json.dumps(data))

response_json = response.json()

# 'cmpCd'의 값을 추출합니다
cmpCds = [item['cmpCd'] for item in response_json['dataBody']['cmpList']]

# 값들을 쌍따옴표로 감싸고 쉼표로 연결합니다
cmpCds_string = ', '.join(f'"{cd}"' for cd in cmpCds)

print(cmpCds_string)
print(data)

# print(response.status_code)
# print(response.text)