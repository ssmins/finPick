import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
 
export const useMapStore = defineStore('map', () => {

  // state 

  const bankInMap = ref([]) // kakao에서 가져올 map 내 있는 은행 정보들 
  const API_URL = 'http://127.0.0.1:8000'

  // actions 
  
  
  const getBanksMap = function (params) {
    const { city, district, neighborhood, keyword } = params
    axios({
      method : 'get', 
      url : `${API_URL}/bankmaps/search-banks/`, 
      params : { // get 요청에는 일반적으로 data 가 아니라 params 로 데이터를 전달한다. 
        city, 
        district, 
        neighborhood, 
        keyword,  
      }
    })
      .then((response) => {
        console.log('getBanksMap success ! ', response)
        bankInMap.value = response.data
        console.log('bankInMap : ', bankInMap.value)
      })
      .catch((error) => {
        console.log('getBanksMap error : ', error)
      })
  }


  // getter 


  return { 
    bankInMap,
    getBanksMap, 
   }
}, {persist: true}) // 새로고침 해도 토큰이 남아있기 
