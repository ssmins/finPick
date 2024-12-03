

<template>
  <div class="signup-container">
    <h2>Sign Up</h2>
    <form @submit.prevent="signUpNext">
      <div class="form-group">
        <label for="nickname"> 닉네임 : </label>
        <input type="text" id="nickname" v-model.trim="nickname">
      </div>
      
      <!-- <div class="form-group"> -->
        <input type="submit" value="Sign Up">
      <!-- </div> -->
    </form>
  </div>


</template>



<script setup>

import { ref } from 'vue';

const nickname = ref(null)


import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()

const signUp = function () {
  // if (!email.value) {
  //   alert('이메일을 입력하세요')
  //   return 
  // }
  const payload = {
    username : username.value , 
    password1 : password1.value, 
    password2 : password2.value, 
    email : email.value, 
    nickname : nickname.value, 
  }
  store.signUp(payload)
}

</script>


<style scoped>
.signup-container {
  background-color: var(--color-background-soft);
  padding: 2rem;
  border-radius: 8px;
  max-width: 400px;
  margin: 0 auto;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.signup-container h2 {
  color: var(--color-heading);
  text-align: center;
  margin-bottom: 1rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  font-size: 14px;
  color: var(--color-text);
  display: block;
  margin-bottom: 0.5rem;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  font-size: 14px;
  color: var(--color-text);
}

input[type="submit"] {
  width: 100%;
  padding: 1rem;
  background-color: hsla(160, 100%, 37%, 1);
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: 0.3s;
}

input[type="submit"]:hover {
  background-color: hsla(160, 100%, 37%, 0.8);
}

</style>