<template>
    <div class="message-content" v-html="parsedContent"></div>
  </template>
  
  <script setup>
  import { computed } from "vue";
  
  const props = defineProps({
    content: String,
  });
  
  const parsedContent = computed(() => {
    const urlRegex = /\(?(https?:\/\/[^\s\)]+)\)?/g;
    return props.content.replace(urlRegex, (url) => {
      const cleanUrl = url.replace(/[\(\)]/g, ""); // 괄호 제거
      return `<a href="${cleanUrl}" target="_blank">${cleanUrl}</a>`;
    });
  });
  </script>
  
  <style scoped>
  .message-content a {
    text-decoration: none !important ;
    color: black !important;
    cursor: pointer !important;
  }
  </style>
  