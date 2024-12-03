from django.urls import path
from . import views

urlpatterns = [
    # 예금 상품 목록 DB에 저장
    path('save-deposit-products/', views.save_deposit_products),
    # 적금 상품 목록 DB에 저장
    path('save-saving-products/', views.save_saving_products),
    # 예금 상품 목록 출력
    path('deposit-products/', views.deposit_products),
    # 적금 상품 목록 출력
    path('saving-products/', views.saving_products),
    # 은행 목록 조회 API
    path('bank-list/', views.get_bank_list),  
    # 예금 상세 조회
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options),
    # 적금 상세 조회
    path('saving-product-options/<str:fin_prdt_cd>/', views.saving_product_options),
    #
    path('deposit_products/', views.deposit_products, name='deposit_products'),
    path('saving_products/', views.saving_products, name='saving_products'),
]