<!-- src/layouts/BaseLayout.vue -->
<template>
  <div class="compare-list-menu-view">
    <CompareListMenuView />
    <!-- 공통 메뉴 -->
    <router-view />
    <!-- 자식 컴포넌트를 렌더링 -->
  </div>
</template>
<script setup>
import CompareListMenuView from "@/components/CompareListMenu.vue";
</script>
<style>
/* 공통 레이아웃 스타일 */
.compare-list-menu-view {
  display: flex;
  flex-direction: column;
  padding: 32px;
}
</style>
