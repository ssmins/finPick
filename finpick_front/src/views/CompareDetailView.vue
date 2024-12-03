<script setup>
import { useRouter } from "vue-router";

// 라우터 객체 가져오기
const router = useRouter();

// 부모 컴포넌트에서 전달된 상세 정보 prop
const props = defineProps({
  isVisible: Boolean,
  details: Object, // 상세 정보 데이터
});

// 부모 컴포넌트로 이벤트 전달
const emit = defineEmits(["close"]);

// 닫기 버튼 클릭 시 실행
const closeModal = () => {
  emit("close"); // 부모 컴포넌트에 'close' 이벤트 전달
};

// 가입하기 함수 (예: 특정 페이지로 이동)
const handleJoin = () => {
  alert("상품이 가입되었습니다."); // 원하는 동작 추가
};
</script>

<template>
  <div v-if="isVisible" class="modal-overlay">
    <div class="modal-content">
      <!-- 닫기 버튼 -->
      <button class="close-button" @click="closeModal">닫기</button>
      <!-- 상품명 -->
      <h2 class="modal-title">{{ details?.fin_prdt_nm || "금융 상품 정보" }}</h2>
      <!-- 상세 정보 테이블 -->
      <table>
        <tbody>
          <tr>
            <td>공시 제출월</td>
            <td>{{ details?.dcls_month || "-" }}</td>
          </tr>
          <tr>
            <td>금융회사명</td>
            <td>{{ details?.kor_co_nm || "-" }}</td>
          </tr>
          <tr>
            <td>금융상품명</td>
            <td>{{ details?.fin_prdt_nm || "-" }}</td>
          </tr>
          <tr>
            <td>가입방법</td>
            <td>{{ details?.join_way || "-" }}</td>
          </tr>
          <tr>
            <td>우대조건</td>
            <td>{{ details?.spcl_cnd || "-" }}</td>
          </tr>
          <tr>
            <td>가입제한</td>
            <td>
              {{
                details?.join_deny === 1
                  ? "제한없음"
                  : details?.join_deny === 2
                  ? "서민전용"
                  : details?.join_deny === 3
                  ? "일부제한"
                  : "-"
              }}
            </td>
          </tr>
          <tr>
            <td>가입대상</td>
            <td>{{ details?.join_member || "-" }}</td>
          </tr>
          <tr>
            <td>최고 한도</td>
            <td>{{ details?.max_limit ? details.max_limit.toLocaleString() : "-" }}</td>
          </tr>
          <tr>
            <td>기타 유의사항</td>
            <td>{{ details?.etc_note || "-" }}</td>
          </tr>
        </tbody>
      </table>
      <p class="note">※ 제공된 정보는 공시 기준일을 기준으로 합니다.</p>
      <!-- 가입하기 버튼 -->
      <button class="join-button" @click="handleJoin">가입하기</button>
    </div>
  </div>
</template>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: #fff;
  padding: 20px 40px;
  border-radius: 10px;
  width: 500px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  position: relative; /* 닫기 버튼 위치를 위해 필요 */
}

.modal-title {
  font-size: 1.5rem;
  font-weight: bold;
  text-align: left; /* 왼쪽 정렬 */
  margin-bottom: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: left;
  font-size: 0.95rem;
}

td:first-child {
  font-weight: bold;
  background: #f9f9f9;
  width: 40%;
}

.close-button {
  position: absolute;
  top: 20px;
  right: 20px;
  background: #ff4d4f;
  color: white;
  border: none;
  padding: 8px 12px;
  font-size: 0.9rem;
  cursor: pointer;
  border-radius: 5px;
  transition: background 0.3s;
}

.close-button:hover {
  background: #d9363e;
}

.note {
  margin-top: 20px;
  font-size: 0.85rem;
  color: #666;
}

/* 가입하기 버튼 */
.join-button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 1rem;
  background-color: #4287f7;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  display: block;
  margin-left: auto;
  margin-right: auto; /* 가운데 정렬 */
  transition: background 0.3s, box-shadow 0.3s;
}

.join-button:hover {
  background-color: #004494;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}
</style>
