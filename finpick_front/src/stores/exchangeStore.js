import { defineStore } from 'pinia';
import axios from 'axios';

export const useExchangeStore = defineStore('exchange', {
  state: () => ({
    currencyList: []
  }),
  actions: {
    fetchCurrencies() {
      return axios.get('http://127.0.0.1:8000/exchange/')
        .then(response => {
          this.currencyList = response.data;
        })
        .catch(error => {
          console.error('Failed to fetch exchange data:', error);
          throw error; 
        });
    }
  }
});

