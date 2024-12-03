from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Exchange
from .serializers import ExchangeSerializer
from datetime import datetime
import requests
import urllib3

# 오늘 날짜를 YYYYMMDD 형식으로 가져오기
# today_date = datetime.now().strftime("%Y%m%d")  # YYYYMMDD 형식

# 환율 API URL 설정
# EXCHANGE_API_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={settings.EXCHANGE_API_KEY}&searchdate={today_date}&data=AP01'
EXCHANGE_API_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={settings.EXCHANGE_API_KEY}&searchdate=20241122&data=AP01'

# urllib3 인증서 경고 무시 (테스트 환경에서만 사용)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@api_view(['GET'])
def index(request):
    """
    환율 데이터를 가져와 DB에 저장하거나 업데이트한 뒤 반환합니다.
    """
    try:
        response = requests.get(EXCHANGE_API_URL, verify=False)
        response.raise_for_status()
        response_data = response.json()

        print(response_data)
    except requests.exceptions.RequestException as e:
        return Response({'error': 'Failed to fetch exchange data', 'details': str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    if response_data:
        for data in response_data:
            Exchange.objects.update_or_create(
                cur_unit=data['cur_unit'],  # 통화 단위를 기준으로 업데이트 또는 생성
                defaults={
                    'cur_nm': data.get('cur_nm', ''),
                    'ttb': data.get('ttb', ''),
                    'tts': data.get('tts', ''),
                    'deal_bas_r': data.get('deal_bas_r', ''),
                    'bkpr': data.get('bkpr', ''),
                    'yy_efee_r': data.get('yy_efee_r', ''),
                    'ten_dd_efee_r': data.get('ten_dd_efee_r', ''),
                    'kftc_deal_bas_r': data.get('kftc_deal_bas_r', ''),
                    'kftc_bkpr': data.get('kftc_bkpr', ''),
                }
            )
    exchange_data = Exchange.objects.all()
    serializer = ExchangeSerializer(exchange_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def calculate_exchange(request):
    """
    특정 금액을 환율에 따라 변환합니다.
    """
    try:
        source_currency = request.data.get('source_currency')  # 원래 통화
        target_currency = request.data.get('target_currency')  # 변환하려는 통화
        amount = float(request.data.get('amount', 0))  # 변환할 금액

        if source_currency == 'KRW':  # 원화를 다른 통화로 변환
            target_rate = Exchange.objects.get(cur_unit=target_currency).tts
            converted_amount = amount / float(target_rate.replace(',', ''))
        elif target_currency == 'KRW':  # 다른 통화를 원화로 변환
            source_rate = Exchange.objects.get(cur_unit=source_currency).ttb
            converted_amount = amount * float(source_rate.replace(',', ''))
        else:  # 두 통화 간 직접 변환
            source_rate = Exchange.objects.get(cur_unit=source_currency).deal_bas_r
            target_rate = Exchange.objects.get(cur_unit=target_currency).deal_bas_r
            converted_amount = (amount * float(source_rate.replace(',', ''))) / float(target_rate.replace(',', ''))

        return Response({
            'source_currency': source_currency,
            'target_currency': target_currency,
            'original_amount': amount,
            'converted_amount': round(converted_amount, 2),
        })
    except Exchange.DoesNotExist:
        return Response({'error': 'Currency not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
