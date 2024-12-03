
<script setup>
import { RouterLink } from 'vue-router';
defineProps({
  article: Object
})

</script>

<template>
  <h2>ArticleListItem</h2>
  <div>
    <!-- <h5>이 곳에 들어갈 Article들</h5> -->
    <!-- <h5>{{ article.id }}</h5> -->
    <h5>{{ article.title }}</h5>
    <h5>{{ article.content }}</h5> <!-- 내용이 없네 .?  -->
    <h5>가입 방법 : {{ article.join_way }}</h5>
    <h5>세부 사항 : {{ article.mtrt_int }}</h5>
    <h5>우대 사항 : {{ article.spcl_cnd }}</h5>
    <!-- <RouterLink :to="{ name: 'ArticleDetailView', params: { id : article.id }}">
      더보기
    </RouterLink> -->
  </div>



</template>