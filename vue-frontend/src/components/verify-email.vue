<script>
import verifyinput from "./verify-input.vue";
export default {
  components: {
    verifyinput,
  },
  data() {
    return {
      Ico1: "src/assets/image/Vector.png",
      passkey: "src/assets/image/Icon4.png",
      Ico2: "src/assets/image/metamask-icon logo.png",
      Ico3: "src/assets/image/twitter logo1.png",
      Ico4: "src/assets/image/Group.png",
    };
  },
};
</script>

<template>
  <div class="login-container">
    <div class="title">
      <p class="text">Verify Your Email</p>
      <p class="text1">
        We have send you a code. Check your email<br />
        and input the code to procced
      </p>
    </div>
    <form class="verify">
      <verifyinput :icon="passkey" type="password" :v-model="password" />
    </form>
    <div class="bar">
      <button type="submit" class="button3 but-style">Proceed</button>
    </div>
  </div>
</template>

<style scoped>
@import "./verify-email.scss";
</style>
