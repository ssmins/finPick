from django.db import models
from django.contrib.auth import get_user_model
from products.models import Deposit, Saving  

User = get_user_model()

# 게시글(Article) 모델
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    fin_prdt_cd = models.TextField(unique=True)  # 금융 상품코드
    dcls_month = models.CharField(max_length=20, blank=True, null=True)  # 공시 제출월
    fin_prdt_nm = models.TextField(blank=True, null=True)  # 금융 상품명
    kor_co_nm = models.TextField(blank=True, null=True)  # 금융 회사명
    join_way = models.TextField(blank=True, null=True)  # 가입방법
    spcl_cnd = models.TextField(blank=True, null=True)  # 우대조건
    join_deny_choices = [
        (1, '제한없음'),
        (2, '서민전용'),
        (3, '일부제한')
    ]
    join_deny = models.IntegerField(choices=join_deny_choices, blank=True, null=True)  # 가입 제한
    join_member = models.TextField(blank=True, null=True)  # 가입 대상
    etc_note = models.TextField(blank=True, null=True)  # 기타 유의사항
    max_limit = models.BigIntegerField(blank=True, null=True)  # 최고 한도

# 댓글(Comment) 모델
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
