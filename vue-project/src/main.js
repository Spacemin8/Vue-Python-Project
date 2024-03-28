import './assets/main.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

new Vue({
  router, // short for `router: router`
  render: (h) => h(App)
}).$mount('#app');
