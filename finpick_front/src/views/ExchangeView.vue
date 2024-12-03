<template>
  <div class="exchange">
    <h2 class="title">환율 계산기</h2>
    <div class="content-wrapper">
      <div class="exchange-calculator">
        <div class="exchange-section">
          <!-- 환율 방향 선택 -->
          <div class="exchange-row">
            <label>변환 방향</label>
            <select v-model="conversionDirection">
              <option value="toForeign">원화 → 외화</option>
              <option value="toKrw">외화 → 원화</option>
            </select>
          </div>

          <!-- 환율 유형 선택 -->
          <div class="exchange-row">
            <label>환율 유형</label>
            <select v-model="selectedRateType">
              <option value="ttb">송금 받을 때</option>
              <option value="tts">송금 보낼 때</option>
              <option value="deal_bas_r">매매 기준율</option>
            </select>
          </div>

          <!-- 통화 선택 -->
          <div class="exchange-row">
            <label>통화 선택</label>
            <select v-model="tempSelectedCurrency">
              <option
                v-for="currency in currencyList"
                :key="currency.cur_unit"
                :value="currency.cur_unit"
              >
                {{ currency.cur_nm }}
              </option>
            </select>
          </div>

          <!-- 금액 입력 -->
          <div class="exchange-row">
            <label>금액 입력</label>
            <input
              v-model.number="tempAmount"
              type="number"
              placeholder="금액 입력"
            />
          </div>

          <!-- 변환 버튼 -->
          <button @click="calculateRate">변환</button>
        </div>

        <!-- 결과 표시 -->
        <div v-if="convertedAmount !== null" class="result-section">
          <h3 v-if="conversionDirection === 'toForeign'">
            {{ amount }} 원 = {{ convertedAmount }} {{ selectedCurrency }}
          </h3>
          <h3 v-else>
            {{ amount }} {{ selectedCurrency }} = {{ convertedAmount }} 원
          </h3>
        </div>
      </div>

      <div id="graph" ref="graphContainer">
        <a
          href="https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=2&acq=%ED%99%98%EC%9C%A8&qdt=0&ie=utf8&query=%ED%99%98%EC%9C%A8%EA%B3%84%EC%82%B0%EA%B8%B0"
          target="_blank"
        >
          <img src="@/assets/image/graph.png" alt="환율 그래프" />
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { useExchangeStore } from "@/stores/exchangeStore";

export default {
  data() {
    return {
      tempSelectedCurrency: "",
      tempAmount: 1,
      selectedCurrency: "",
      amount: 1,
      convertedAmount: null,
      selectedRateType: "deal_bas_r", // 기본 환율 유형
      conversionDirection: "toForeign", // 기본 변환 방향
    };
  },
  computed: {
    currencyList() {
      return this.exchangeStore.currencyList;
    },
  },
  created() {
    this.exchangeStore = useExchangeStore();
    this.exchangeStore
      .fetchCurrencies()
      .then(() => {
        console.log("Currencies fetched successfully");
      })
      .catch((error) => {
        console.error("Failed to fetch currencies:", error);
      });
  },
  methods: {
    calculateRate() {
      this.amount = this.tempAmount;
      this.selectedCurrency = this.tempSelectedCurrency;

      const selectedCurrencyData = this.currencyList.find(
        (rate) => rate.cur_unit === this.selectedCurrency
      );

      if (selectedCurrencyData) {
        let exchangeRate;
        if (this.selectedRateType === "ttb") {
          exchangeRate = parseFloat(selectedCurrencyData.ttb.replace(/,/g, ""));
        } else if (this.selectedRateType === "tts") {
          exchangeRate = parseFloat(selectedCurrencyData.tts.replace(/,/g, ""));
        } else if (this.selectedRateType === "deal_bas_r") {
          exchangeRate = parseFloat(
            selectedCurrencyData.deal_bas_r.replace(/,/g, "")
          );
        } else {
          console.error("유효하지 않은 환율 유형:", this.selectedRateType);
          this.convertedAmount = 0;
          return;
        }

        if (isNaN(exchangeRate)) {
          console.error("유효하지 않은 환율 데이터:", exchangeRate);
          this.convertedAmount = 0;
        } else {
          if (this.conversionDirection === "toForeign") {
            // 원화 -> 외화
            this.convertedAmount = (this.amount / exchangeRate).toFixed(2);
          } else if (this.conversionDirection === "toKrw") {
            // 외화 -> 원화
            this.convertedAmount = (this.amount * exchangeRate).toFixed(2);
          }
        }
      } else {
        console.error("통화를 찾을 수 없습니다:", this.selectedCurrency);
        this.convertedAmount = 0;
      }
    },
  },
};
</script>

<style scoped>
.exchange {
  display: flex;
  flex-direction: column;
  padding: 32px;
}

.title {
  padding: 20px 0px;
  display: flex;
  gap: 8px;
  font-size: 1.5rem;
  text-decoration: none;
  font-weight: 600;
}

.content-wrapper {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}

.exchange-calculator {
  padding: 1rem;
  border-radius: 10px;
  width: 40%;
  height: 500px;
  background-color: var(--color-background-soft);
  box-shadow: 0 0px 8px rgba(0, 0.2, 0.2, 0.3);
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.exchange-section {
  display: flex;
  flex-wrap: wrap;
  gap: 22px;
  align-items: flex-start;
}

.exchange-row {
  display: flex;
  flex-direction: column;
  width: 100%;
  gap: 8px;
}

.exchange-row label {
  font-size: 1rem;
  color: #333;
  margin-bottom: 12px;
}

.exchange-row input,
.exchange-row select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #fff;
  font-size: 1rem;
  color: #333;
  outline: none;
  transition: border-color 0.3s;
}

.exchange-row select:focus,
.exchange-row input:focus {
  border-color: #4287f7;
}

button {
  padding: 8px 16px;
  margin-top: 8px;
  font-size: 1rem;
  background-color: #4287f7;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s, transform 0.2s;
  width: 100%;
}

button:hover {
  background-color: #4287f7;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

button:active {
  background-color: #004494;
  transform: translateY(0);
}

.result-section {
  text-align: center;
  margin-top: 40px;
  font-size: 1.5rem;
  font-weight: bold;
  color: #2E3D86;
}

#graph {
  width: 60%;
  height: 500px;
  /* border-radius: 10px;
  box-shadow: 0 0px 8px rgba(0, 0.2, 0.2, 0.3); */
  display: flex;
  align-items: center;
  justify-content: center;
  /* overflow: hidden; */
}

#graph img {
  max-width: 100%;
  max-height: 100%;
  /* object-fit: contain; */
}
</style>
