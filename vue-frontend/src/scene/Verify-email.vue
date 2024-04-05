<script>
import logo from "../components/logo.vue";
import appmenu from "../components/app-menu.vue";
import verifyinput from "../components/verify-input.vue";
export default {
  components: {
    logo,
    appmenu,
    verifyinput,
  },
};
</script>

<template>
  <div>
    <appmenu />
    <div class="Login-page">
      <div class="Login-back">
        <logo />
      </div>
      <div class="Login-set">
        <div class="login-container">
          <div class="title">
            <p class="text">Verify Your Email</p>
            <p class="text1">
              We have send you a code. Check your email<br />
              and input the code to procced
            </p>
          </div>
          <verifyinput />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "./verify-email.scss";
</style>
