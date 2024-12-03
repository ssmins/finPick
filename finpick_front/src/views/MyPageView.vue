<script setup>
import { useCounterStore } from "@/stores/counter";
import { onMounted, computed } from "vue";

// store에서 사용자 정보 가져오기
const store = useCounterStore();
const user = computed(() => store.user);

// 연봉 변환 함수
const formattedSalary = computed(() => {
  const salaryRanges = {
    "<3000": "3천만원 이하",
    "3000-5000": "3천만원 이상 5천만원 이하",
    "5000-10000": "5천만원 이상 1억원 이하",
    ">10000": "1억원 이상",
  };
  return salaryRanges[user.value.salary] || "알 수 없음";
});

// 예금 한도액 변환 함수
const formattedDepositAmount = computed(() => {
  const depositRanges = {
    "0-500": "500만원 이하",
    "500-1000": "500만원 이상 1천만원 이하",
    "1000-5000": "1천만원 이상 5천만원 이하",
    ">5000": "5천만원 이상",
  };
  return depositRanges[user.value.depositAmount] || "알 수 없음";
});

// 예치 기간 변환 함수
const formattedDepositPeriod = computed(() => {
  const periodRanges = {
    6: "6개월 미만",
    12: "6개월 이상 1년 미만",
    24: "1년 이상 2년 미만",
    36: "2년 이상",
  };
  return periodRanges[user.value.depositPeriod] || "알 수 없음";
});

// 적금 한도액 변환 함수
const formattedSavingsAmount = computed(() => {
  const savingsRanges = {
    "0-500": "50만원 미만",
    "500-1000": "50만원 이상 100만원 미만",
    "1000-5000": "100만원 이상 300만원 미만",
    ">5000": "300만원 이상",
  };
  return savingsRanges[user.value.savingsAmount] || "알 수 없음";
});

// 적금 납부 기간 변환 함수
const formattedSavingsPeriod = computed(() => {
  const savingsPeriodRanges = {
    6: "6개월 미만",
    12: "6개월 이상 1년 미만",
    24: "1년 이상 2년 미만",
    36: "2년 이상",
  };
  return savingsPeriodRanges[user.value.savingsPeriod] || "알 수 없음";
});
</script>

<template>
  <div class="mypage">
    <div class="container">
      <img
        :src="user.profileImage || '/images/profile_yuju.png'"
        alt="profile image"
        class="profile-image"
      />
      <!-- <h2 class="title">마이 페이지</h2> -->
      <div class="section">
        <p>
          <span class="nickname">{{ user.nickname }}</span> 님, 반갑습니다!
        </p>
      </div>

      <div class="section">
        <div class="info-section">
          <p>기본 정보</p>
          <button class="edit-button">수정하기</button>
        </div>
        <table class="info-table">
          <tbody>
            <tr>
              <td>나이</td>
              <td>{{ user.age }}세</td>
            </tr>
            <tr>
              <td>이메일</td>
              <td>{{ user.email }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="section">
        <div class="info-section">
          <p>금융 정보</p>
          <button class="edit-button">수정하기</button>
        </div>
        <table class="info-table">
          <tbody>
            <tr>
              <td>현재 연봉</td>
              <td>{{ formattedSalary }}</td>
            </tr>
            <tr>
              <td>예금 희망 금액</td>
              <td>{{ formattedDepositAmount }}</td>
            </tr>
            <tr>
              <td>예금 희망 기간</td>
              <td>{{ formattedDepositPeriod }}</td>
            </tr>
            <tr>
              <td>월 적금 희망 금액</td>
              <td>{{ formattedSavingsAmount }}</td>
            </tr>
            <tr>
              <td>적금 희망 기간</td>
              <td>{{ formattedSavingsPeriod }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- <RouterLink @click.prevent="store.logOut" :to="{ name : 'HomeView' }" class="logout-link"> 로그아웃하기 </RouterLink> -->
      <RouterLink
        @click.prevent="store.logOut"
        :to="{ name: 'HomeView' }"
        class="logout-button"
      >
        로그아웃
      </RouterLink>
    </div>
  </div>
</template>

<style scoped>
.mypage {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 62px;
}

.container {
  background-color: var(--color-background-soft);
  padding: 2rem;
  border-radius: 8px;
  width: 600px;
  margin: 62px auto;
  box-shadow: 0 0px 8px rgba(0, 0.2, 0.2, 0.3);
}

.title {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--color-heading);
  text-align: center;
  margin-bottom: 1.5rem;
}

.button,
input[type="submit"] {
  display: inline-block;
  padding: 10px 20px;
  background-color: var(--color-primary);
  color: #ffffff;
  text-align: center;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  font-size: 1rem;
  margin: 10px 0;
}

.button:hover,
input[type="submit"]:hover {
  background-color: var(--color-primary-hover);
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: var(--color-heading);
}

input[type="text"],
input[type="password"],
select {
  width: 100%;
  padding: 10px;
  border: 2px solid var(--color-border);
  border-radius: 4px;
  font-size: 1rem;
  color: var(--color-text);
  background-color: white;
}

p,
h2 {
  margin: 10px 0;
  font-size: 1rem;
  color: var(--color-text);
}
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.title {
  font-size: 24px;
  margin-bottom: 20px;
}

.section {
  background-color: var(--color-background-section);
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 8px;
}

.section p {
  font-size: 1.5rem; /* 글씨 크기를 1.5rem으로 설정 */
  font-weight: bold; /* 글씨를 굵게 설정 */
  text-align: center; /* 텍스트를 중앙 정렬 */
  margin-top: 1rem; /* 위쪽 여백 추가 */
}

.nickname {
  color: #2e3d86; /* 닉네임 색상을 파란색으로 변경 */
  font-weight: bold; /* 굵게 설정 (선택 사항) */
}

.info-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
  margin-bottom: 10px;
}

.edit-button {
  padding: 8px 16px;
  font-size: 14px;
  background-color: #4287f7;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s, transform 0.2s;
}

.edit-button:hover {
  background-color: #3366cc;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.edit-button:active {
  background-color: #004494;
  transform: translateY(0);
}

.logout-button {
  display: inline-block; /* 버튼으로 동작하게 설정 */
  padding: 8px 16px; /* 내부 여백 */
  font-size: 14px; /* 글씨 크기 */
  background-color: #787878; /* 로그아웃 버튼 배경 색상 */
  color: white; /* 글자색 흰색 */
  border: none; /* 테두리 제거 */
  border-radius: 5px; /* 모서리 둥글게 */
  cursor: pointer; /* 마우스 커서 변경 */
  text-align: center; /* 텍스트 가운데 정렬 */
  transition: background-color 0.3s, box-shadow 0.3s, transform 0.2s; /* 전환 효과 */
  margin-top: 1rem; /* 간격 추가 */
  text-decoration: none; /* 링크 스타일 제거 */
  margin-bottom: 20px;
}

.logout-button:hover {
  background-color: black; /* 호버 시 배경 색상 변경 (더 어두운 빨간색) */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 호버 시 그림자 추가 */
  transform: translateY(-2px); /* 살짝 위로 올라가게 */
}

.logout-button:active {
  background-color: black; /* 클릭 시 배경 색상 (더 진한 빨간색) */
  transform: translateY(0); /* 클릭 시 원래 위치로 돌아가게 */
}


.profile-image {
  width: 250px; /* 원형 이미지의 크기 설정 */
  height: 250px; /* 원형 이미지의 크기 설정 */
  object-fit: cover; /* 이미지 비율에 맞게 잘라내기 */
  border-radius: 50%; /* 이미지를 동그랗게 만들기 */
  border: 2px solid #ccc; /* 원형 이미지에 테두리 추가 (선택 사항) */
  display: block;
  margin: 30px auto;
}

/* 테이블 스타일 */
.info-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
  text-align: left;
}

.info-table tbody tr {
  border-bottom: 1px solid #ddd;
  text-align: left;
}

.info-table td {
  padding: 10px 15px;
  font-size: 1rem;
  color: var(--color-text);
}

.info-table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.info-table tr:hover {
  background-color: #f1f1f1;
}

.info-table td:first-child {
  font-weight: bold;
  color: var(--color-heading);
  width: 40%; /* 첫 번째 컬럼 너비 조정 */
}

.info-table td:last-child {
  text-align: left;
  color: #555;
}
</style>
