<script>
import http from "../http";
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
      mail: "src/assets/image/Icon2.png",
      email: "",
      password: "",
    };
  },
  methods: {
    handlesignup() {
      this.$router.push("/signup");
    },
    handledashboard() {
      this.$router.push("/dashboard");
    },
    login() {
      const credentials = {
        email: this.email,
        password: this.password,
      };
      console.log(credentials);
      http
        .post("http://127.0.0.1:8000/user/login/", credentials)
        .then((response) => {
          const accesstoken = response.data.accesstoken;
          const refreshtoken = response.data.refreshtoken;
          console.log(accesstoken);
          console.log("Login successful", response.data);
          this.handledashboard();
          localStorage.setItem("accesstoken", accesstoken);
          localStorage.setItem("refreshtoken", refreshtoken);
        })
        .catch((error) => {
          console.log("Login error", error.response.data);
        });
    },
  },
};
</script>

<template>
  <div class="login-container">
    <div class="title">
      <p class="text">Welcome Back</p>
      <p class="text1">
        Go ahead and log in. Get acces to your incredible
        <br />
        account!
      </p>
    </div>
    <form class="log-in">
      <vueinput
        :icon="mail"
        type="email"
        placeholder="Enter email"
        v-model="email"
      />
      <vueinput
        :icon="passkey"
        type="password"
        placeholder="Phone Number (Optional)"
        v-model="password"
      />
      <button type="button" class="button3 but-style" @click="login">
        Log In
      </button>
      <button class="btnlog but-style" @click="handlesignup">
        I forgot my password
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
@import "./login.scss";
</style>
