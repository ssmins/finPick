from django.urls import path
from .views import BankSearchAPIView

urlpatterns = [
    path('search-banks/', BankSearchAPIView.as_view(), name='bank_search'),
]