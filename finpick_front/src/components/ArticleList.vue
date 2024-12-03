
<script setup>
import ArticleListItem from '@/components/ArticleListItem.vue'
import { useCounterStore } from '@/stores/counter';
import { onMounted } from 'vue';
const store = useCounterStore() 
onMounted(() => {
  // store.getArticles() 
})

</script>

<template>
  <h2>ArticleList</h2>
  <ArticleListItem 
  v-for="article in store.articles"
  :key="article.id"
  :article="article"
  />

</template>