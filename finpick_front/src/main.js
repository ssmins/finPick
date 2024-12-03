import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import vuetify from './plugins/vuetify';
import 'vuetify/styles';

import App from './App.vue'
import router from './router'

const pinia = createPinia() 
pinia.use(piniaPluginPersistedstate)

const app = createApp(App)

// app.use(createPinia())
app.use(pinia)
app.use(router)
app.use(vuetify);

app.mount('#app')
