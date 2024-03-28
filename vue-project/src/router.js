// router.js
import Vue from 'vue';
import Router from 'vue-router';
import Login from './components/Login.vue';
import Signup from './components/Signup.vue';

Vue.use(Router);

export default new Router({
  routes: [
    { path: '/login', component: Login },
    { path: '/signup', component: Signup },
    // Redirect to login page as default
    { path: '/', redirect: '/login' }
  ]
});
