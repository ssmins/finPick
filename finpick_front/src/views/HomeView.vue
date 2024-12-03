<script setup>
import { onMounted } from "vue";
import { useCounterStore } from "@/stores/counter";
const store = useCounterStore();
import { RouterLink } from "vue-router";

onMounted(() => {
  store.createDeposit();
  store.createSavings();
  // store.createArticles() // article이 생성되지 않고 있다.
  // store.getArticles()
  // store.getCompareProducts()
});
</script>

<template>
  <div>
    <!-- <h1>Home Page</h1> -->

    <div class="main-container">
      <article class="main-container">
        <section>
          <RouterLink v-if="store.token" :to="{ name : 'CompareDepositView' }">
            <img 
            class="main-banner-img"
            src="../assets/image/main_banner_1.png"
            alt="banner"
            />
          </RouterLink>
          <RouterLink v-if="!store.token" :to="{ name : 'LoginView' }">
            <img 
            class="main-banner-img"
            src="../assets/image/main_banner_1.png"
            alt="banner"
            />
          </RouterLink>
          <img
            class="main-menu-img"
            src="../assets/image/main_menu_3.png"
            alt="main-menu"
          />
        </section>
        <!-- <section class="main-section">

          <div class="recommend-section">
            <h2>나에게 꼭 맞는 예/적금 추천받기</h2>
            <p>
              내 친구는 어떤 적금에 가입해 얼마씩 납입하고 있을까요? <br />
              목돈을 넣어 둘 예금이 필요해요, 어떤 상품을 선택해야 할까요?
            </p>
            <RouterLink :to="{ name: 'RecommandView' }" class="button"
              >나에게 꼭 맞는 예/적금 추천받기</RouterLink
            >
          </div>

          <div class="row">
            <div class="half-section">
              <h2>인기글</h2>
              <p>
                [예금] 한국스탠다드차타드은행 퍼스트정기예금 후기 <br />
                [꿀팁] 2024 금리 높은 저축은행 예금, 저축은행 적금 추천
              </p>
              <RouterLink :to="{ name: 'ArticleView' }" class="button"
                >더보기</RouterLink
              >
            </div>
            <div class="half-section">
              <h2>상품 비교하기</h2>
              <p>금융기관별 , 예/적금 금리 비교 페이지입니다.</p>
              <RouterLink :to="{ name: 'CompareDepositView' }" class="button"
                >더보기</RouterLink
              >
            </div>
          </div>


          <div class="row">
            <div class="half-section">
              <h2>환율 계산기</h2>
              <p>해외 여행을 계획 중이신가요?</p>
              <RouterLink :to="{ name: 'ExchangeView' }" class="button"
                >환율 계산기 실행하기</RouterLink
              >
            </div>
            <div class="half-section">
              <h2>은행 정보 보기</h2>
              <p>주변의 은행을 안내합니다.</p>
              <RouterLink :to="{ name: 'BankMapView' }" class="button"
                >내 근처 은행 보기</RouterLink
              >
            </div>
          </div>
          
        </section> -->
      </article>
    </div>
  </div>
</template>

<style scoped>
.section {
  width: 100%;
}

.main-banner-img {
  width: 100%;
  height: auto;
}
.main-menu-img {
  width: 100%;
}

.main-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;

  & > *:not(:last-child) {
    margin-bottom: 28px;
  }
}

.main-section {
  display: grid;
  grid-template-columns: 1fr; /* 기본적으로 한 열로 설정 */
  grid-template-rows: auto auto 1fr; /* 추천, 환율/은행, 후기 보기 구역의 순서대로 */
  gap: 1rem;
  margin-top: 2rem;
}

/* 주요 구역 스타일 */
.recommend-section,
.row .half-section,
.article-section {
  padding: 1rem 2rem;
  background-color: var(--color-background-soft); /*기본 배경색*/
  color: var(--color-text); /* 텍스트 색상 */
  border-radius: 8px;
  margin-bottom: 1rem;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
}

.recommend-section h2,
.row .half-section h2,
.article-section h2 {
  margin-bottom: 0.5rem;
  color: var(--color-heading); /* 헤딩 색상 */
}

.recommend-section p,
.row .half-section p,
.article-section p {
  font-size: 0.9rem;
  margin-bottom: 1rem;
  color: var(--color-text-muted); /* 흐릿한 텍스트 색상 */
}

.row {
  display: flex;
  justify-content: space-between; /* 양쪽에 배치 */
}

.half-section {
  width: 48%; /* 왼쪽 반, 오른쪽 반 차지 */
}

/* 버튼 스타일 */
.button {
  display: inline-block;
  padding: 0.5rem 1rem;
  background-color: var(--color-button); /* 기본 배경색 */
  color: var(--color-button-text); /* 버튼 텍스트 색상 */
  text-align: center;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
  transition: background-color 0.3s, color 0.3s;
}

.button:hover {
  background-color: var(--color-button-hover); /* Hover 시 배경색 */
  color: hsla(160, 100%, 37%, 1); /* Hover 시 텍스트 색상 */
  cursor: pointer;
}
</style>
