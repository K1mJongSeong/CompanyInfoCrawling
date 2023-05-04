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
from .models import Crawling, Khcrawling, Mkcrawling, Khfncrawling, Instagram, Facebook, User, Coruser
from .serializers import CrawlingSerializer, KhCrawlingSerializer, MkCrawlingSerializer, KhfncrawlingSerializer, UserSerializer, CorUserSerializer
from .facebook import fetch_facebook_data, save_facebook_data
from .insta import scrape_instagram
from .insta2 import scrape_instagram


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
    

def get_instagram_posts(request):
    scrape_instagram()

def get_instagram_posts2(request):
    scrape_instagram()


def fetch_and_save_fb_data(request):
    page_id = 'jtbcnews'  # JTBC 뉴스 채널 page_id
    access_token = '1325728901310569|c2kKh7Wi6SNfMr_b2MV2R8uXbPw'  # 소프트랩스 페이스북 개발자 기업정보 플랫폼 API토큰

    data = fetch_facebook_data(page_id, access_token)
    save_facebook_data(data)

    return JsonResponse({"status": "success"})


class UserLogin(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @swagger_auto_schema(
        operation_summary=' 일반 로그인 POST API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

class CorUserLogin(generics.ListCreateAPIView):
    serializer_class = CorUserSerializer
    queryset = Coruser.objects.all()

    @swagger_auto_schema(
        operation_summary=' 법인 로그인 POST API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)