<script setup>
import { ref } from "vue";
import { RouterView } from "vue-router";
import Header from "./components/common/Header.vue";
import Footer from "./components/common/Footer.vue";
import ChatbotComponent from "@/components/Chatbot.vue";
import chatbotIcon from "@/assets/image/chatbot-icon.png"; // 챗봇 아이콘 이미지
import "vuetify/styles";

// 챗봇 열림/닫힘 상태 관리
const expand = ref(false);
</script>

<template>
  <Header></Header>
  <div class="content">
    <RouterView />
  </div>
  <Footer></Footer>

  <!-- 챗봇 -->
  <Transition name="bounce">
    <v-card
      v-show="expand"
      style="
        position: fixed;
        bottom: 130px;
        right: 50px;
        z-index: 1000;
        box-shadow: 0 0px 30px rgba(0, 0.2, 0.2, 0.6);
        border-radius: 15px;
      "
      class="mx-auto bg-secondary expand-component"
      height="600"
      width="400"
    >
      <ChatbotComponent />
    </v-card>
  </Transition>

  <v-avatar
    @click="expand = !expand"
    class="chatbot-btn"
    size="115"
    color="transparent"
    style="
      position: fixed;
      bottom: 20px;
      right: 50px;
      z-index: 1001;
      cursor: pointer;
    "
  >
    <v-img :src="chatbotIcon"></v-img>
  </v-avatar>
</template>

<style scoped>
.content {
  width: 1536px;
  margin: 0 auto;
}

.chatbot-btn {
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.6);
  transition: transform 0.3s ease-in-out;
}

.chatbot-btn:hover {
  transform: scale(1.05);
}

.bounce-enter-active,
.bounce-leave-active {
  transition: transform 0.3s;
}

.bounce-enter-from,
.bounce-leave-to {
  transform: scale(0.9);
}
</style>
