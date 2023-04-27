from django.db import models


class Crawling(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    news_date = models.DateTimeField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    news_agency = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Crawling'


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    secession = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    payment_role = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'