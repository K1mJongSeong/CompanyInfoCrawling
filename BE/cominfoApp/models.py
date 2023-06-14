from django.db import models


class Crawling(models.Model):#네이버
    crawling_id = models.AutoField(db_column='crawling_id',primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    news_date = models.DateTimeField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    news_agency = models.CharField(max_length=45, blank=True, null=True)
    en_content = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    collect_date = models.DateTimeField(blank=True, null=True)
    kr_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Crawling'


class Khcrawling(models.Model):
    khcrawling_id = models.AutoField(db_column='khCrawling_id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True, null=True)
    news_date = models.DateTimeField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    news_agency = models.CharField(max_length=45, blank=True, null=True)
    en_content = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    collect_date = models.DateField(blank=True, null=True)
    kr_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'khCrawling'


class Mkcrawling(models.Model):
    mkcrawling_id = models.AutoField(db_column='mkCrawling_id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True, null=True)
    news_date = models.DateTimeField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    news_agency = models.CharField(max_length=45, blank=True, null=True)
    en_content = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    collect_date = models.DateField(blank=True, null=True)
    kr_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mkCrawling'

class Khfncrawling(models.Model):
    fn_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    news_date = models.DateTimeField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    news_agency = models.CharField(max_length=45, blank=True, null=True)
    en_content = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    collect_date = models.DateField(blank=True, null=True)
    kr_content = models.TextField(blank=True, null=True)

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
    news_agency=models.CharField(max_length=45, blank=True, null=True)
    news_date = models.DateTimeField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    en_content = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    collect_date = models.DateField(blank=True, null=True)
    kr_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instagram'

class User(models.Model): #일반로그인
    user_id = models.IntegerField(primary_key=True, verbose_name="NO")
    name = models.CharField(max_length=100, blank=True, null=True,verbose_name="회원이름")
    password = models.CharField(max_length=100, blank=True, null=True,verbose_name="비밀번호")
    email = models.CharField(max_length=100, blank=True, null=True,verbose_name="이메일")
    country = models.CharField(max_length=100, blank=True, null=True,verbose_name="나라")
    is_login = models.CharField(max_length=1, blank=True, null=True)
    sus_reason = models.CharField(max_length=255, blank=True, null=True,verbose_name="정지사유")
    sub_date = models.DateTimeField(blank=True, null=True,verbose_name="가입일")
    last_login = models.DateTimeField(blank=True, null=True,verbose_name="최근 접속")
    phone = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'
        verbose_name = '회원관리'
        verbose_name_plural = '회원관리'
    
    AUTH_STATE_CHOICES = [
        ('정상','정상'),
        ('정지','정지'),
    ]
    auth_state = models.CharField(max_length=10, blank=True, null=True,verbose_name="계정상태",choices=AUTH_STATE_CHOICES)


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
    sub_date = models.DateTimeField(blank=True, null=True,verbose_name="가입일")
    last_login = models.DateTimeField(blank=True, null=True,verbose_name="최근 접속")
    phone = models.CharField(max_length=100, blank=True, null=True)
    

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
    page_num = models.CharField(max_length=10, blank=True, null=True)
    total_page_num = models.CharField(max_length=10, blank=True, null=True)
    

    EXPOSURE_STATE_CHOICES = [
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
    email = models.CharField(max_length=100, blank=True, null=True,verbose_name='이메일')

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

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_code = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    page_num = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Payment'


class CmpInfo(models.Model): #기업정보 
    cmp_id = models.AutoField(primary_key=True)
    cmpcd = models.CharField(db_column='cmpCd', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cmpnm = models.CharField(db_column='cmpNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cmpenm = models.CharField(db_column='cmpEnm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bizno = models.CharField(db_column='bizNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cmptypenm = models.CharField(db_column='cmpTypEnm', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estbdate = models.CharField(db_column='estbDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    indcd = models.CharField(db_column='indCd', max_length=100, blank=True, null=True)  # Field name made lowercase.
    empcnt = models.CharField(db_column='empCnt', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telno = models.CharField(db_column='telNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    faxtelno = models.CharField(db_column='faxTelNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enadr = models.CharField(db_column='enAdr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mnbizcont = models.CharField(db_column='mnBizCont', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pstncdnm1 = models.CharField(db_column='pstnCdNm1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm1 = models.CharField(db_column='mgrNm1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu1 = models.CharField(max_length=100, blank=True, null=True)
    crr1 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm2 = models.CharField(db_column='pstnCdNm2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm2 = models.CharField(db_column='mgrNm2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu2 = models.CharField(max_length=100, blank=True, null=True)
    crr2 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm3 = models.CharField(db_column='pstnCdNm3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm3 = models.CharField(db_column='mgrNm3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu3 = models.CharField(max_length=100, blank=True, null=True)
    crr3 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm4 = models.CharField(db_column='pstnCdNm4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm4 = models.CharField(db_column='mgrNm4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu4 = models.CharField(max_length=100, blank=True, null=True)
    crr4 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm5 = models.CharField(db_column='pstnCdNm5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm5 = models.CharField(db_column='mgrNm5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu5 = models.CharField(max_length=100, blank=True, null=True)
    crr5 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm6 = models.CharField(db_column='pstnCdNm6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm6 = models.CharField(db_column='mgrNm6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu6 = models.CharField(max_length=100, blank=True, null=True)
    crr6 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm7 = models.CharField(db_column='pstnCdNm7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm7 = models.CharField(db_column='mgrNm7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu7 = models.CharField(max_length=100, blank=True, null=True)
    crr7 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm8 = models.CharField(db_column='pstnCdNm8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm8 = models.CharField(db_column='mgrNm8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu8 = models.CharField(max_length=100, blank=True, null=True)
    crr8 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm9 = models.CharField(db_column='pstnCdNm9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm9 = models.CharField(db_column='mgrNm9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu9 = models.CharField(max_length=100, blank=True, null=True)
    crr9 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm10 = models.CharField(db_column='pstnCdNm10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm10 = models.CharField(db_column='mgrNm10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu10 = models.CharField(max_length=100, blank=True, null=True)
    crr10 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm11 = models.CharField(db_column='pstnCdNm11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm11 = models.CharField(db_column='mgrNm11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu11 = models.CharField(max_length=100, blank=True, null=True)
    crr11 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm12 = models.CharField(db_column='pstnCdNm12', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm12 = models.CharField(db_column='mgrNm12', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu12 = models.CharField(max_length=100, blank=True, null=True)
    crr12 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm13 = models.CharField(db_column='pstnCdNm13', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm13 = models.CharField(db_column='mgrNm13', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu13 = models.CharField(max_length=100, blank=True, null=True)
    crr13 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm14 = models.CharField(db_column='pstnCdNm14', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm14 = models.CharField(db_column='mgrNm14', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu14 = models.CharField(max_length=100, blank=True, null=True)
    crr14 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm15 = models.CharField(db_column='pstnCdNm15', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm15 = models.CharField(db_column='mgrNm15', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu15 = models.CharField(max_length=100, blank=True, null=True)
    crr15 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm16 = models.CharField(db_column='pstnCdNm16', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm16 = models.CharField(db_column='mgrNm16', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu16 = models.CharField(max_length=100, blank=True, null=True)
    crr16 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm17 = models.CharField(db_column='pstnCdNm17', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm17 = models.CharField(db_column='mgrNm17', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu17 = models.CharField(max_length=100, blank=True, null=True)
    crr17 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm18 = models.CharField(db_column='pstnCdNm18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm18 = models.CharField(db_column='mgrNm18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu18 = models.CharField(max_length=100, blank=True, null=True)
    crr18 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm19 = models.CharField(db_column='pstnCdNm19', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm19 = models.CharField(db_column='mgrNm19', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu19 = models.CharField(max_length=100, blank=True, null=True)
    crr19 = models.CharField(max_length=100, blank=True, null=True)
    pstncdnm20 = models.CharField(db_column='pstnCdNm20', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mgrnm20 = models.CharField(db_column='mgrNm20', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu20 = models.CharField(max_length=100, blank=True, null=True)
    crr20 = models.CharField(max_length=100, blank=True, null=True)
    stkrnm1 = models.CharField(db_column='stkrNm1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    note1 = models.CharField(max_length=100, blank=True, null=True)
    ownrate1 = models.CharField(db_column='ownRate1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stkrnm2 = models.CharField(db_column='stkrNm2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    note2 = models.CharField(max_length=100, blank=True, null=True)
    ownrate2 = models.CharField(db_column='ownRate2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stkrnm3 = models.CharField(db_column='stkrNm3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    note3 = models.CharField(max_length=100, blank=True, null=True)
    ownrate3 = models.CharField(db_column='ownRate3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stkrnm4 = models.CharField(db_column='stkrNm4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    note4 = models.CharField(max_length=100, blank=True, null=True)
    ownrate4 = models.CharField(db_column='ownRate4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stkrnm5 = models.CharField(db_column='stkrNm5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    note5 = models.CharField(max_length=100, blank=True, null=True)
    ownrate5 = models.CharField(db_column='ownRate5', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cmp_info'