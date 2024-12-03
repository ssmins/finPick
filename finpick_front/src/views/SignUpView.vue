<template>
  <div class="signup">
    <div class="signup-container">
      <h2 class="title">회원가입</h2>
      <form @submit.prevent="signUp">
        <div class="form-group">
          <label for="username">아이디</label>
          <input type="text" id="username" v-model.trim="username" /><br />
        </div>

        <div class="form-group">
          <label for="password1">비밀번호</label>
          <input
            type="password"
            id="password1"
            v-model.trim="password1"
          /><br />
        </div>

        <div class="form-group">
          <label for="password2">비밀번호 확인</label>
          <input type="password" id="password2" v-model.trim="password2" />
        </div>

        <div class="form-group">
          <label for="email">이메일</label>
          <input type="text" id="email" v-model.trim="email" />
        </div>

        <div class="form-group">
          <label for="nickname">닉네임</label>
          <input type="text" id="nickname" v-model.trim="nickname" />
        </div>

        <div class="form-group">
          <label for="age">나이</label>
          <input type="text" id="age" v-model.trim="age" />
        </div>

        <div class="form-group">
          <label for="salary">현재 연봉</label>
          <select id="salary" v-model="salary">
            <option value="<3000">3천만원 미만</option>
            <option value="3000-5000">3천만원 이상 5천만원 이하</option>
            <option value="5000-10000">5천만원 이상 1억원 미만</option>
            <option value=">10000">1억원 이상</option>
          </select>
        </div>

        <div class="form-group">
          <label for="depositAmount">예금 희망 금액</label>
          <select id="depositAmount" v-model="depositAmount">
            <option value="0-500">500만원 이하</option>
            <option value="500-1000">500만원 이상 1천만원 이하</option>
            <option value="1000-5000">1천만원 이상 5천만원 이하</option>
            <option value=">5000">5천만원 이상</option>
          </select>
        </div>

        <div class="form-group">
          <label for="depositPeriod">예금 희망 기간</label>
          <select id="depositPeriod" v-model="depositPeriod">
            <option value="6">6개월 미만</option>
            <option value="12">6개월 이상 1년 미만</option>
            <option value="24">1년 이상 2년 미만</option>
            <option value="36">2년 이상</option>
          </select>
        </div>

        <div class="form-group">
          <label for="savingsAmount">월 적금 희망 금액</label>
          <select id="savingsAmount" v-model="savingsAmount">
            <option value="0-500">50만원 미만</option>
            <option value="500-1000">50만원 이상 100만원 미만</option>
            <option value="1000-5000">100만원 이상 300만원 미만</option>
            <option value=">5000">300만원 이상</option>
          </select>
        </div>

        <div class="form-group">
          <label for="savingsPeriod">적금 희망 기간</label>
          <select id="savingsPeriod" v-model="savingsPeriod">
            <option value="6">6개월 미만</option>
            <option value="12">6개월 이상 1년 미만</option>
            <option value="24">1년 이상 2년 미만</option>
            <option value="36">2년 이상</option>
          </select>
        </div>

        <input type="submit" value="회원가입" />
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const email = ref(null);
const nickname = ref(null);
const age = ref(0);
const salary = ref(null);
const depositAmount = ref(null);
const depositPeriod = ref(null);
const savingsAmount = ref(null);
const savingsPeriod = ref(null);

import { useCounterStore } from "@/stores/counter";
const store = useCounterStore();

const signUp = function () {
  // if (!email.value) {
  //   alert('이메일을 입력하세요')
  //   return
  // }
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
    nickname: nickname.value,
    age: age.value,
    salary: salary.value,
    depositAmount: depositAmount.value,
    depositPeriod: depositPeriod.value,
    savingsAmount: savingsAmount.value,
    savingsPeriod: savingsPeriod.value,
  };
  store.signUp(payload);
};
</script>

<style scoped>
.signup {
  padding: 62px;
}
.signup-container {
  background-color: var(--color-background-soft);
  padding: 2rem;
  border-radius: 8px;
  max-width: 500px;
  margin: 0 auto;
  box-shadow: 0 0px 8px rgba(0, 0.2, 0.2, 0.3);
}

.signup-container h2 {
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
input[type="password"],
select {
  width: 100%;
  padding: 0.8rem;
  border: 2px solid #cccccc;
  border-radius: 4px;
  font-size: 1rem;
  color: var(--color-text);
  background-color: white;
  appearance: none; /* 기본 브라우저 화살표 제거 */
  -webkit-appearance: none;
  -moz-appearance: none;
}

select {
  background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23777777'%3E%3Cpath d='M7 10l5 5 5-5z'/%3E%3C/svg%3E"); /* 화살표 아이콘 추가 */
  background-repeat: no-repeat;
  background-position: right 1rem center;
  background-size: 1rem;
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
</style>
