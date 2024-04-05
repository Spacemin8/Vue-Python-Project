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
    path: '/signup/verify',
    name: 'verify',
    component: verifyemail
  },
  {
    path: '/signup/setpassword',
    name: 'resetpasspage',
    component: resetpasspage
  },
  {
    path: '/dashboard',
    name: 'dashboardpage',
    component: dashboardpage,
    meta: {
      requireAuth: true
    }
  }

  // Add more routes as needed
];

const router = createRouter({
  history: createWebHistory(),
  routes
});
export default router;
router.beforeEach((to, from, next) => {
  const accessToken = localStorage.getItem('accesstoken');

  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // This route requires authentication, check if the token is present
    if (accessToken) {
      // There is a token, continue to the route
      next();
    } else {
      // No token found, redirect to the login page
      next({
        path: '/login',
        query: { redirect: to.fullPath } // Store the full path to redirect back after login
      });
    }
  } else if (to.path === '/login' && accessToken) {
    // If trying to access the login page while already logged in, redirect to the dashboard
    next('/dashboard');
  } else {
    // Make sure to always call next()!
    next();
  }
});
