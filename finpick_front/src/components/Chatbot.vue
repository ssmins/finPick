<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import MessageContent from "@/components/MessageContent.vue"; // 새로 만든 컴포넌트 임포트

const AI_API_KEY = import.meta.env.VITE_AI_API_KEY;
const loading = ref(false);
const messages = ref([
  { role: "system", content: "FINPICK CHAT BOT" },
  { role: "assistant", content: "무엇이든지 물어보세요!" },
]);
const inputMessage = ref("");
const chatbotResponse = ref("");

// 예금 및 적금 데이터를 저장할 변수
const depositData = ref([]);
const savingData = ref([]);

// API를 통해 예금 및 적금 데이터를 가져오는 함수
const loadJSONData = async () => {
  try {
    // Django API에서 예금 데이터를 가져옵니다
    const depositResponse = await axios.get(
      "http://127.0.0.1:8000/api/deposit_products/"
    );
    depositData.value = depositResponse.data;

    // Django API에서 적금 데이터를 가져옵니다
    const savingResponse = await axios.get(
      "http://127.0.0.1:8000/api/saving_products/"
    );
    savingData.value = savingResponse.data;
  } catch (error) {
    console.error("Failed to load product data:", error);
  }
};

// 컴포넌트가 마운트될 때 데이터 로드
onMounted(() => {
  loadJSONData();
});

// 챗봇 API 호출 함수
const getChatbot = async () => {
  if (!inputMessage.value.trim()) return;

  loading.value = true;
  const userMessage = { role: "user", content: inputMessage.value };
  messages.value.push(userMessage);
  inputMessage.value = "";

  try {
    const response = await axios.post(
      "https://api.openai.com/v1/chat/completions",
      {
        model: "gpt-4",
        messages: [
          {
            role: "system",
            content: `당신은 금융 전문가입니다. 사용자가 제공한 데이터를 바탕으로 예금 및 적금 상품을 추천하세요.`,
          },
          ...messages.value,
        ],
      },
      {
        headers: {
          Authorization: `Bearer ${AI_API_KEY}`,
          "Content-Type": "application/json",
        },
      }
    );
    const botMessage = response.data.choices[0].message.content;
    messages.value.push({ role: "assistant", content: botMessage });
  } catch (error) {
    console.error("Error in Chatbot API:", error.response?.data || error);
    chatbotResponse.value = "Error: Unable to fetch response.";
  } finally {
    loading.value = false;
  }
};

// 데이터를 포맷팅하는 함수
const formatData = (data) => {
  return data
    .map((item) => {
      return `
      상품명: ${item.fin_prdt_nm}, 
      은행명: ${item.kor_co_nm}, 
      가입 방법: ${item.join_way}, 
      가입 제한: ${item.join_deny}, 
      특이 사항: ${item.spcl_cnd}
    `;
    })
    .join("<br>");
};

// 챗봇 초기화 함수
const resetChat = () => {
  messages.value = [
    {
      role: "assistant",
      content: "어서오세요! 투자 관련 질문을 환영합니다. 어떻게 도와드릴까요?",
    },
  ];
};
</script>

<template>
  <div>
    <v-list
      ref="messageContainer"
      style="width: 400px; height: 505px; overflow-y: auto"
    >
      <v-list-item v-for="(message, index) in messages" :key="index">
        <div
          class="ibm-plex-sans-kr-regular"
          :class="{
            'user-message': message.role === 'user',
            'assistant-message': message.role === 'assistant',
            'system-message': message.role === 'system',
          }"
        >
          <MessageContent :content="message.content" />
        </div>
      </v-list-item>
    </v-list>
    <div class="message-input">
      <v-progress-linear
        v-if="loading"
        color="grey-lighten-1"
        indeterminate
      ></v-progress-linear>
      <div class="d-flex">
        <v-text-field
          hint="나에게 맞는 금융 상품은?"
          class="ms-5 mb-3 me-3 mt-5"
          v-model="inputMessage"
          label="메시지를 입력하세요"
          @keydown.enter="getChatbot"
          rows="1"
          outlined
        ></v-text-field>
        <v-btn
          icon="mdi-arrow-up"
          class="custom-btn mt-6 arrow-up"
          @click="getChatbot()"
        ></v-btn>
        <v-btn
          icon="mdi-cached"
          class="custom-btn mt-6 mr-4 ms-3 cached"
          @click="resetChat()"
        ></v-btn>
      </div>
    </div>
  </div>
</template>

<style scoped>
.assistant-message {
  text-align: left;
  background-color: #f0f0f0;
  border: 1px solid #ddd;
  border-radius: 20px;
  display: inline-block;
  padding: 10px 15px;
  margin: 5px;
  max-width: 800px;
}

.user-message {
  text-align: right;
  float: right;
  background-color: #93beff;
  border: 1px solid #93beff;
  border-radius: 20px;
  padding: 10px 15px;
  margin: 5px;
  max-width: 800px;
}

.system-message {
  height: 40px;
  line-height: 40px;
  text-align: center;
  font-size: 21px;
  font-weight: 550;
  border-radius: 20px;
  background-color: #2e3d86;
  color: white;
}

.message-content {
  white-space: pre-wrap;
  word-break: break-word;
}

.chat-box {
  border: lightgrey 1px solid;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 20px;
}

.custom-btn.arrow-up {
  background-image: url("@/assets/image/send.png") !important;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}
.custom-btn.cached {
  background-image: url("@/assets/image/reset.png") !important;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

.message-input {
  background-color: white;
  color: black;
  position: absolute;
  bottom: 0;
  width: 100%;
}
</style>
