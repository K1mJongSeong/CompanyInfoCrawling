from rest_framework import serializers
from rest_framework.parsers import MultiPartParser
from .models import Mkcrawling, Khcrawling, Crawling, Khfncrawling, Facebook, Instagram, User, Coruser, Login, Email, EmailVerfi

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('email',)

class EmailVerfiSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('email','auth_num')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','password','email','country')

class CorUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coruser
        fields = ('name','password','email','country','corporate_name','business_num')

class MkCrawlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mkcrawling
        fields = '__all__'

class KhCrawlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Khcrawling
        fields = '__all__'

class CrawlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crawling
        fields = '__all__'

class KhfncrawlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Khfncrawling
        fields = '__all__'

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