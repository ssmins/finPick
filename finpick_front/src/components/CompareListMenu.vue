<script setup>
import { useRouter, useRoute } from "vue-router";

const router = useRouter();
const route = useRoute();

// 예금 페이지로 이동하는 함수
const goToDeposit = () => {
  router.push({ name: "CompareDepositView" });
};

// 적금 페이지로 이동하는 함수
const goToSavings = () => {
  router.push({ name: "CompareSavingsView" });
};
</script>

<template>
  <div class="link-wrapper">
    <p
      class="link"
      :class="{ active: route.name === 'CompareDepositView' }"
      @click="goToDeposit"
    >
      예금
    </p>
    <span>&nbsp;|&nbsp;</span>
    <p
      class="link"
      :class="{ active: route.name === 'CompareSavingsView' }"
      @click="goToSavings"
    >
      적금
    </p>
  </div>
</template>

<style scoped>
.link-wrapper {
  padding: 20px 0px;
  display: flex;
  gap: 8px;
  font-size: 1.5rem;
}
/* 예금, 적금 링크 스타일 */
.link {
  cursor: pointer; /* 마우스를 올렸을 때 클릭 가능한 커서 */
  text-decoration: none;
  font-weight: 600;
}

/* 호버 시 스타일 */
.link:hover {
  color: #4287f7;
}

/* 활성화된 링크 스타일 */
.link.active {
  color: #4287f7; /* 선택된 링크에 색상 추가 */
}
</style>
