<script>
import vueinput from "./input.vue";
export default {
  components: {
    vueinput,
  },
  data() {
    return {
      Ico1: "src/assets/image/Vector.png",
      passkey: "src/assets/image/Icon4.png",
      Ico2: "src/assets/image/metamask-icon logo.png",
      Ico3: "src/assets/image/twitter logo1.png",
      Ico4: "src/assets/image/Group.png",
      password: "",
      Confirm_password: "",
    };
  },
};
</script>

<template>
  <div class="login-container">
    <div class="title">
      <p class="text">Create Password</p>
      <p class="text1">
        Set your security password. Recommended <br />
        usage of at least 1 number, 1 uppercase letter<br />
        and 1 special character
      </p>
    </div>
    <form class="log-in">
      <vueinput
        :icon="passkey"
        type="password"
        placeholder="password"
        :v-model="password"
      />
      <vueinput
        :icon="passkey"
        type="password"
        placeholder="Confirm password"
        :v-model="Confirm_password"
      />
      <button type="submit" class="button3 but-style">Submit</button>
      <button class="btnreset but-style" @click="handlelogin()">
        I already have an account
      </button>
    </form>
    <div class="browser">
      <button class="button-style">
        <img :src="Ico1" alt="" />
      </button>
      <button class="button-style">
        <img :src="Ico2" class="metamask" alt="" />
        <img :src="Ico4" class="instegram" alt="" />
      </button>
      <button class="button-style">
        <img :src="Ico3" alt="" />
      </button>
    </div>
  </div>
</template>

<style scoped>
@import "./resetpass.scss";
</style>
