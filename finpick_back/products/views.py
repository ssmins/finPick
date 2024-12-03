from django.shortcuts import get_list_or_404, get_object_or_404
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Deposit, DepositOptions, Saving, SavingOptions
from .serializers import DepositSerializer, DepositOptionsSerializer, SavingSerializer, SavingOptionsSerializer
from django.conf import settings
from articles.models import Article  # Article 모델 임포트
from django.contrib.auth import get_user_model

User = get_user_model()

# 예금 적금 API 호출 저장
@api_view(['GET'])
def save_deposit_products(request):
    DEPOSIT_API_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={settings.API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(DEPOSIT_API_URL)

    # 응답 상태 코드가 200 OK인지 확인
    if response.status_code != 200:
        return Response({"error": "API 요청 실패"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    result = response.json().get('result')

    # result가 없는 경우 처리
    if not result:
        return Response({"error": "API 응답에서 'result'를 찾을 수 없음"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    base_list = result.get('baseList')
    option_list = result.get('optionList')

    # baseList가 없거나 빈 경우 처리
    if not base_list:
        return Response({"error": "'baseList'가 비어있거나 존재하지 않음"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    admin_user = User.objects.filter(is_superuser=True).first()
    if not admin_user:
        return Response({"error": "관리자 계정이 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)

    deposit_created_count = 0
    for data_list in base_list:
        if not Deposit.objects.filter(fin_prdt_cd=data_list['fin_prdt_cd']).exists():
            deposit = Deposit.objects.create(
                fin_prdt_cd=data_list['fin_prdt_cd'],
                dcls_month=data_list['dcls_month'],
                kor_co_nm=data_list['kor_co_nm'],
                fin_prdt_nm=data_list['fin_prdt_nm'],
                etc_note=data_list['etc_note'],
                join_deny=data_list['join_deny'],
                join_member=data_list['join_member'],
                join_way=data_list['join_way'],
                spcl_cnd=data_list['spcl_cnd'],
                max_limit=data_list['max_limit'],
            )
            deposit_created_count += 1

            # 게시글 생성
            Article.objects.create(
                user=admin_user,
                title=f"{deposit.fin_prdt_nm} 상품 안내",
                content=f"{deposit.kor_co_nm}의 {deposit.fin_prdt_nm} 상품에 대한 설명입니다.",
                fin_prdt_cd=deposit.fin_prdt_cd,
                dcls_month=deposit.dcls_month,
                fin_prdt_nm=deposit.fin_prdt_nm,
                kor_co_nm=deposit.kor_co_nm,
                join_way=deposit.join_way,
                spcl_cnd=deposit.spcl_cnd,
                join_deny=deposit.join_deny,
                join_member=deposit.join_member,
                etc_note=deposit.etc_note,
                max_limit=deposit.max_limit,
            )

    # optionList가 없는 경우 처리
    if not option_list:
        return Response({"error": "'optionList'가 비어있거나 존재하지 않음"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    for data_list in option_list:
        # 중복 조건 확인
        is_duplicate = DepositOptions.objects.filter(
            product__fin_prdt_cd=data_list['fin_prdt_cd'],
            intr_rate=data_list.get('intr_rate', -1),
            intr_rate2=data_list.get('intr_rate2', -1),
            save_trm=data_list['save_trm'],
            intr_rate_type_nm=data_list['intr_rate_type_nm']
        ).exists()

        if not is_duplicate:
            deposit_product = Deposit.objects.get(fin_prdt_cd=data_list['fin_prdt_cd'])
            intr_rate_value = data_list.get('intr_rate') if data_list.get('intr_rate') is not None else -1
            intr_rate2_value = data_list.get('intr_rate2') if data_list.get('intr_rate2') is not None else -1

            DepositOptions.objects.create(
                product=deposit_product,
                fin_prdt_cd=data_list['fin_prdt_cd'],
                intr_rate_type_nm=data_list['intr_rate_type_nm'],
                intr_rate=intr_rate_value,
                intr_rate2=intr_rate2_value,
                save_trm=data_list['save_trm'],
            )

    return Response({
        "message": "Deposit products and articles saved successfully.",
        "deposits_created": deposit_created_count
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def save_saving_products(request):
    SAVING_API_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={settings.API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(SAVING_API_URL)

    # 응답 상태 코드가 200 OK인지 확인
    if response.status_code != 200:
        return Response({"error": "API 요청 실패"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    result = response.json().get('result')

    # result가 없는 경우 처리
    if not result:
        return Response({"error": "API 응답에서 'result'를 찾을 수 없음"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    base_list = result.get('baseList')
    option_list = result.get('optionList')

    # baseList가 없거나 빈 경우 처리
    if not base_list:
        return Response({"error": "'baseList'가 비어있거나 존재하지 않음"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    admin_user = User.objects.filter(is_superuser=True).first()
    if not admin_user:
        return Response({"error": "관리자 계정이 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)

    saving_created_count = 0
    for data_list in base_list:
        if not Saving.objects.filter(fin_prdt_cd=data_list['fin_prdt_cd']).exists():
            saving = Saving.objects.create(
                fin_prdt_cd=data_list['fin_prdt_cd'],
                dcls_month=data_list['dcls_month'],
                kor_co_nm=data_list['kor_co_nm'],
                fin_prdt_nm=data_list['fin_prdt_nm'],
                etc_note=data_list['etc_note'],
                join_deny=data_list['join_deny'],
                join_member=data_list['join_member'],
                join_way=data_list['join_way'],
                spcl_cnd=data_list['spcl_cnd'],
                max_limit=data_list['max_limit'],
            )
            saving_created_count += 1

            # 게시글 생성
            Article.objects.create(
                user=admin_user,
                title=f"{saving.fin_prdt_nm} 상품 안내",
                content=f"{saving.kor_co_nm}의 {saving.fin_prdt_nm} 상품에 대한 설명입니다.",
                fin_prdt_cd=saving.fin_prdt_cd,
                dcls_month=saving.dcls_month,
                fin_prdt_nm=saving.fin_prdt_nm,
                kor_co_nm=saving.kor_co_nm,
                join_way=saving.join_way,
                spcl_cnd=saving.spcl_cnd,
                join_deny=saving.join_deny,
                join_member=saving.join_member,
                etc_note=saving.etc_note,
                max_limit=saving.max_limit,
            )

    # optionList가 없는 경우 처리
    if not option_list:
        return Response({"error": "'optionList'가 비어있거나 존재하지 않음"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    for data_list in option_list:
        # 중복 조건 확인
        is_duplicate = SavingOptions.objects.filter(
            product__fin_prdt_cd=data_list['fin_prdt_cd'],
            intr_rate_type_nm=data_list['intr_rate_type_nm'],
            rsrv_type_nm=data_list['rsrv_type_nm'],
            intr_rate=data_list.get('intr_rate', -1),
            intr_rate2=data_list.get('intr_rate2', -1),
            save_trm=data_list['save_trm'],
        ).exists()

        if not is_duplicate:
            saving_product = Saving.objects.get(fin_prdt_cd=data_list['fin_prdt_cd'])
            intr_rate_value = data_list.get('intr_rate') if data_list.get('intr_rate') is not None else -1
            intr_rate2_value = data_list.get('intr_rate2') if data_list.get('intr_rate2') is not None else -1

            SavingOptions.objects.create(
                product=saving_product,
                fin_prdt_cd=data_list['fin_prdt_cd'],
                intr_rate_type_nm=data_list['intr_rate_type_nm'],
                rsrv_type_nm=data_list['rsrv_type_nm'],
                intr_rate=intr_rate_value,
                intr_rate2=intr_rate2_value,
                save_trm=data_list['save_trm'],
            )

    return Response({
        "message": "Saving products and articles saved successfully.",
        "savings_created": saving_created_count
    }, status=status.HTTP_201_CREATED)

# 예금 상품 조회 및 필터링 (은행명별 필터링 추가)
@api_view(['GET'])
def deposit_products(request):
    # 은행명을 필터로 받음
    bank_name = request.query_params.get('bank', None)  

    # 기본 QuerySet
    deposit_products = Deposit.objects.all()

    # 은행명을 기준으로 필터링
    if bank_name:
        deposit_products = deposit_products.filter(kor_co_nm=bank_name)

    # 상품 목록 직렬화
    data = []
    for product in deposit_products:
        options = DepositOptions.objects.filter(product=product)

        # 가입 기간별로 데이터 분류
        terms_data = {}
        for option in options:
            if option.save_trm == 6:
                terms_data["6개월"] = {
                    "intr_rate": option.intr_rate
                }
            elif option.save_trm == 12:
                terms_data["12개월"] = {
                    "intr_rate": option.intr_rate
                }
            elif option.save_trm == 24:
                terms_data["24개월"] = {
                    "intr_rate": option.intr_rate
                }
            elif option.save_trm == 36:
                terms_data["36개월"] = {
                    "intr_rate": option.intr_rate
                }

        if terms_data:
            product_data = {
                "dcls_month": product.dcls_month,
                "kor_co_nm": product.kor_co_nm,
                "fin_prdt_nm": product.fin_prdt_nm,
                "terms": terms_data,  
                "join_way": product.join_way,
                "spcl_cnd": product.spcl_cnd,
                "join_deny": product.join_deny,
                "join_member": product.join_member,
                "max_limit": product.max_limit,
                "etc_note": product.etc_note,
            }
            data.append(product_data)

    return Response(data, status=status.HTTP_200_OK)


# 금리 비교
# 적금 상품 조회 및 필터링 (은행명별 필터링 추가)
@api_view(['GET'])
def saving_products(request):
    # 은행명을 필터로 받음
    bank_name = request.query_params.get('bank', None)  

    # 기본 QuerySet
    saving_products = Saving.objects.all()

    # 은행명을 기준으로 필터링
    if bank_name:
        saving_products = saving_products.filter(kor_co_nm=bank_name)

    # 상품 목록 직렬화
    data = []
    for product in saving_products:
        options = SavingOptions.objects.filter(product=product)

        # 가입 기간별로 데이터 분류
        terms_data = {}
        for option in options:
            if option.save_trm == 6:
                terms_data["6개월"] = {
                    "intr_rate": option.intr_rate
                }
            elif option.save_trm == 12:
                terms_data["12개월"] = {
                    "intr_rate": option.intr_rate
                }
            elif option.save_trm == 24:
                terms_data["24개월"] = {
                    "intr_rate": option.intr_rate
                }
            elif option.save_trm == 36:
                terms_data["36개월"] = {
                    "intr_rate": option.intr_rate
                }

        if terms_data:
            product_data = {
                "dcls_month": product.dcls_month,
                "kor_co_nm": product.kor_co_nm,
                "fin_prdt_nm": product.fin_prdt_nm,
                "terms": terms_data,  
                "join_way": product.join_way,
                "spcl_cnd": product.spcl_cnd,
                "join_deny": product.join_deny,
                "join_member": product.join_member,
                "max_limit": product.max_limit,
                "etc_note": product.etc_note,
            }
            data.append(product_data)

    return Response(data, status=status.HTTP_200_OK)

# 은행 목록 조회 API 추가
@api_view(['GET'])
def get_bank_list(request):
    bank_list = Deposit.objects.values_list('kor_co_nm', flat=True).distinct()
    return Response(list(bank_list), status=status.HTTP_200_OK)
    
# 상세 조회
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd) : 
    data_list = DepositOptions.objects.filter(fin_prdt_cd = fin_prdt_cd)
    if request.method == 'GET' : 
        serializer = DepositOptionsSerializer(data_list, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def saving_product_options(request, fin_prdt_cd) : 
    data_list = SavingOptions.objects.filter(fin_prdt_cd = fin_prdt_cd)
    if request.method == 'GET' : 
        serializer = SavingOptionsSerializer(data_list, many=True)
        return Response(serializer.data)


def main(request) : 
    pass