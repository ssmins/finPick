import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
 
export const useCounterStore = defineStore('counter', () => {

  // state 
  const API_URL = 'http://127.0.0.1:8000' // django 서버 url  
  const router = useRouter() 

  const d_products = ref([]) // deposit, savings 저장될 products 
  const s_products = ref([]) // deposit, savings 저장될 products 
  const articles = ref([]) // deposit, savings 를 가져와서 articles 로 변환  

  const token = ref(null) // 회원가입 시 발급되고 로그인 시 생기는 토큰 
  const user = ref(null) // 현재 로그인한 사용자 정보

  const iscreatedDeposit = ref(false) 
  const iscreatedSavings = ref(false) 
  const isgetCompareProducts = ref(false) 

  const bankInMap = ref([]) // kakao에서 가져올 map 내 있는 은행 정보들 

  // actions 
  
  // API에서 article 가져오기 
  
  // 1. product 가져오기 - post 

  
  const createDeposit = function () {
    if (iscreatedDeposit.value) {
      console.log('Deposit은 이미 생성되었습니다.')
      return 
    }
    
    axios({
      method : 'get', 
      url : `${API_URL}/products/save-deposit-products/`, 
      // headers : {
        //   Authorization : `Token ${token.value}` // token 필요한가? 
        // }
      })
      .then((response) => {
        console.log('create Deposit success ! :', response)
        d_products.value = response.data 
        iscreatedDeposit.value = true
      })
      .catch((error) => {
        console.log('create Deposit error :', error)
      })
      
    }
    
    const createSavings = function () {
      if (iscreatedSavings.value) {
        console.log('Saving은 이미 생성되었습니다.')
        return 
      }
  
      axios({
        method: 'get', 
        url : `${API_URL}/products/save-saving-products/`
      })
        .then((response) => {
          console.log('create Savings success !', response)
          s_products.value = response.data
          iscreatedSavings.value = true
        })
        .catch((error) => {
          console.log('create Savings error :', error)
        })
    }

    // 2-1. createArticles
  const createArticles = function () { 
    axios({
      method : 'post', 
      url : `${API_URL}/articles/create-articles/`, // post method 실행 
      // headers: {
      //   Authorization : `Token ${token.value}` // token 필요한가? 
      // }
    })
      .then((response) => {
        console.log(response)
      })
      .catch((error) => {
        console.log('createArticles error', error)
      }) 
  } 


  // 2-2. article로 불러오기 - get 
  const getArticles = function () {
    axios({
      method : 'get' , 
      url : `${API_URL}/articles/get-articles/`, // Django와 소통하는 창구 (여기서 api/v1/ 안 붙여주면 error 뜨려나 ?)
      // headers : {
      //   Authorization : `Token ${token.value}`
      // }
    })
      .then((response) => {
        console.log('response :', response)
        articles.value = response.data 
        console.log(articles) 
      })
      .catch((error) => {
        console.log('getArticles error', error)
      })
  }

  const signUp = function (payload) {
    console.log('signUp 함수 실행 시 전달되는 payload : ', payload) // payload 전달 OK s
    const { username , password1, password2, email, nickname, age, salary, depositAmount, depositPeriod, savingsAmount, savingsPeriod } = payload

    // const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    // if (!emailRegex.test(email.value)) {
    //   alert('유효한 이메일 주소를 입력하세요')
    //   return 
    // }

    axios({
      method : 'post', 
      url : `${API_URL}/accounts/registration/`, 
      data : {
        username, password1, password2, email, nickname, age, salary, depositAmount, depositPeriod, savingsAmount, savingsPeriod 
      }
    })
      .then((response) => {
        console.log('회원가입에 성공했습니다.')
        console.log('response : ', response) // key 확인 
        console.log(response.data) // key 확인 
        router.push('/') // HomeView로 이동 
      })
      .catch((error) => {
        console.log('회원가입에 실패했습니다.')
        console.log('Error Details:', error.response ? error.response.data : error.message)
        // 에러 메시지 표시
        alert(error.response ? 
            JSON.stringify(error.response.data) : 
            '회원가입 중 오류가 발생했습니다.'
        )
        // console.log(error.request)
        // console.log(error.request.response)
      })
  }

  const logIn = function (payload) {
    const { username , password } = payload 
    axios({
      method : 'post', 
      url : `${API_URL}/accounts/login/`, 
      data : {
        username, password
      }
    })
      .then((response) => {
        console.log('정상적으로 dj_rest_auth를 통해 로그인에 성공했습니다.', response)
        token.value = response.data.key 
        fetchUserInfo() // 사용자 정보 요청 함수 호출 
        // user.value = response.data.user // 로그인한 유저 정보 저장 
        console.log('user : ', user.value)
        // getProducts() // 
        router.push('/') // HomeView로 이동 
      })
      .catch((error) => {
        console.log('비정상적인 접근입니다. dj_rest_auth를 통해 로그인되지 않았습니다.', error)
        alert('비정상적인 접근입니다. 로그인되지 않았습니다.')
      })
  }

  const fetchUserInfo = function () {
    axios({
      method : 'get' , 
      url : `${API_URL}/accounts/user/`, 
      headers : {
        Authorization : `Token ${token.value}`, 
      }
    })
      .then((response) => {
        console.log('사용자 정보 요청 성공', response)
        user.value = response.data 
      })
      .catch((error) => {
        console.log('사용자 정보 가져오기 실패', error)
      })
  }
  
  // const logOut = function () {
  //   axios({
  //     method: 'post', 
  //     url: `${API_URL}/accounts/logout/`
  //   })
  //     .then((response) => {
  //       console.log('정상적으로 dj_rest_auth를 통해 로그아웃되었습니다.', response)
  //       router.push('/')
  //     })
  //     .catch((error) => {
  //       console.log('비정상적인 접근입니다. dj_rest_auth를 통해 로그아웃되지 않았습니다.', error)
  //     })
  // }

  const logOut = function () {
    token.value = null
    user.value = null // 로그아웃 시 초기화 
    console.log('로그아웃되었습니다.')
    router.push('/') // HomeView로 이동 
  }

  // CompareDepositView 실행 시 , get 요청으로 예/적금 정보 가져오기 
  
  
  const getCompareProducts = function () { 
    if (isgetCompareProducts.value) {
      console.log('이미 getCompareProducts 호출이 완료되었습니다.')
      return 
    }

    axios({
      method : 'get', 
      url : `${API_URL}/products/save-deposit-products/`
    })
      .then((response) => {
        console.log('getCompareProducts 성공 ! ', response)
        isgetCompareProducts.value = true // 호출 완료로 변경 
      })
      .catch((error) => {
        console.log('getCompareProducts 실패 , ', error)
      })
  }

  const getBanksMap = function (params) {
    const { city, district, neighborhood, keyword } = params
    axios({
      method : 'get', 
      url : `${API_URL}/bankmaps/search-banks/`, 
      params : { // get 요청에는 일반적으로 data 가 아니라 params 로 데이터를 전달한다. 
        city, district, neighborhood, keyword 
      }
    })
      .then((response) => {
        console.log('getBanksMap success ! ', response)
        bankInMap.value = response.data
        console.log('bankInMap : ', bankInMap.value)
      })
      .catch((error) => {
        console.log(error)
      })
  }


  // getter 


  return { 
    d_products, s_products, articles, token, API_URL, router, user, bankInMap, 
    createDeposit, createSavings, createArticles, getArticles, signUp, logIn, fetchUserInfo, logOut, getCompareProducts, getBanksMap, 
   }
}, {persist: true}) // 새로고침 해도 토큰이 남아있기 
