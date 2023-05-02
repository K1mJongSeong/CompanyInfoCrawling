from django.http import JsonResponse
from rest_framework_swagger.renderers import SwaggerUIRenderer
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view, renderer_classes, parser_classes #api
from rest_framework import status, generics, viewsets, serializers
from rest_framework.parsers import FileUploadParser,MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema, force_serializer_instance
from drf_yasg import openapi
from . import mkcrawling, khcrawling, crawling, khfncrawling, mkcrawling2
from .models import Crawling, Khcrawling, Mkcrawling, Khfncrawling
from .serializers import CrawlingSerializer, KhCrawlingSerializer, MkCrawlingSerializer, KhfncrawlingSerializer

def start_crawling(request):
    crawling.schedule_crawling()  # 크롤링 코드를 실행합니다. company_list
    return JsonResponse({"status": "정상", "message": "네이버 뉴스 크롤링 시작."})

def start_mkcrawling(requset):
    mkcrawling.start_mk()
    return JsonResponse({"message":"매일경제 크롤링 시작."})

def start_khcrawling(requset):
    khcrawling.start_kh()
    return JsonResponse({"message":"헤럴드경제 크롤링 시작."})

def start_khfncrawling(requset):
    khfncrawling.start_khfn()
    return JsonResponse({"message":"헤럴드 파이넨스 크롤링 시작."})

def start_mkcrawling2(requset):
    mkcrawling2.start_mk2()
    return JsonResponse({"message":"매일경제 모든 뉴스 크롤링 시작."})

#매일경제 크롤링 GET API
class MkCrwawlingGet(APIView):
    @swagger_auto_schema(
        operation_summary='매일경제 크롤링 데이터 GET API',
    )
    def get(self, request):
        mkData = Mkcrawling.objects.all()
        serializers = MkCrawlingSerializer(mkData, many=True)
        return Response(serializers.data)
    
#헤럴드경제 크롤링 GET API
class KhCrwawlingGet(APIView):
    @swagger_auto_schema(
        operation_summary='헤럴드경제 크롤링 데이터 GET API',
    )
    def get(self, request):
        khData = Khcrawling.objects.all()
        serializers = KhCrawlingSerializer(khData, many=True)
        return Response(serializers.data)