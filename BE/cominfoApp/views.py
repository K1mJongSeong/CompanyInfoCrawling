#from django.shortcuts import render
from django.http import JsonResponse
from .crawling import schedule_crawling

def run_crawling(request):
    company_list = ["이아이디", "이브이첨단소재", "에코프로", "현대로템","에코프로비엠","피엔티","엘엔에프","이수화학","두산에너빌리티","이트론"]
    schedule_crawling(company_list)
    
    response_data = {
        'status': 'success',
        'message': 'Crawling completed'
    }
    
    return JsonResponse(response_data)

