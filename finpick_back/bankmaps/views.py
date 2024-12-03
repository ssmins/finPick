from django.shortcuts import render
import requests
from decouple import config
from rest_framework.views import APIView
from rest_framework.response import Response

class BankSearchAPIView(APIView):
    def get(self, request):
        # 사용자로부터 입력받은 시(도), 구(시), 동
        city = request.query_params.get('city')
        district = request.query_params.get('district')
        neighborhood = request.query_params.get('neighborhood')  # 동
        keyword = request.query_params.get('keyword', '은행') # default : '은행' 

        if not city or not district or not neighborhood:
            return Response({"error": "시(도), 구(시), 동을 모두 입력해주세요."}, status=400)

        # 주소 -> 좌표 변환 (카카오 API 호출)
        geocode_url = "https://dapi.kakao.com/v2/local/search/address.json"
        geocode_headers = {"Authorization": f"KakaoAK {config('KAKAO_ADMIN_KEY')}"}
        geocode_params = {
            "query": f"{city} {district} {neighborhood}"
        }
        geocode_response = requests.get(geocode_url, headers=geocode_headers, params=geocode_params)
        print("Geocode Response Status Code:", geocode_response.status_code)
        print("Geocode Response Content:", geocode_response.text)  # 응답 본문 확인

        if geocode_response.status_code != 200:
            print("Geocode API Response:", geocode_response.json())
            return Response({"error": "좌표 변환에 실패했습니다."}, status=500)
        
        geocode_data = geocode_response.json()
        if not geocode_data.get('documents'):
            return Response({"error": "유효한 주소가 아닙니다."}, status=404)

        # 변환된 위도와 경도 추출
        lat = geocode_data['documents'][0]['y']
        lng = geocode_data['documents'][0]['x']

        # 은행 검색 (카카오 API 호출)
        search_url = "https://dapi.kakao.com/v2/local/search/keyword.json"
        search_headers = {"Authorization": f"KakaoAK {config('KAKAO_ADMIN_KEY')}"}
        search_params = {
            "y": lat,
            "x": lng,
            "radius": 5000,  # 검색 반경: 5km
            "query": keyword
        }
        search_response = requests.get(search_url, headers=search_headers, params=search_params)

        if search_response.status_code != 200:
            return Response({"error": "은행 검색에 실패했습니다."}, status=500)

        # 검색 결과 반환
        return Response(search_response.json())
