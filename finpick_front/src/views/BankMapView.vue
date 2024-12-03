<script setup>
import { useMapStore } from "@/stores/map";
import axios from "axios";
import { computed, onMounted, ref, watch } from "vue";

/* ------------- 검색 ------------- */

// 상태 관리 스토어 사용
const store = useMapStore();

// 사용자 입력 데이터 (반응형 변수)
const city = ref("");
const district = ref("");
const neighborhood = ref("");
const keyword = ref("은행");

// 시도 리스트
const cities = [
  "서울특별시",
  "부산광역시",
  "대구광역시",
  "인천광역시",
  "광주광역시",
  "대전광역시",
  "울산광역시",
  "세종특별자치시",
  "경기도",
  "강원도",
  "충청북도",
  "충청남도",
  "전라북도",
  "전라남도",
  "경상북도",
  "경상남도",
  "제주특별자치도",
];

// 구 리스트 (각 시도에 해당하는 구를 설정)
const districts = ref([]);

const districtData = {
  서울특별시: [
    "강남구",
    "강동구",
    "강북구",
    "강서구",
    "관악구",
    "광진구",
    "구로구",
    "금천구",
    "노원구",
    "도봉구",
    "동대문구",
    "동작구",
    "마포구",
    "서대문구",
    "서초구",
    "성동구",
    "성북구",
    "송파구",
    "양천구",
    "영등포구",
    "용산구",
    "은평구",
    "종로구",
    "중구",
    "중랑구",
  ],
  부산광역시: [
    "강서구",
    "금정구",
    "기장군",
    "남구",
    "동구",
    "동래구",
    "부산진구",
    "북구",
    "사상구",
    "사하구",
    "서구",
    "수영구",
    "연제구",
    "영도구",
    "중구",
    "해운대구",
  ],
  대구광역시: [
    "남구",
    "달서구",
    "달성군",
    "동구",
    "북구",
    "서구",
    "수성구",
    "중구",
  ],
  인천광역시: [
    "강화군",
    "계양구",
    "남동구",
    "동구",
    "미추홀구",
    "부평구",
    "서구",
    "연수구",
    "옹진군",
    "중구",
  ],
  광주광역시: ["광산구", "남구", "동구", "북구", "서구"],
  대전광역시: ["대덕구", "동구", "서구", "유성구", "중구"],
  울산광역시: ["남구", "동구", "북구", "울주군", "중구"],
  세종특별자치시: ["세종시"],
  경기도: [
    "가평군",
    "고양시",
    "과천시",
    "광명시",
    "광주시",
    "구리시",
    "군포시",
    "김포시",
    "남양주시",
    "동두천시",
    "부천시",
    "성남시",
    "수원시",
    "시흥시",
    "안산시",
    "안성시",
    "안양시",
    "양주시",
    "양평군",
    "여주시",
    "연천군",
    "오산시",
    "용인시",
    "의왕시",
    "의정부시",
    "이천시",
    "파주시",
    "평택시",
    "포천시",
    "하남시",
    "화성시",
  ],
  강원도: [
    "강릉시",
    "고성군",
    "동해시",
    "삼척시",
    "속초시",
    "양구군",
    "양양군",
    "영월군",
    "원주시",
    "인제군",
    "정선군",
    "철원군",
    "춘천시",
    "태백시",
    "평창군",
    "홍천군",
    "화천군",
    "횡성군",
  ],
  충청북도: [
    "괴산군",
    "단양군",
    "보은군",
    "영동군",
    "옥천군",
    "음성군",
    "제천시",
    "증평군",
    "진천군",
    "청주시",
    "충주시",
  ],
  충청남도: [
    "계룡시",
    "공주시",
    "금산군",
    "논산시",
    "당진시",
    "보령시",
    "부여군",
    "서산시",
    "서천군",
    "아산시",
    "예산군",
    "천안시",
    "청양군",
    "태안군",
    "홍성군",
  ],
  전라북도: [
    "고창군",
    "군산시",
    "김제시",
    "남원시",
    "무주군",
    "부안군",
    "순창군",
    "완주군",
    "익산시",
    "임실군",
    "장수군",
    "전주시",
    "정읍시",
    "진안군",
  ],
  전라남도: [
    "강진군",
    "고흥군",
    "곡성군",
    "광양시",
    "구례군",
    "나주시",
    "담양군",
    "목포시",
    "무안군",
    "보성군",
    "순천시",
    "신안군",
    "여수시",
    "영광군",
    "영암군",
    "완도군",
    "장성군",
    "장흥군",
    "진도군",
    "함평군",
    "해남군",
    "화순군",
  ],
  경상북도: [
    "경산시",
    "경주시",
    "고령군",
    "구미시",
    "군위군",
    "김천시",
    "문경시",
    "봉화군",
    "상주시",
    "성주군",
    "안동시",
    "영덕군",
    "영양군",
    "영주시",
    "영천시",
    "예천군",
    "울릉군",
    "울진군",
    "의성군",
    "청도군",
    "청송군",
    "칠곡군",
    "포항시",
  ],
  경상남도: [
    "거제시",
    "거창군",
    "고성군",
    "김해시",
    "남해군",
    "밀양시",
    "사천시",
    "산청군",
    "양산시",
    "의령군",
    "진주시",
    "창녕군",
    "창원시",
    "통영시",
    "하동군",
    "함안군",
    "함양군",
    "합천군",
  ],
  제주특별자치도: ["서귀포시", "제주시"],
};

// 시도 변경 시 구 목록 업데이트
const updateDistricts = () => {
  districts.value = districtData[city.value] || [];
  district.value = ""; // 구 선택 초기화
};

// 검색 함수
const handleSearch = function () {
  const params = {
    city: city.value,
    district: district.value,
    neighborhood: neighborhood.value,
    keyword: keyword.value,
  };
  store.getBanksMap(params); // 서버 요청
  findDatas(city.value, district.value, neighborhood.value, keyword.value); // API 호출 확인
};

/* ------------- 검색 ------------- */

/* ------------- 지도 ------------- */

// // Kakao API 키 (환경 변수 또는 설정에서 가져오기)
const KAKAO_JAVASCRIPT_KEY = import.meta.env.VITE_KAKAO_JAVASCRIPT_KEY;
const API_KEY = import.meta.env.VITE_KAKAO_JAVASCRIPT_KEY
// const API_KEY = "f8e029cac81f6326a04eb13f32714408";

// 지도 관련 변수
// const mapContainer = ref(null) // Kakao Map 객체
// // const mapContainer = document.querySelector('#mapContainer') // Kakao Map 객체
// const map = ref(null);
// const markerInfo = ref(null);
// const markers = ref([]);
// const lat = ref(37.566826);
// const lng = ref(126.9786567);
// const API_KEY = import.meta.env.VITE_KAKAO_JAVASCRIPT_KEY;

const lat = ref(37.5173319258532);
const lng = ref(127.047377408384);
const mapContainer = ref(null); // Kakao Map 객체
const map = ref(null);
const markerInfo = ref(null);
const markers = ref([]);
// const API_KEY = import.meta.env.VITE_KAKAO_JAVASCRIPT_KEY;

const loadKakaoMap = (container) => {
  const script = document.createElement("script");
  script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${API_KEY}&autoload=false`;
  document.head.appendChild(script);
  script.onload = () => {
    window.kakao.maps.load(() => {
      const options = {
        center: new window.kakao.maps.LatLng(lat.value, lng.value),
        level: 3,
      };
      map.value = new window.kakao.maps.Map(container, options);
    });
  };
};

onMounted(() => {
  loadKakaoMap(mapContainer.value);
});

const updateMapCenter = (newLat, newLng) => {
  if (map.value) {
    const newCenter = new window.kakao.maps.LatLng(newLat, newLng);
    // console.log('updateMapCenter : ', map.value)
    map.value.setCenter(newCenter);
    // console.log('updateMapCenter : ', map.value)
  }
};

const API_BASE_URL = "http://127.0.0.1:8000";

const findDatas = (city, district, neighborhood, keyword) => {
  axios
    .get(
      `${API_BASE_URL}/bankmaps/search-banks/?city=${city}&district=${district}&neighborhood=${neighborhood}&keyword=${keyword}`
    )
    .then((res) => {
      console.log("여기! ");
      console.log(res);
      lat.value = res.data.documents[0].y;
      lng.value = res.data.documents[0].x; // value를 변동시켜 지도 이동 !
      markerInfo.value = res.data.documents;
      console.log("markerInfo : ", markerInfo.value);
      updateMapMaker(markerInfo);
    })
    .catch((error) => {
      console.error("Error fetching lat/lng:", error);
    });
};

const updateMapMaker = (markerInfo) => {
  console.log("markers.value : ", markers.value);
  console.log("updateMarker 함수가 실행되었습니다.");
  markers.value.forEach((marker) => marker.setMap(null)); // 기존 마커 제거
  markers.value = [];
  console.log("markers.value : ", markers.value);

  const imageSrc = "/images/location.png";
  const imageSize = new window.kakao.maps.Size(32, 32);

  markerInfo.value.forEach((element) => {
    // 여기에서 markerInfo는 markerInfo.value로 변경해야 할 부분
    if (
      !element.place_name ||
      element.place_name.includes("ATM") ||
      element.place_name.includes("무인") ||
      element.place_name.includes("365")
    ) {
      return;
    }
    console.log("element : ", element);
    const position = {
      title: element.place_name,
      latlng: new window.kakao.maps.LatLng(element.y, element.x),
    };
    console.log("position : ", position);
    const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
    console.log("markerImage : ", markerImage);
    console.log("map : ", map.value);
    console.log("position : ", position);
    const marker = new kakao.maps.Marker({
      // 지도 상에 표시될 마커를 생성하는 데 사용
      map: map.value,
      position: position.latlng,
      title: position.title,
      image: markerImage,
    });
    markers.value.push(marker); // **새로운 마커를 배열에 추가**
    console.log("markers.value : ", markers.value);
  });
};

// lat, lng 값 변경 감지 및 지도 업데이트
watch([lat, lng], ([newLat, newLng]) => {
  updateMapCenter(newLat, newLng);
});

/* ------------- 지도 ------------- */
</script>

<template>
  <div class="bankmap">
    <h2 class="title">주변 은행 검색</h2>
    <div class="content-wrapper">
      <div class="filter-section">
        <form @submit.prevent="handleSearch">
          <div>
            <label for="city">광역시/도</label>
            <select v-model="city" id="city" @change="updateDistricts" required>
              <option v-for="city in cities" :key="city" :value="city">
                {{ city }}
              </option>
            </select>
          </div>
          <div>
            <label for="district">시/군/구</label>
            <select v-model="district" id="district" required>
              <option v-for="d in districts" :key="d" :value="d">
                {{ d }}
              </option>
            </select>
          </div>
          <div>
            <label for="neighborhood">읍/면/동/리</label>
            <input type="text" v-model="neighborhood" id="neighborhood" />
          </div>
          <div>
            <label for="keyword">은행 검색</label>
            <input type="text" v-model="keyword" id="keyword" />
          </div>
          <button type="submit">검색</button>
        </form>
      </div>

      <div id="map" ref="mapContainer"></div>
    </div>
  </div>
</template>

<style scoped>
.bankmap {
  padding: 32px;
}

.title {
  padding: 20px 0px;
  font-size: 1.5rem;
  font-weight: 600;
  text-decoration: none;
}

.content-wrapper {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}

.filter-section {
  width: 40%;
  height: 500px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 1rem;
  background-color: var(--color-background-soft);
  border-radius: 10px;
  box-shadow: 0 0px 8px rgba(0, 0.2, 0.2, 0.3);
  gap: 15px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 24px;
  width: 100%;
}

form div {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

label {
  font-size: 1rem;
  color: #333;
  margin-bottom: 8px;
}

input,
select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #fff;
  font-size: 1rem;
  color: #333;
  outline: none;
  transition: border-color 0.3s;
  width: 100%;
  box-sizing: border-box;
}

input:focus,
select:focus {
  border-color: #4287f7;
}

button {
  padding: 8px 16px;
  margin-top: 8px;
  font-size: 1rem;
  background-color: #4287f7;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s, transform 0.2s;
  width: 100%;
}

button:hover {
  background-color: #4287f7;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

button:active {
  background-color: #004494;
  transform: translateY(0);
}

#map {
  width: 60%;
  height: 500px;
  border-radius: 10px;
  box-shadow: 0 0px 8px rgba(0, 0.2, 0.2, 0.3);
}
</style>
