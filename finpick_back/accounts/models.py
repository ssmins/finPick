from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    nickname = models.CharField(blank=True, null=True, max_length=100) 
    age = models.PositiveIntegerField(blank=True, null=True)  # 나이
    salary = models.CharField(blank=True, null=True, max_length=20)  # 현재 연봉
    depositAmount = models.CharField(blank=True, null=True, max_length=20)  # 예금 희망 금액
    depositPeriod = models.CharField(blank=True, null=True, max_length=20)  # 예금 희망 기간
    savingsAmount = models.CharField(blank=True, null=True, max_length=20)  # 적금 희망 금액
    savingsPeriod = models.CharField(blank=True, null=True, max_length=20)  # 적금 납입 희망 기간
