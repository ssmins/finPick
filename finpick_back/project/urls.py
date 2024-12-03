"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger 설정
schema_view = get_schema_view(
    openapi.Info(
        title="FINPICK API",  # API 이름
        default_version="v1",
        description="FINPICK API 문서입니다.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # 모든 사용자에게 공개
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('dj_rest_auth.urls')),
        # 로그인 요청 : [POST] /accounts/login/ 
        # 로그아웃 요청 : [POST] /accounts/logout/ 
        # 비밀번호 변경 요청 : [POST] /accounts/password/change/ 
        # 비밀번호 초기화 요청 [POST] /accounts/password/reset/
    path('accounts/registration/', include('dj_rest_auth.registration.urls')), 
        # 회원가입 요청 : [POST] /accounts/registration/
        # 이메일 인증 링크 확인 [POST] /accounts/registration/verify-email/ 
    path('products/', include('products.urls')),  # products
    path('articles/', include('articles.urls')),  # articles
    path('exchange/', include('exchange.urls')),  # exchange
    path('bankmaps/', include('bankmaps.urls')),  # bankmaps
    path('api/', include('products.urls')),

    # Swagger 경로 추가
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # 선택사항
]
