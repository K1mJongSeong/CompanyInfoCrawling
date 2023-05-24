"""companyinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework import routers
from rest_framework.decorators import api_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view
from cominfoApp.views import start_navercrawling, start_mkcrawling, start_khcrawling, start_khfncrawling, fetch_and_save_fb_data, get_instagram_posts, start_mkcrawling2, start_navercrawling2
from cominfoApp.views import  KhCrwawlingGet, KhfnCrwawlingGet, MkCrwawlingGet, InstagramGet, UserLogin, CorUserLogin, SendEmailVerificationView, VerifyEmailView, ChangePasswordView, UserLoginView2, UserLogoutView, UserLoginStatusView, UserListView, UserUpdateView, CorUserUpdateView, CorUserListView, UserWithdrawalUpdate, CorUserWithdrawalUpdate, QnaListAPI
schema_view = get_schema_view(
    openapi.Info(
        title="Open API", #타이틀
        default_version='v1', #버전
        description="시스템 API", #설명
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(AllowAny,),
) #Swagger API문서 스키마


urlpatterns = [
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),#Swagger API PATH
    path('admin/', admin.site.urls),
    #path('start_navercrawling/',start_navercrawling), #네이버뉴스(네이버API 따로 제공 받을 예정.)
    path('start_navercrawling2/',start_navercrawling2), #네이버뉴스(네이버API 따로 제공 받을 예정.)
    path('start_khcrawling/',start_khcrawling), #헤럴드경제
    path('start_khfncrawling/',start_khfncrawling), #헤럴드 파이넨스
    path('start_mkcrawling/',start_mkcrawling), #매일경제 모든 뉴스
    path('start_mkcrawling2/',start_mkcrawling2), #매일경제 모든 뉴스
    path('start_facebook/',fetch_and_save_fb_data), #페이스북
    path('get_instagram_posts/',get_instagram_posts), #인스타그램
    path('KhCrwawlingGet/',KhCrwawlingGet.as_view()), #헤럴드 경제 GET API
    path('MkCrwawlingGet/',MkCrwawlingGet.as_view()), #매일경제 GET API  
    path('InstagramGet/',InstagramGet.as_view()), #인스타그램 GET API
    path('KhfnCrwawlingGet',KhfnCrwawlingGet.as_view()), #헤럴드 파이넨스 GET API
    path('UserJoin/',UserLogin.as_view()), # 일반 로그인
    path('CorJoin/',CorUserLogin.as_view()), #법인 로그인
    #path('Login/',LoginView.as_view()), #로그인 검증
    path('SendEmail/', SendEmailVerificationView.as_view()),
    path('verfication/', VerifyEmailView.as_view()),
    path('ChangePassword/<str:email>', ChangePasswordView.as_view()),
    path("Login/", UserLoginView2.as_view()),
    path("UserLogout/", UserLogoutView.as_view()),
    path("UserLoginStatus/<str:email>/", UserLoginStatusView.as_view()),
    path("UserPUT/<str:email>/",UserUpdateView.as_view()),
    path("UserGET/<str:email>/", UserListView.as_view()),
    path("CorUserGET/<str:email>/",CorUserListView.as_view()),
    path("CorUserPUT/<str:email>/",CorUserUpdateView.as_view()),
    path("UserWithdrawalUpdate/<str:email>/", UserWithdrawalUpdate.as_view()),
    path("CorUserWithdrawalUpdate/<str:email>/", CorUserWithdrawalUpdate.as_view()),
    path("QnaListAPI/<str:page_num>", QnaListAPI.as_view()),
    #path('email/',send_email_verification),
]
