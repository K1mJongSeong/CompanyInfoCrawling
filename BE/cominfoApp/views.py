from django.http import JsonResponse, HttpResponse
from rest_framework_swagger.renderers import SwaggerUIRenderer
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, renderer_classes, parser_classes #api
from rest_framework import status, generics, viewsets, serializers
from rest_framework.parsers import FileUploadParser,MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema, force_serializer_instance
from drf_yasg import openapi
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.core.mail import EmailMessage,send_mail
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from django.conf import settings
from django.views.generic import View
from . import mkcrawling, khcrawling, crawling, khfncrawling, mkcrawling2
from .models import Crawling, Khcrawling, Mkcrawling, Khfncrawling, Instagram, Facebook, User, Coruser, Login, Email, EmailVerfi
from .serializers import CrawlingSerializer, KhCrawlingSerializer, MkCrawlingSerializer, KhfncrawlingSerializer, UserSerializer, CorUserSerializer, InstagramSerializer, LoginSerializer, EmailSerializer, EmailVerfiSerailizer, UserPasswordChange
from .facebook import fetch_facebook_data, save_facebook_data
from .insta import scrape_instagram
import random
from datetime import datetime, timedelta


#-----------------------------------------------------크롤링 동작
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

def get_instagram_posts(request):
    scrape_instagram()
    return JsonResponse({"message":"인스타그램 크롤링 시작."})

def fetch_and_save_fb_data(request): #페이스북 크롤링
    page_id = 'jtbcnews'  # JTBC 뉴스 채널 page_id
    access_token = '1325728901310569|c2kKh7Wi6SNfMr_b2MV2R8uXbPw'  # 소프트랩스 페이스북 개발자 기업정보 플랫폼 API토큰

    data = fetch_facebook_data(page_id, access_token)
    save_facebook_data(data)

    return JsonResponse({"status": "success"})

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             return JsonResponse({"status": "success", "message": "로그인 성공"})
#         else:
#             return JsonResponse({"status": "error", "message": "이메일 또는 비밀번호가 일치하지 않습니다."})
#-----------------------------------------------------크롤링 동작

#-----------------------------------------------------API
class SendEmailVerificationView(GenericAPIView):
    serializer_class = EmailSerializer
    def post(self, request, *args, **kwargs):
        # POST 요청에서 이메일 주소 가져오기
        email = request.data.get('email')

        # 5자리 랜덤 인증번호 생성
        verification_code = get_random_string(length=5, allowed_chars='0123456789')

        # 이메일 전송
        success = send_mail(
            '회원가입 인증번호',  # 제목
            f'인증번호: {verification_code}',  # 내용
            settings.EMAIL_HOST_USER,  # 발신자 이메일
            [email],  # 수신자 이메일
            fail_silently=False,  # 실패 시 에러를 발생시키도록 설정
        )
        print(f"받는 사람 {email}. 성공여부: {success}")
        # 현재 시간 저장
        now = datetime.now()

        # Email 객체 생성 및 저장
        email_obj = Email.objects.create(
            email=email, 
            auth_num=verification_code, 
            create_at=now,
            expires_at=now + timedelta(minutes=5) # 현재 시간에서 5분 더한 시간을 만료 시간으로 설정
        )
        email_obj = Email.objects.get(email=email, auth_num=verification_code)

        if email_obj.expires_at < datetime.now():
            # 인증번호가 만료된 경우
            email_obj.auth_num = None # 인증번호를 초기화하거나, None 값으로 저장합니다.
            email_obj.save()
        #email_obj = Email.objects.create(email=email, auth_num=verification_code, create_at=datetime.now())

        # 인증번호와 메시지 반환
        return JsonResponse({'verification_code': verification_code, 'message': '인증번호가 이메일로 발송되었습니다.'})


class VerifyEmailView(GenericAPIView): #이메일 인증
    serializer_class = EmailVerfiSerailizer

    def post(self, request, *args, **kwargs):
        # POST 요청에서 이메일과 인증번호 가져오기
        email = request.data.get('email')
        auth_num = request.data.get('auth_num')

        # 이메일이 존재하지 않는 경우 에러 메시지 반환
        try:
            email_verfi = Email.objects.get(email=email)
        except Email.DoesNotExist:
            return JsonResponse({'message': '등록되지 않은 이메일입니다.'}, status=404)

        # 이메일이 존재하면서 인증번호가 일치하지 않는 경우 에러 메시지 반환
        if email_verfi.auth_num != auth_num:
            return JsonResponse({'message': '인증번호가 일치하지 않습니다.'}, status=400)

        # 인증번호 일치 시 성공 메시지 반환
        return JsonResponse({'message': '인증되었습니다.'})


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = UserPasswordChange
    queryset = User.objects.all()
    lookup_field = 'email'

    @swagger_auto_schema(
        operation_summary='비밀번호 변경 PUT API',
    )
    def put(self, request, *args, **kwargs):
        email = kwargs.get('email')
        password = request.data.get('password')
        try:
            user = self.get_object()
            user.password = password
            user.save()
            return Response({'message': '비밀번호가 변경되었습니다.'})
        except User.DoesNotExist:
            return Response({'message': '일치하는 이메일이 없습니다.'})


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    @swagger_auto_schema(
        operation_summary='로그인 POST API',
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(request, email=email, password=password)
        print("유저 반환값:",user)

        if user is not None:
            # 로그인 성공
            return Response({"status": "success", "message": "로그인 성공"}, status=status.HTTP_200_OK)
        else:
            # 이메일 또는 비밀번호가 일치하지 않음
            return Response({"status": "error", "message": "이메일 또는 비밀번호가 일치하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
    
#인스타그램 크롤링 GET API
class InstagramGet(APIView):
    @swagger_auto_schema(
        operation_summary='인스타그램 크롤링 데이터 GET API',
    )
    def get(self, request):
        instaData = Instagram.objects.all()
        serializers = InstagramSerializer(instaData, many=True)
        return Response(serializers.data)

#헤럳드 파이넨스 크롤링 GET API
class KhfnCrwawlingGet(APIView):
    @swagger_auto_schema(
        operation_summary='헤럴드 파이넨스 크롤링 데이터 GET API',
    )
    def get(self, request):
        khfnData = Khfncrawling.objects.all()
        serializers = KhfncrawlingSerializer(khfnData, many=True)
        return Response(serializers.data)

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
    

#-----------------------------------------------------API