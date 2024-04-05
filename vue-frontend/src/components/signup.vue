<script>
import vueinput from "./input.vue";
import axios from "axios";
export default {
  components: {
    vueinput,
  },
  data() {
    return {
      Ico1: "src/assets/image/Vector.png",
      Ico2: "src/assets/image/metamask-icon logo.png",
      Ico3: "src/assets/image/twitter logo1.png",
      Ico4: "src/assets/image/Group.png",
      mail: "src/assets/image/Icon2.png",
      ph: "src/assets/image/Icon3.png",
      user: "src/assets/image/Icon1.png",
      username: "",
      email: "",
      phone: "",
    };
  },
  methods: {
    handleVerify() {
      this.$router.push("/signup/verify");
    },
    signup() {
      const userData = {
        username: this.username,
        email: this.email,
        phone: this.phone,
      };
      axios
        .post("http://127.0.0.1:8000/user/signup/", userData)
        .then((response) => {
          console.log("Signup successful", response.data);
          const email = userData.email;
          const username = userData.username;
          localStorage.setItem("email", email);
          localStorage.setItem("username", username);
          this.handleVerify();
        })
        .catch((error) => {
          console.error("Signup error", error.response.data);
        });
    },
  },
};
</script>
<template>
  <div class="signup-container">
    <div class="title">
      <p class="text">Create Account</p>
      <p class="text1">
        Provide necessary information to proceed <br />
        with registration or sign up with social media
      </p>
    </div>
    <div class="sign-up">
      <vueinput
        :icon="user"
        type="text"
        placeholder="Enter username"
        v-model="username"
      />
      <vueinput
        :icon="mail"
        type="mail"
        placeholder="Enter email"
        v-model="email"
      />
      <vueinput
        :icon="ph"
        type="number"
        placeholder="Phone Number (Optional)"
        v-model="phone"
      />
      <button type="button" class="button3 but-style" @click="signup">
        Proceed
      </button>
      <button class="btn-sign but-style" @click="handlelogin">
        I already have an account
      </button>
    </div>
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
@import "./signup.scss";
</style>
