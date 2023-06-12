from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from rest_framework_swagger.renderers import SwaggerUIRenderer
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes#api
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.core.mail import EmailMessage
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema, force_serializer_instance
from drf_yasg import openapi
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, Http404
from django.core.mail import EmailMessage,send_mail
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from django.conf import settings
from django.views.generic import View
from datetime import datetime, timedelta
from . import mkcrawling2, navercrawling, navercrawling2
from . import mkcrawling, khcrawling, khfncrawling
from .models import Crawling, Khcrawling, Mkcrawling, Khfncrawling, Instagram, Facebook, User, Coruser, Login, Email, EmailVerfi, Qna, PuchasedSales
from .serializers import CrawlingSerializer, KhCrawlingSerializer, MkCrawlingSerializer, KhfncrawlingSerializer, UserSerializer, CorUserSerializer, InstagramSerializer, LoginSerializer, EmailSerializer, EmailVerfiSerailizer, UserPasswordChange, QnaSerializer, LoginOutSerializer, UserCorUserSerializer, UserWithdrawalSerializer, CorUserWithdrawalSerializer
from .facebook import fetch_facebook_data, save_facebook_data
from .insta import scrape_instagram
import string
import random
from datetime import datetime, timedelta


#-----------------------------------------------------크롤링 동작
def start_navercrawling(request):
    navercrawling.schedule_crawling()  # 크롤링 코드를 실행합니다. company_list
    return JsonResponse({"status": "정상", "message": "네이버 뉴스 크롤링 시작."})

def start_navercrawling2(request):
    navercrawling2.start_navercrawling2()  # 크롤링 코드를 실행합니다. company_list
    return JsonResponse({"status": "정상", "message": "네이버 뉴스 크롤링 시작."})

def start_khcrawling(requset):
    khcrawling.start_kh()
    return JsonResponse({"message":"헤럴드경제 크롤링 시작."})

def start_khfncrawling(requset):
    khfncrawling.start_khfn()
    return JsonResponse({"message":"헤럴드 파이넨스 크롤링 시작."})

def start_mkcrawling(requset):
    mkcrawling.start_mk()
    return JsonResponse({"message":"매일경제 모든 뉴스 크롤링 시작."})

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


class QnaListAPI(generics.ListAPIView):
    serializer_class = QnaSerializer

    @swagger_auto_schema(
            operation_summary='Q&A GET API'
    )
    def get_queryset(self):
        page_num = self.kwargs['page_num']
        return Qna.objects.filter(page_num=page_num)

class SendEmailVerificationView(GenericAPIView):
    serializer_class = EmailSerializer
    
    @swagger_auto_schema(
        operation_summary='이메일 POST API',
    )
    def post(self, request, *args, **kwargs):
        # POST 요청에서 이메일 주소 가져오기
        email = request.data.get('email')

        # 5자리 랜덤 인증번호 생성
        verification_code = get_random_string(length=5, allowed_chars=string.ascii_letters)

        html_content = f"""
            <html
        xmlns="http://www.w3.org/1999/xhtml"
        xmlns:v="urn:schemas-microsoft-com:vml"
        xmlns:o="urn:schemas-microsoft-com:office:office"
        >
        <head>
            <link
            href="https://fonts.googleapis.com/css?family=Cabin:400,700"
            rel="stylesheet"
            type="text/css"
            />
        </head>
        <body
            class="clean-body u_body"
            style="
            margin: 0;
            padding: 0;
            -webkit-text-size-adjust: 100%;
            background-color: #f9f9f9;
            color: #000000;
            "
        >
            <table
            id="u_body"
            style="
                border-collapse: collapse;
                table-layout: fixed;
                border-spacing: 0;
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                vertical-align: top;
                min-width: 320px;
                margin: 0 auto;
                background-color: #f9f9f9;
                width: 100%;
            "
            cellpadding="0"
            cellspacing="0"
            >
            <tbody>
                <tr style="vertical-align: top">
                <td
                    style="
                    word-break: break-word;
                    border-collapse: collapse !important;
                    vertical-align: top;
                    "
                >
                    <div
                    class="u-row-container"
                    style="padding: 0px; background-color: transparent"
                    >
                    <div
                        class="u-row"
                        style="
                        margin: 0 auto;
                        min-width: 320px;
                        max-width: 600px;
                        overflow-wrap: break-word;
                        word-wrap: break-word;
                        word-break: break-word;
                        background-color: transparent;
                        "
                    >
                        <div
                        style="
                            border-collapse: collapse;
                            display: table;
                            width: 100%;
                            height: 100%;
                            background-color: transparent;
                        "
                        >
                        <div
                            class="u-col u-col-100"
                            style="
                            max-width: 320px;
                            min-width: 600px;
                            display: table-cell;
                            vertical-align: top;
                            "
                        >
                            <div style="height: 100%; width: 100% !important">
                            <div
                                style="
                                box-sizing: border-box;
                                height: 100%;
                                padding: 0px;
                                border-top: 0px solid transparent;
                                border-left: 0px solid transparent;
                                border-right: 0px solid transparent;
                                border-bottom: 0px solid transparent;
                                "
                            ></div>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>

                    <div
                    class="u-row-container"
                    style="padding: 0px; background-color: transparent"
                    >
                    <div
                        class="u-row"
                        style="
                        margin: 0 auto;
                        min-width: 320px;
                        max-width: 600px;
                        overflow-wrap: break-word;
                        word-wrap: break-word;
                        word-break: break-word;
                        background-color: #ffffff;
                        "
                    >
                        <div
                        style="
                            border-collapse: collapse;
                            display: table;
                            width: 100%;
                            height: 100%;
                            background-color: transparent;
                        "
                        >
                        <div
                            class="u-col u-col-100"
                            style="
                            max-width: 320px;
                            min-width: 600px;
                            display: table-cell;
                            vertical-align: top;
                            "
                        >
                            <div style="height: 100%; width: 100% !important">
                            <div
                                style="
                                box-sizing: border-box;
                                height: 100%;
                                padding: 0px;
                                border-top: 0px solid transparent;
                                border-left: 0px solid transparent;
                                border-right: 0px solid transparent;
                                border-bottom: 0px solid transparent;
                                "
                            >
                                <table
                                style="font-family: 'Cabin', sans-serif"
                                role="presentation"
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                border="0"
                                >
                                <tbody>
                                    <tr>
                                    <td
                                        style="
                                        overflow-wrap: break-word;
                                        word-break: break-word;
                                        padding: 20px;
                                        font-family: 'Cabin', sans-serif;
                                        "
                                        align="left"
                                    >
                                        <table
                                        width="100%"
                                        cellpadding="0"
                                        cellspacing="0"
                                        border="0"
                                        >
                                        <tr>
                                            <td
                                            style="
                                                padding-right: 0px;
                                                padding-left: 0px;
                                            "
                                            align="center"
                                            >
                                            <img
                                                align="center"
                                                border="0"
                                                src="https://item.kakaocdn.net/do/dc9561970173c28a13654c3f14180b4b617ea012db208c18f6e83b1a90a7baa7"
                                                alt="Image"
                                                title="Image"
                                                style="
                                                outline: none;
                                                text-decoration: none;
                                                -ms-interpolation-mode: bicubic;
                                                clear: both;
                                                display: inline-block !important;
                                                border: none;
                                                height: auto;
                                                float: none;
                                                width: 32%;
                                                max-width: 179.2px;
                                                "
                                                width="179.2"
                                            />
                                            </td>
                                        </tr>
                                        </table>
                                    </td>
                                    </tr>
                                </tbody>
                                </table>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>

                    <div
                    class="u-row-container"
                    style="padding: 0px; background-color: transparent"
                    >
                    <div
                        class="u-row"
                        style="
                        margin: 0 auto;
                        min-width: 320px;
                        max-width: 600px;
                        overflow-wrap: break-word;
                        word-wrap: break-word;
                        word-break: break-word;
                        background-color: #17217a;
                        "
                    >
                        <div
                        style="
                            border-collapse: collapse;
                            display: table;
                            width: 100%;
                            height: 100%;
                            background-color: transparent;
                            display: flex;
                            flex-direction: column;
                        "
                        >
                        <div
                            class="u-col u-col-100"
                            style="
                            max-width: 320px;
                            min-width: 600px;
                            display: table-cell;
                            vertical-align: top;
                            "
                        >
                            <div style="height: 100%; width: 100% !important">
                            <div
                                style="
                                box-sizing: border-box;
                                height: 100%;
                                padding: 0px;
                                border-top: 0px solid transparent;
                                border-left: 0px solid transparent;
                                border-right: 0px solid transparent;
                                border-bottom: 0px solid transparent;
                                "
                            >
                                <table
                                style="font-family: 'Cabin', sans-serif"
                                role="presentation"
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                border="0"
                                >
                                <tbody>
                                    <tr>
                                    <td
                                        style="
                                        overflow-wrap: break-word;
                                        word-break: break-word;
                                        padding: 40px 10px 10px;
                                        font-family: 'Cabin', sans-serif;
                                        "
                                        align="left"
                                    >
                                        <table
                                        width="100%"
                                        cellpadding="0"
                                        cellspacing="0"
                                        border="0"
                                        >
                                        <tr>
                                            <td
                                            style="
                                                padding-right: 0px;
                                                padding-left: 0px;
                                            "
                                            align="center"
                                            >
                                            <img
                                                align="center"
                                                border="0"
                                                src="https://cdn.templates.unlayer.com/assets/1597218650916-xxxxc.png"
                                                alt="Image"
                                                title="Image"
                                                style="
                                                outline: none;
                                                text-decoration: none;
                                                -ms-interpolation-mode: bicubic;
                                                clear: both;
                                                display: inline-block !important;
                                                border: none;
                                                height: auto;
                                                float: none;
                                                width: 26%;
                                                max-width: 150.8px;
                                                "
                                                width="150.8"
                                            />
                                            </td>
                                        </tr>
                                        </table>
                                    </td>
                                    </tr>
                                </tbody>
                                </table>

                                <table
                                style="font-family: 'Cabin', sans-serif"
                                role="presentation"
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                border="0"
                                >
                                <tbody>
                                    <tr>
                                    <td
                                        style="
                                        overflow-wrap: break-word;
                                        word-break: break-word;
                                        padding: 10px;
                                        font-family: 'Cabin', sans-serif;
                                        "
                                        align="left"
                                    >
                                        <div
                                        style="
                                            font-size: 14px;
                                            color: #e5eaf5;
                                            line-height: 140%;
                                            text-align: center;
                                            word-wrap: break-word;
                                        "
                                        >
                                        <p style="font-size: 14px; line-height: 140%">
                                            <strong
                                            >T H A N K S&nbsp; &nbsp;F O R&nbsp;
                                            &nbsp;S I G N I N G&nbsp; &nbsp;U P
                                            !</strong
                                            >
                                        </p>
                                        </div>
                                    </td>
                                    </tr>
                                </tbody>
                                </table>

                                <table
                                style="font-family: 'Cabin', sans-serif"
                                role="presentation"
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                border="0"
                                >
                                <tbody>
                                    <tr>
                                    <td
                                        style="
                                        overflow-wrap: break-word;
                                        word-break: break-word;
                                        padding: 0px 10px 31px;
                                        font-family: 'Cabin', sans-serif;
                                        "
                                        align="left"
                                    >
                                        <div
                                        style="
                                            font-size: 14px;
                                            color: #e5eaf5;
                                            line-height: 140%;
                                            text-align: center;
                                            word-wrap: break-word;
                                        "
                                        >
                                        <p style="font-size: 14px; line-height: 140%">
                                            <span
                                            style="
                                                font-size: 28px;
                                                line-height: 39.2px;
                                            "
                                            ><strong
                                                ><span
                                                style="
                                                    line-height: 39.2px;
                                                    font-size: 28px;
                                                "
                                                >Verify Your E-mail Address
                                                </span></strong
                                            >
                                            </span>
                                        </p>
                                        </div>
                                    </td>
                                    </tr>
                                </tbody>
                                </table>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>

                    <div
                    class="u-row-container"
                    style="padding: 0px; background-color: transparent"
                    >
                    <div
                        class="u-row"
                        style="
                        margin: 0 auto;
                        min-width: 320px;
                        max-width: 600px;
                        overflow-wrap: break-word;
                        word-wrap: break-word;
                        word-break: break-word;
                        background-color: #ffffff;
                        "
                    >
                        <div
                        style="
                            border-collapse: collapse;
                            display: table;
                            width: 100%;
                            height: 100%;
                            background-color: transparent;
                        "
                        >
                        <div
                            class="u-col u-col-100"
                            style="
                            max-width: 320px;
                            min-width: 600px;
                            display: table-cell;
                            vertical-align: top;
                            "
                        >
                            <div style="height: 100%; width: 100% !important">
                            <div
                                style="
                                box-sizing: border-box;
                                height: 100%;
                                padding: 0px;
                                border-top: 0px solid transparent;
                                border-left: 0px solid transparent;
                                border-right: 0px solid transparent;
                                border-bottom: 0px solid transparent;
                                "
                            >
                                <table
                                style="font-family: 'Cabin', sans-serif"
                                role="presentation"
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                border="0"
                                >
                                <tbody>
                                    <tr>
                                    <td
                                        style="
                                        overflow-wrap: break-word;
                                        word-break: break-word;
                                        padding: 33px 55px;
                                        font-family: 'Cabin', sans-serif;
                                        "
                                        align="left"
                                    >
                                        <div
                                        style="
                                            font-size: 14px;
                                            line-height: 160%;
                                            text-align: center;
                                            word-wrap: break-word;
                                        "
                                        >
                                        <p style="font-size: 14px; line-height: 160%">
                                            <span
                                            style="
                                                font-size: 22px;
                                                line-height: 35.2px;
                                            "
                                            >Hi,
                                            </span>
                                        </p>
                                        <p style="font-size: 14px; line-height: 160%">
                                            <span
                                            style="
                                                font-size: 18px;
                                                line-height: 28.8px;
                                            "
                                            >Thank you for using sentinel Korea
                                            KYC.<br />
                                            Please authenticate the code below at
                                            sentinel Korea KYC!
                                            </span>
                                        </p>
                                        </div>
                                    </td>
                                    </tr>
                                </tbody>
                                </table>

                                <table
                                style="font-family: 'Cabin', sans-serif"
                                role="presentation"
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                border="0"
                                >
                                <tbody>
                                    <tr>
                                    <td
                                        style="
                                        overflow-wrap: break-word;
                                        word-break: break-word;
                                        padding: 10px;
                                        font-family: 'Cabin', sans-serif;
                                        "
                                        align="left"
                                    >
                                        <div align="center">
                                        <div
                                            href=""
                                            target="_blank"
                                            class="v-button"
                                            style="
                                            box-sizing: border-box;
                                            display: inline-block;
                                            font-family: 'Cabin', sans-serif;
                                            text-decoration: none;
                                            -webkit-text-size-adjust: none;
                                            text-align: center;
                                            color: #ffffff;
                                            background-color: #ff6600;
                                            border-radius: 4px;
                                            -webkit-border-radius: 4px;
                                            -moz-border-radius: 4px;
                                            width: auto;
                                            max-width: 100%;
                                            overflow-wrap: break-word;
                                            word-break: break-word;
                                            word-wrap: break-word;
                                            mso-border-alt: none;
                                            font-size: 14px;
                                            "
                                        >
                                            <span
                                            style="
                                                display: block;
                                                padding: 14px 44px 13px;
                                                line-height: 120%;
                                            "
                                            ><span style="line-height: 16.8px"
                                                ><strong
                                                ><span style="line-height: 16.8px"
                                                    >{verification_code}</span
                                                ></strong
                                                >
                                            </span>
                                            </span>
                                        </div>
                                        <!--[if mso]></center></v:roundrect><![endif]-->
                                        </div>
                                    </td>
                                    </tr>
                                </tbody>
                                </table>

                                <table
                                style="font-family: 'Cabin', sans-serif"
                                role="presentation"
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                border="0"
                                >
                                <tbody>
                                    <tr>
                                    <td
                                        style="
                                        overflow-wrap: break-word;
                                        word-break: break-word;
                                        padding: 33px 55px 60px;
                                        font-family: 'Cabin', sans-serif;
                                        "
                                        align="left"
                                    >
                                        <div
                                        style="
                                            font-size: 14px;
                                            line-height: 160%;
                                            text-align: center;
                                            word-wrap: break-word;
                                        "
                                        >
                                        <p style="line-height: 160%; font-size: 14px">
                                            <span
                                            style="
                                                font-size: 18px;
                                                line-height: 28.8px;
                                            "
                                            >Thanks,</span
                                            >
                                        </p>
                                        <p style="line-height: 160%; font-size: 14px">
                                            <span
                                            style="
                                                font-size: 18px;
                                                line-height: 28.8px;
                                            "
                                            >The Company Team</span
                                            >
                                        </p>
                                        </div>
                                    </td>
                                    </tr>
                                </tbody>
                                </table>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>

                    <div
                    class="u-row-container"
                    style="padding: 0px; background-color: transparent"
                    >
                    <div
                        class="u-row"
                        style="
                        margin: 0 auto;
                        min-width: 320px;
                        max-width: 600px;
                        overflow-wrap: break-word;
                        word-wrap: break-word;
                        word-break: break-word;
                        background-color: #e5eaf5;
                        "
                    >
                        <div
                        style="
                            border-collapse: collapse;
                            display: table;
                            width: 100%;
                            height: 100%;
                            background-color: transparent;
                        "
                        >
                        <div
                            class="u-col u-col-100"
                            style="
                            max-width: 320px;
                            min-width: 600px;
                            display: table-cell;
                            vertical-align: top;
                            "
                        >
                            <div style="height: 100%; width: 100% !important">
                            <div
                                style="
                                box-sizing: border-box;
                                height: 100%;
                                padding: 0px;
                                border-top: 0px solid transparent;
                                border-left: 0px solid transparent;
                                border-right: 0px solid transparent;
                                border-bottom: 0px solid transparent;
                                "
                            >
                                <table
                                style="font-family: 'Cabin', sans-serif"
                                role="presentation"
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                border="0"
                                ></table>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>

                    <div
                    class="u-row-container"
                    style="padding: 0px; background-color: transparent"
                    >
                    <div
                        class="u-row"
                        style="
                        margin: 0 auto;
                        min-width: 320px;
                        max-width: 600px;
                        overflow-wrap: break-word;
                        word-wrap: break-word;
                        word-break: break-word;
                        background-color: #17217a;
                        "
                    >
                        <div
                        style="
                            border-collapse: collapse;
                            display: table;
                            width: 100%;
                            height: 100%;
                            background-color: transparent;
                        "
                        >
                        <div
                            class="u-col u-col-100"
                            style="
                            max-width: 320px;
                            min-width: 600px;
                            display: table-cell;
                            vertical-align: top;
                            "
                        >
                            <div style="height: 100%; width: 100% !important">
                            <div
                                style="
                                box-sizing: border-box;
                                height: 100%;
                                padding: 0px;
                                border-top: 0px solid transparent;
                                border-left: 0px solid transparent;
                                border-right: 0px solid transparent;
                                border-bottom: 0px solid transparent;
                                "
                            >
                                <table
                                style="font-family: 'Cabin', sans-serif"
                                role="presentation"
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                border="0"
                                >
                                <tbody>
                                    <tr>
                                    <td
                                        style="
                                        overflow-wrap: break-word;
                                        word-break: break-word;
                                        padding: 10px;
                                        font-family: 'Cabin', sans-serif;
                                        "
                                        align="left"
                                    >
                                        <div
                                        style="
                                            font-size: 14px;
                                            color: #fafafa;
                                            line-height: 180%;
                                            text-align: center;
                                            word-wrap: break-word;
                                        "
                                        >
                                        <p style="font-size: 14px; line-height: 180%">
                                            <span
                                            style="
                                                font-size: 16px;
                                                line-height: 28.8px;
                                            "
                                            >Copyrights © Sentinel Korea KYC All
                                            Rights Reserved</span
                                            >
                                        </p>
                                        </div>
                                    </td>
                                    </tr>
                                </tbody>
                                </table>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>
                </td>
                </tr>
            </tbody>
            </table>
        </body>
        </html>
        """


        # 이메일 전송
        success = send_mail(
            '회원가입 인증번호',  # 제목
            f'인증번호: {verification_code}',  # 내용
            settings.EMAIL_HOST_USER,  # 발신자 이메일
            [email],  # 수신자 이메일
            fail_silently=False,  # 실패 시 에러를 발생시키도록 설정
            html_message = html_content,
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

    @swagger_auto_schema(
        operation_summary='이메일 인증번호 POST API',
    )
    def post(self, request, *args, **kwargs):
        # POST 요청에서 이메일과 인증번호 가져오기
        email = request.data.get('email')
        auth_num = request.data.get('auth_num')

        # 이메일이 존재하지 않는 경우 에러 메시지 반환
        try:
            email_verfi = Email.objects.filter(email=email).last()
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


class UserLoginView2(GenericAPIView):
    serializer_class = LoginSerializer
    
    @swagger_auto_schema(
        operation_summary='로그인 POST API',
    )
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()
        cor_user = Coruser.objects.filter(email=email).first()

        print(user)
        print(cor_user)
        if user is None and cor_user is None:
            return Response(
                {"message": "존재하지 않는 아이디입니다."}, status=status.HTTP_400_BAD_REQUEST
            )
        if (user and user.password != password) or (cor_user and cor_user.password != password):
            return Response({"message":"비밀번호가 틀렸습니다."},status=status.HTTP_400_BAD_REQUEST)

        if user:
            user.is_login = '1'
            user.last_login = datetime.now()
            login_record, created = Login.objects.get_or_create(email=email)
            login_record.last_login = datetime.now()
            login_record.save()
            user.save()
            return Response({"message": "로그인에 성공했습니다."}, status=status.HTTP_200_OK)
        elif cor_user:
            cor_user.is_login = '1'
            cor_user.last_login = datetime.now()
            login_record, created = Login.objects.get_or_create(email=email)
            login_record.last_login = datetime.now()
            login_record.save()
            cor_user.save()
            return Response({"message": "로그인에 성공했습니다."}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "로그인에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST
            )


class UserLogoutView(GenericAPIView):
    serializer_class = LoginOutSerializer

    @swagger_auto_schema(
        operation_summary='로그아웃 POST API',
    )
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')

        user = User.objects.filter(email=email).first()
        cor_user = Coruser.objects.filter(email=email).first()
        login = Login.objects.filter(email=email).first()

        if user is None and cor_user is None:
            return Response(
                {"message": "존재하지 않는 아이디입니다."}, status=status.HTTP_400_BAD_REQUEST
            )
        
        logout_msg = ""  # 변수 초기화

        if user and user.is_login == '1':
            user.is_login = '0'
            user.save()
            logout_msg = "로그아웃에 성공하였습니다."

        if cor_user and cor_user.is_login == '1':
            cor_user.is_login = '0'
            cor_user.save()
            logout_msg = "로그아웃에 성공하였습니다."

        if logout_msg:
            return Response(
                {"message": logout_msg}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "이미 로그아웃 상태입니다."}, status=status.HTTP_400_BAD_REQUEST
            )


class UserLoginStatusView(APIView):
    def get_objects(self, email):
        user = User.objects.filter(email=email).first()
        coruser = Coruser.objects.filter(email=email).first()

        if user is None and coruser is None:
            raise Http404("회원을 찾지 못했습니다.")
        
        user_name = user.name if user else None
        coruser_name = coruser.name if coruser else None
        auth_state = user.auth_state if user else coruser.auth_state if coruser else None

        return {'user_name': user_name, 'coruser_name': coruser_name, 'auth_state': auth_state}

    @swagger_auto_schema(
        operation_summary='로그인 상태',
    )
    def get(self, request, email):
        data = self.get_objects(email)
        serializer = UserCorUserSerializer(data)
        
        if serializer is None:
            return Response({"message":"아이디가 존재하지 않습니다"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()

        coruser = Coruser.objects.filter(email=email).first()

        if (user and user.is_login == '1') or (coruser and coruser.is_login =='1'):
            return Response({"message":"로그인 상태입니다.", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"로그아웃 상태입니다.", "data": serializer.data}, status=status.HTTP_200_OK)



# class UserLoginStatusView(APIView):
#     serializer_class = UserSerializer
#     lookup_field=("email")

#     @swagger_auto_schema(
#         operation_summary='로그인 상태 확인 GET API',
#     )
#     def get(self, request, *args, **kwargs):
#         email = self.request.query_params.get('email')
#         print(email)
#         user = User.objects.filter(email=email).first()
#         print(user)

#         if user is None:
#             return Response(
#                 {"message": "존재하지 않는 아이디입니다."}, status=status.HTTP_400_BAD_REQUEST
#             )
#         if user.is_login == '1':
#             return Response({
#                 "message": "로그인 중입니다."
#             },status=status.HTTP_200_OK)
#         else:
#             return Response({"message":"로그아웃 상태입니다."},status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(
            operation_summary='일반회원 GET API'
    )
    def get_queryset(self):
        email = self.kwargs['email']
        return User.objects.filter(email=email)


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'

    @swagger_auto_schema(
        operation_summary='일반회원 PUT API'
    )
    def put(self, request, *args, **kwargs):
        response = super().put(request, *args, **kwargs)
        return Response({"message":"변경되었습니다.", "data": response.data})



class CorUserListView(generics.ListAPIView):
    serializer_class = CorUserSerializer

    @swagger_auto_schema(
            operation_summary='법인회원 GET API'
    )
    def get_queryset(self):
        email = self.kwargs['email']
        return Coruser.objects.filter(email=email)


class CorUserUpdateView(generics.UpdateAPIView):
    queryset = Coruser.objects.all()
    serializer_class = CorUserSerializer
    lookup_field = 'email'

    @swagger_auto_schema(
        operation_summary='법인회원 PUT API'
    )
    def put(self, request, *args, **kwargs):
        response = super().put(request, *args, **kwargs)
        return Response({"message":"변경되었습니다.", "data": response.data})


class UserWithdrawalUpdate(generics.UpdateAPIView, mixins.UpdateModelMixin):
        serializer_class = UserWithdrawalSerializer
        queryset = User.objects.all()
        lookup_field = 'email'
        @swagger_auto_schema(
                operation_summary='일반 회원탈퇴 PUT'
        )
        def put(self, request, *args, **kwargs):
            response = super().put(request, *args, **kwargs)
            return Response({"message":"변경되었습니다.", "data": response.data})

class CorUserWithdrawalUpdate(generics.UpdateAPIView, mixins.UpdateModelMixin):
        serializer_class = CorUserWithdrawalSerializer
        queryset = Coruser.objects.all()
        lookup_field = 'email'
        @swagger_auto_schema(
                operation_summary='법인 회원탈퇴 PUT'
        )
        def put(self, request, *args, **kwargs):
            response = super().put(request, *args, **kwargs)
            return Response({"message":"변경되었습니다.", "data": response.data})


# class LoginView(GenericAPIView):
#     serializer_class = LoginSerializer
#     @swagger_auto_schema(
#         operation_summary='로그인 POST API',
#     )
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         email = serializer.validated_data['email']
#         password = serializer.validated_data['password']

#         user = authenticate(request, email=email, password=password)
#         print("유저 반환값:",user)

#         if user is not None:
#             # 로그인 성공
#             return Response({"status": "success", "message": "로그인 성공"}, status=status.HTTP_200_OK)
#         else:
#             # 이메일 또는 비밀번호가 일치하지 않음
#             return Response({"status": "error", "message": "이메일 또는 비밀번호가 일치하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

#네이버 크롤링 GET API
class NaverCrwawlingGet(APIView):
    @swagger_auto_schema(
        operation_summary='네이버 크롤링 데이터 GET API',
    )
    def get(self, request, kr_content):
        queries = [Q(kr_content__icontains=word) for word in kr_content.split()]
        query = queries.pop()
        for item in queries:
            query |= item
        naverData = Crawling.objects.filter(query)
        serializers = CrawlingSerializer(naverData, many=True)
        return Response(serializers.data)

#매일경제 크롤링 GET API
class MkCrwawlingGet(APIView):
    @swagger_auto_schema(
        operation_summary='매일경제 크롤링 데이터 GET API',
    )
    def get(self, request, kr_content):
        queries = [Q(kr_content__icontains=word) for word in kr_content.split()]
        query = queries.pop()
        for item in queries:
            query |= item
        mkData = Mkcrawling.objects.filter(query)
        serializers = MkCrawlingSerializer(mkData, many=True)
        return Response(serializers.data)
    
#헤럴드경제 크롤링 GET API
class KhCrwawlingGet(APIView):
    @swagger_auto_schema(
        operation_summary='헤럴드경제 크롤링 데이터 GET API',
    )
    def get(self, request, kr_content):
        queries = [Q(kr_content__icontains=word) for word in kr_content.split()]
        query = queries.pop()
        for item in queries:
            query |= item
        khData = Khcrawling.objects.filter(query)
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
        operation_summary='헤럴드파이넨스 크롤링 데이터 GET API',
    )
    def get(self, request, kr_content):
        queries = [Q(kr_content__icontains=word) for word in kr_content.split()]
        query = queries.pop()
        for item in queries:
            query |= item
        khfnData = Khfncrawling.objects.filter(query)
        serializers = KhfncrawlingSerializer(khfnData, many=True)
        return Response(serializers.data)

class UserLogin(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @swagger_auto_schema(
        operation_summary=' 일반 로그인 POST API'
    )
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if User.objects.filter(email=email).exists():
            return Response({"message": "중복된 이메일이 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)
    

class CorUserLogin(generics.ListCreateAPIView):
    serializer_class = CorUserSerializer
    queryset = Coruser.objects.all()

    @swagger_auto_schema(
        operation_summary=' 법인 로그인 POST API'
    )
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if User.objects.filter(email=email).exists():
            return Response({"message": "중복된 이메일이 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)
    
#-----------------------------------------------------API