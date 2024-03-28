import { createRouter, createWebHistory } from 'vue-router';
import loginpage from './scene/loginpage.vue';
import signuppage from './scene/signuppage.vue';
import resetpasspage from './scene/resetpasspage.vue';
import dashboardpage from './scene/dashboardpage.vue';
const routes = [
  {
    path: '/login',
    name: 'loginpage',
    component: loginpage
  },
  {
    path: '/signup',
    name: 'signuppage',
    component: signuppage
  },
  {
    path: '/reset',
    name: 'resetpasspage',
    component: resetpasspage
  },
  {
    path: '/dashboard',
    name: 'dashboardpage',
    component: dashboardpage
  }
  // Add more routes as needed
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
