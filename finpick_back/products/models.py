from django.db import models

class Deposit(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융 상품코드
    dcls_month = models.CharField(max_length=20)  # 공시 제출월
    fin_prdt_nm = models.TextField() # 금융 상품명
    kor_co_nm = models.TextField() # 금융 회사명
    join_way = models.TextField() # 가입방법
    spcl_cnd = models.TextField() # 우대조건
    join_deny_choices = [
        (1, '제한없음'),
        (2, '서민전용'),
        (3, '일부제한')
    ]
    join_deny = models.IntegerField(choices=join_deny_choices) # 가입제한
    join_member = models.TextField() # 가입대상
    etc_note = models.TextField() # 기타 유의사항
    max_limit = models.BigIntegerField(blank=True, null=True)  # 최고 한도
    
class DepositOptions(models.Model): 
    product = models.ForeignKey( # 상품 
        Deposit,
        on_delete = models.CASCADE,
        to_field = 'id'
    )
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100) # 저축 금리 유형명 
    save_trm = models.IntegerField() # 저축 기간
    intr_rate = models.FloatField() # 저축 금리
    intr_rate2 = models.FloatField() # 최고 우대 금리

class Saving(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융 상품코드
    dcls_month = models.CharField(max_length=20)  # 공시 제출월
    fin_prdt_nm = models.TextField() # 금융 상품명
    kor_co_nm = models.TextField() # 금융 회사명
    join_way = models.TextField() # 가입방법
    spcl_cnd = models.TextField() # 우대조건
    join_deny_choices = [
        (1, '제한없음'),
        (2, '서민전용'),
        (3, '일부제한')
    ]
    join_deny = models.IntegerField(choices=join_deny_choices) # 가입제한
    join_member = models.TextField() # 가입대상
    etc_note = models.TextField() # 기타 유의사항
    max_limit = models.BigIntegerField(blank=True, null=True)  # 최고 한도
    
class SavingOptions(models.Model): 
    product = models.ForeignKey( # 상품 
        Saving,
        on_delete = models.CASCADE,
        to_field = 'id'
    )
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100) # 저축 금리 유형명 
    rsrv_type_nm = models.TextField() # 적립 유형명
    save_trm = models.IntegerField() # 저축 기간
    intr_rate = models.FloatField() # 저축 금리
    intr_rate2 = models.FloatField() # 최고 우대 금리