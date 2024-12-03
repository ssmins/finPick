<template>
  <header class="main-header">
    <nav class="main-nav-wrapper">
      <RouterLink :to="{ name: 'HomeView' }" class="logo">FinPick</RouterLink>
      <div class="nav-links">
        <!-- 로그인 여부와 상관없는 페이지  -->
        <!-- <RouterLink :to="{ name: 'RecommandView' }">Recommand</RouterLink>
      <RouterLink :to="{ name: 'ArticleView' }">Article</RouterLink> -->
        <RouterLink
          :to="{ name: 'CompareDepositView' }"
          :class="{ active: $route.name === 'CompareDepositView' }"
        >
          금리비교
        </RouterLink>
        <RouterLink
          :to="{ name: 'ExchangeView' }"
          :class="{ active: $route.name === 'ExchangeView' }"
        >
          환율계산
        </RouterLink>
        <RouterLink
          :to="{ name: 'BankMapView' }"
          :class="{ active: $route.name === 'BankMapView' }"
        >
          주변은행
        </RouterLink>
        <!-- 비로그인 상태 v-if="!store.token"-->
        <RouterLink
          v-if="!store.token"
          :to="{ name: 'LoginView' }"
          :class="{ active: $route.name === 'LoginView' }"
        >
          로그인
        </RouterLink>
        <RouterLink
          v-if="!store.token"
          :to="{ name: 'SignUpView' }"
          :class="{ active: $route.name === 'SignUpView' }"
        >
          회원가입
        </RouterLink>
        <!-- 로그인 상태 v-if="store.token"-->
        <!-- <RouterLink v-if="store.token" :to="{ name: 'MyPageView' }"
          >마이페이지</RouterLink
        > -->
        <RouterLink
          v-if="store.token"
          :to="{ name: 'MyPageView' }"
          :class="{ active: $route.name === 'MyPageView' }"
        >
          마이페이지
        </RouterLink>
        <!-- <RouterLink v-if="store.token" @click.prevent="store.logOut" to="#"
          >로그아웃</RouterLink
        > -->
      </div>
      <!-- <div class="hamburger-menu" @click="toggleMenu">
      &#9776;
    </div> -->
    </nav>
  </header>
</template>
<script setup>
import { useCounterStore } from "@/stores/counter";
const store = useCounterStore();
</script>
<style scoped>
.main-header {
  display: flex;
  justify-content: center;
  width: 100%;
  background-color: var(--color-background-soft);
  box-shadow: 0px 14px 12px -10px rgba(0, 0, 0, 0.1);
}

.main-nav-wrapper {
  width: 1536px;
  padding: 16px 32px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* 로고 스타일 */
.logo {
  /* align-items: center; */
  font-size: 2rem;
  font-weight: bold;
  color: var(--color-heading);
  text-decoration: none;
  /* cursor: pointer; */
  flex-grow: 0;
}

/* 로고에 마우스를 올려도 배경색이 변경되지 않도록 설정 */
.logo:hover {
  background-color: transparent !important; /* 배경색 변경 효과 제거 */
  color: var(--color-heading); /* 텍스트 색 유지 */
  cursor: pointer; /* 클릭 가능 커서 */
}

/* 네비게이션 링크들 */
.nav-links {
  display: flex;
  gap: 2rem;
  flex-grow: 1;
  justify-content: flex-end;
}

/* 링크 스타일 */
.nav-links {
  text-decoration: none;
  color: black !important;
  font-size: 1.2rem;
  font-weight: 700;
  padding: 0.5rem;
  transition: color 0.3s ease, border-bottom 0.3s ease;
}

/* 호버 시 링크 효과 */
.nav-links:hover {
  color: #4287f7 !important;
  border-bottom: 2px solid var(--vt-c-indigo);
}

.nav-links a.active {
  color: #4287f7;
}

/* 햄버거 메뉴 버튼 */
/* .hamburger-menu {
  display: none;
  font-size: 2rem;
  cursor: pointer;
  color: var(--color-heading);
} */

/* 반응형 햄버거 메뉴 */
/* .hamburger-menu {
  display: block;
} */
</style>
