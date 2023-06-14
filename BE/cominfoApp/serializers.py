from rest_framework import serializers
from rest_framework.parsers import MultiPartParser
from .models import Mkcrawling, Khcrawling, Crawling, Khfncrawling, Facebook, Instagram, User, Coruser, Login, Email, EmailVerfi, Qna, Payment, CmpInfo
from datetime import datetime

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class QnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qna
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('email',)

class EmailVerfiSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('email','auth_num')

class UserSerializer(serializers.ModelSerializer):
    auth_state = serializers.CharField(default='정상')
    sub_date = serializers.DateTimeField(default=datetime.now())

    class Meta:
        model = User
        fields = ('name','password','email','country','auth_state','sub_date','phone')



class UserPasswordChange(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password')

class CorUserSerializer(serializers.ModelSerializer):
    auth_state = serializers.CharField(default='정상')
    sub_date = serializers.DateTimeField(default=datetime.now())

    class Meta:
        model = Coruser
        fields = ('name','password','email','country','corporate_name','business_num','auth_state','sub_date','phone')


class MkCrawlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mkcrawling
        fields = ('mkcrawling_id','title','news_date','link','news_agency','en_content','img','kr_content')

class KhCrawlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Khcrawling
        fields = ('khcrawling_id','title','news_date','link','news_agency','en_content','img','kr_content')

class CrawlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crawling
        fields = ('crawling_id','title','news_date','link','news_agency','en_content','img','kr_content')

class KhfncrawlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Khfncrawling
        fields = ('fn_id','title','news_date','link','news_agency','en_content','img','kr_content')

class FacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facebook
        fields = '__all__'

class InstagramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instagram
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('email','password')

class LoginOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('email',)

class UserCorUserSerializer(serializers.Serializer):
    user_name = serializers.CharField(allow_null=True)
    coruser_name = serializers.CharField(allow_null=True)
    auth_state = serializers.CharField(allow_null=True)

class UserWithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('auth_state',)

class CorUserWithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coruser
        fields = ('auth_state',)

class CmpInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpInfo
        fields = '__all__'