# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
client_id = "QLA1DnSIvTqdzWipjyfa"
client_secret = "C78oNcaMvb"
encText = urllib.parse.quote("삼성전자경찰조사수사")
keywords = [["경찰조사수사","검찰조사수사","횡령배임","증여","사기","자금세탁"], 
                ["법원소송","법원판결","공정거래위원회처분시정제재","금융감독원처분행정지도"], 
                ["친환경에너지기술","탄소배출권","윤리경영","사회공헌","기업지배구조"]]
for keyword in keywords:
    url = "https://openapi.naver.com/v1/search/news?query=" + keywords # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)