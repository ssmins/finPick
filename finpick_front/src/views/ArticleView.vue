<script setup>
import ArticleList from '@/components/ArticleList.vue'
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore() 

import { onMounted } from 'vue';
onMounted(() => {
  // store.getProducts()
  // store.getArticles() // HomeView 
})

</script>

<template>
  <h1>ArticleView</h1>
  <ArticleList />

</template>

<style scoped>



</style>