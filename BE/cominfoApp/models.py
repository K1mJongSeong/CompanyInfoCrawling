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
    fb_id = models.AutoField(primary_key=True)
    message = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facebook'      

class Instagram(models.Model):
    ins_id = models.AutoField(primary_key=True, db_index=True)
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
    is_login = models.CharField(max_length=1, blank=True, null=True)
    auth_state = models.CharField(max_length=10, blank=True, null=True)
    sus_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'

class Coruser(models.Model): #법인 로그인
    cor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    corporate_name = models.CharField(max_length=255, blank=True, null=True)
    business_num = models.CharField(max_length=100, blank=True, null=True)
    is_login = models.CharField(max_length=1, blank=True, null=True)
    auth_state = models.CharField(max_length=10, blank=True, null=True)
    sus_reason = models.CharField(max_length=255, blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'corUser'

class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Login'

class Email(models.Model):
    email_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    auth_num = models.CharField(max_length=10, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email'

class EmailVerfi(models.Model):
    email = models.CharField(primary_key=True, max_length=100)
    verfication_num = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_verfi'

class Qna(models.Model):
    qna_id = models.AutoField(primary_key=True,verbose_name='NO')
    question = models.TextField(blank=True, null=True,verbose_name='제목')
    answer = models.TextField(blank=True, null=True,verbose_name='답변')
    create_at = models.DateTimeField(blank=True, null=True,verbose_name='등록일')
    modified_at = models.DateTimeField(blank=True, null=True)
    writer = models.CharField(max_length=50, blank=True, null=True,verbose_name='작성자')
    question_content = models.TextField(blank=True, null=True,verbose_name='내용')
    

    EXPOSURE_STATE_CHOICES = [
        ('메인','메인'),
        ('노출','노출'),
        ('미노출','미노출'),
    ]
    exposure = models.CharField(max_length=45, blank=True, null=True,verbose_name='노출여부',choices=EXPOSURE_STATE_CHOICES)

    class Meta:
        managed = False
        db_table = 'Qna'
        verbose_name = 'Q&A'
        verbose_name_plural = 'Q&A'

class PuchasedSales(models.Model):
    ps_id = models.AutoField(primary_key=True,verbose_name='NO')
    trans_num = models.CharField(max_length=100, blank=True, null=True,verbose_name='거래번호')
    trans_item = models.CharField(max_length=100, blank=True, null=True,verbose_name='거래항목')
    trans_name = models.CharField(max_length=100, blank=True, null=True,verbose_name='거래자')
    trans_date = models.DateField(blank=True, null=True,verbose_name='거래일')
    payment = models.CharField(max_length=100, blank=True, null=True,verbose_name='결제금액')
    pay_method = models.CharField(max_length=100, blank=True, null=True,verbose_name='결제방식')

    STATE_CHOICES = [
        ('거래완료','거래완료'),
        ('거래취소','거래취소'),
    ]
    state = models.CharField(max_length=10, blank=True, null=True,verbose_name='상태',choices=STATE_CHOICES)
    class Meta:
        managed = False
        db_table = 'Puchased_sales'
        verbose_name = '거래목록'
        verbose_name_plural = '거래목록'