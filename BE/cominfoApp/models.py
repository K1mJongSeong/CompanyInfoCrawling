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