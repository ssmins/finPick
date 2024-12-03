from django.urls import path
from .views import get_articles

urlpatterns = [
    path('get-articles/', get_articles, name='get_articles'),
]
