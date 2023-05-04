from django.db import models


class Crawling(models.Model):
    crawling_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    news_date = models.DateTimeField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    news_agency = models.CharField(max_length=45, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    collect_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Crawling'


class Khcrawling(models.Model):
    khcrawling_id = models.AutoField(db_column='khCrawling_id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True, null=True)
    news_date = models.DateTimeField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    news_agency = models.CharField(max_length=45, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    collect_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'khCrawling'


class Mkcrawling(models.Model):
    mkcrawling_id = models.AutoField(db_column='mkCrawling_id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True, null=True)
    news_date = models.DateTimeField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    news_agency = models.CharField(max_length=45, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    collect_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mkCrawling'

class Khfncrawling(models.Model):
    fn_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    news_date = models.DateTimeField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    news_agency = models.CharField(max_length=45, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    collect_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'khfnCrawling'


class Facebook(models.Model):
    meta_id = models.IntegerField(primary_key=True)
    message = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facebook'      

class Instagram(models.Model):
    ins_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    news_date = models.DateTimeField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    collect_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instagram'

class User(models.Model): #일반로그인
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    password_ck = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'

class Coruser(models.Model): #법인 로그인
    cor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    password_ck = models.CharField(max_length=100, blank=True, null=True)
    corporate_name = models.CharField(max_length=255, blank=True, null=True)
    business_num = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corUser'