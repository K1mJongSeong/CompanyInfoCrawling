from rest_framework import serializers
from rest_framework.parsers import MultiPartParser
from .models import Mkcrawling, Khcrawling, Crawling, Khfncrawling

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