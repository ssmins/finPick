<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";
const store = useCounterStore();
const username = ref(null);
const password = ref(null);

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<template>
  <div class="login">
    <div class="login-container">
      <h2 class="title">로그인</h2>
      <form @submit.prevent="logIn">
        <div class="form-group">
          <label for="username">아이디</label>
          <input type="text" id="username" v-model.trim="username" /><br />
        </div>

        <div class="form-group">
          <label for="password">비밀번호</label>
          <input type="password" id="password" v-model.trim="password" />
        </div>

        <input type="submit" value="로그인" />
        <!-- <RouterLink :to="{ name : 'SignUpView' }" class="signup-link"> 회원가입하기 </RouterLink> -->
        <RouterLink
          :to="{ name: 'SignUpView' }"
          class="signup-button"
        >
          회원가입
        </RouterLink>      
      </form>
    </div>
  </div>
</template>

<style scoped>
/* .signup-link {
  display: block; 
  text-align: center; 
  margin-top: 1rem; 
  font-size: 0.9rem; 
  color: #4287f7; 
  text-decoration: none; 
  transition: 0.3s; 
}

.signup-link:hover {
  text-decoration: underline; 
  color: #2a6bda; 
} */

.login {
  padding: 62px;
}
.login-container {
  background-color: var(--color-background-soft);
  padding: 2rem;
  border-radius: 8px;
  max-width: 500px;
  margin: 0 auto;
  box-shadow: 0 0px 8px rgba(0, 0.2, 0.2, 0.3);
}

.login-container h2 {
  color: var(--color-heading);
  text-align: center;
  margin-bottom: 1.5rem;
}

.title {
  font-size: 1.5rem;
  text-decoration: none;
  font-weight: 600;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  font-size: 1rem;
  color: var(--color-text);
  display: block;
  margin-bottom: 0.5rem;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 0.8rem;
  border: 2px solid #cccccc;
  border-radius: 4px;
  font-size: 1rem;
  color: var(--color-text);
}

input[type="submit"] {
  width: 100%;
  padding: 1rem;
  background-color: #4287f7;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: 0.3s;
  margin-top: 20px;
}

input[type="submit"]:hover {
  background-color: #4287f7;
}

.signup-button {
  display: block; /* 블록 요소로 설정 */
  width: 100%; /* 버튼 너비를 100%로 */
  padding: 1rem; /* 내부 여백 */
  text-align: center; /* 텍스트 가운데 정렬 */
  font-size: 1.1rem; /* 폰트 크기 */
  font-weight: bold; /* 폰트 두께 */
  background-color: #f1f1f1; /* 버튼 배경색 (회원가입용 색상) */
  color: #333; /* 텍스트 색상 */
  border: 1px solid #cccccc; /* 테두리 */
  border-radius: 4px; /* 둥근 모서리 */
  cursor: pointer; /* 마우스 포인터 변경 */
  margin-top: 1rem; /* 위와의 간격 */
  text-decoration: none; /* 밑줄 제거 */
  transition: 0.3s; /* 호버 효과 전환 시간 */
}

.signup-button:hover {
  background-color: #e0e0e0; /* 호버 시 배경색 변경 */
  color: #000; /* 호버 시 텍스트 색상 변경 */
}
</style>
