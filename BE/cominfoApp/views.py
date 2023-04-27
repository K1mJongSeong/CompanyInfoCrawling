from django.http import JsonResponse
from .crawling import schedule_crawling, company_list
from . import mkcrawling

def start_crawling(request):
    schedule_crawling(company_list)  # 크롤링 코드를 실행합니다.
    return JsonResponse({"status": "정상", "message": "네이버 뉴스 크롤링 시작."})

def start_mkcrawling(requset):
    mkcrawling.start_mk()
    return JsonResponse({"message":"매일경제 크롤링 시작."})