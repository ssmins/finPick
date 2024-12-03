<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import CompareDepositDetailView from "./CompareDetailView.vue";

// 상태 관리
const bankFilter = ref("전체은행"); // 필터 선택값
const bankList = ref(["전체은행"]); // 은행 목록
const depositProducts = ref([]); // 예금 상품 목록
const isModalVisible = ref(false); // 모달 표시 여부
const selectedDetails = ref(null); // 선택된 금융 상품 상세 정보
const sortDirection = ref({}); // 각 기간별 정렬 상태

// 은행 목록 가져오기
const fetchBanks = async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/products/bank-list/"
    );
    bankList.value = ["전체은행", ...response.data]; // "전체은행" 옵션 추가
  } catch (error) {
    console.error("은행 목록 가져오기 실패:", error);
  }
};

// 예금 상품 목록 가져오기
const fetchDeposits = async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/products/deposit-products/",
      {
        params: {
          bank: bankFilter.value !== "전체은행" ? bankFilter.value : undefined, // 필터 조건 적용
        },
      }
    );
    depositProducts.value = response.data; // 데이터 업데이트
  } catch (error) {
    console.error("예금 데이터 가져오기 실패:", error);
  }
};

// 필터 적용 함수
const applyFilter = () => {
  fetchDeposits(); // 선택된 필터로 데이터 재조회
};

// 상세 모달 열기
const openDetailModal = (details) => {
  selectedDetails.value = details; // 선택된 상품 데이터 설정
  isModalVisible.value = true; // 모달 표시
};

// 금리 정렬 함수
const sortByRate = (term) => {
  const direction = sortDirection.value[term] || "asc"; // 기본 정렬은 오름차순
  depositProducts.value.sort((a, b) => {
    const rateA = a.terms[term]?.intr_rate || 0;
    const rateB = b.terms[term]?.intr_rate || 0;
    return direction === "asc" ? rateA - rateB : rateB - rateA;
  });
  // 방향 토글
  sortDirection.value[term] = direction === "asc" ? "desc" : "asc";
};

// 컴포넌트 마운트 시 데이터 가져오기
onMounted(() => {
  fetchBanks(); // 은행 목록 가져오기
  fetchDeposits(); // 예금 상품 데이터 가져오기
});
</script>

<template>
  <div>
    <!-- 필터 섹션 -->
    <div class="filter-section">
      <div class="filter-row">
        <label>은행을 선택하세요</label>
        <select v-model="bankFilter">
          <option v-for="bank in bankList" :key="bank" :value="bank">
            {{ bank }}
          </option>
        </select>
      </div>
      <button @click="applyFilter">확인</button>
    </div>

    <!-- 예금 상품 목록 -->
    <div>
      <h2 class="list-title">정기 예금 상품 목록</h2>
      <table>
        <thead>
          <tr>
            <th>공시 제출월</th>
            <th>금융회사명</th>
            <th>상품명</th>
            <th>
              6개월
              <button @click="sortByRate('6개월')">▲ ▼</button>
            </th>
            <th>
              12개월
              <button @click="sortByRate('12개월')">▲ ▼</button>
            </th>
            <th>
              24개월
              <button @click="sortByRate('24개월')">▲ ▼</button>
            </th>
            <th>
              36개월
              <button @click="sortByRate('36개월')">▲ ▼</button>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="product in depositProducts"
            :key="product.fin_prdt_cd"
            @click="openDetailModal(product)"
          >
            <td>{{ product.dcls_month }}</td>
            <td>{{ product.kor_co_nm }}</td>
            <td>{{ product.fin_prdt_nm }}</td>
            <td>{{ product.terms["6개월"]?.intr_rate || "-" }}</td>
            <td>{{ product.terms["12개월"]?.intr_rate || "-" }}</td>
            <td>{{ product.terms["24개월"]?.intr_rate || "-" }}</td>
            <td>{{ product.terms["36개월"]?.intr_rate || "-" }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 상세 모달 -->
    <CompareDepositDetailView
      :isVisible="isModalVisible"
      :details="selectedDetails"
      @close="isModalVisible = false"
    />
  </div>
</template>

<style scoped>
/* 필터 섹션 스타일 */
.filter-section {
  display: flex;
  align-items: flex-start;
  width: 320px; /* 340*/
  margin: 20px 0;
  padding: 1rem;
  background-color: var(--color-background-soft);
  border-radius: 10px;
  box-shadow: 0 0px 8px rgba(0, 0.2, 0.2, 0.3);
}

.filter-row {
  display: flex;
  flex-direction: column;
  margin-right: 15px;
}

label {
  font-size: 1rem;
  color: #333;
  margin-bottom: 12px;
}

select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #fff;
  font-size: 1rem;
  color: #333;
  outline: none;
  transition: border-color 0.3s;
}

select:focus {
  border-color: #4287f7;
}

/* 테이블 스타일 */
.list-title {
  padding: 12px 0;
  font-size: 1.3rem;
  font-weight: bold;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

th {
  background-color: #f2f2f2;
  font-weight: bold;
  position: relative;
}

th button {
  margin-left: 8px;
  padding: 2px 5px;
  font-size: 0.8rem;
  cursor: pointer;
  border: none;
  background: transparent;
  color: black;
}

th button:hover {
  background-color: #c2c2c2;
}

button {
  align-self: flex-end;
  padding: 8px 16px;
  font-size: 1rem;
  background-color: #4287f7;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s, transform 0.2s;
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
</style>
