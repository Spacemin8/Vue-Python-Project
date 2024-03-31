import { createRouter, createWebHistory } from 'vue-router';
import loginpage from './scene/loginpage.vue';
import signuppage from './scene/signuppage.vue';
import resetpasspage from './scene/resetpasspage.vue';
import dashboardpage from './scene/dashboardpage.vue';
import verifyemail from './scene/Verify-email.vue';
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
    path: '/signup/verifyemail',
    name: 'verifyemail',
    component: verifyemail
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
