from django.shortcuts import render
from django.http import HttpResponse
from .crawling import crawl_articles

def run_crawling(request):
    # 크롤링 실행에 필요한 인자들
    company_name = "삼성전자"
    start_date = "20230401"
    end_date = "20230413"

    # 크롤링 실행
    crawl_articles(company_name, start_date, end_date)

    # HTTP 응답
    return HttpResponse("Crawling completed.")

