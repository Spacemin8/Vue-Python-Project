<script>
import vueinput from "./input.vue";
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
      phone: "src/assets/image/Icon3.png",
      user: "src/assets/image/Icon1.png",
      username: "",
      email: "",
      password: "",
    };
  },
  methods: {
    handlelogin() {
      this.$router.push("/login");
    },
    signup() {
      const userData = {
        username: this.username,
        email: this.email,
        password: this.password,
      };
      axios
        .post("http://localhost:8000/signup/", userData)
        .then((response) => {
          console.log("Signup successful", response.data);
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
    <form onsubmit="signup()" class="sign-up">
      <vueinput
        :icon="user"
        type="text"
        placeholder="Enter username"
        :v-model="username"
      />
      <vueinput
        :icon="mail"
        type="mail"
        placeholder="Enter email"
        :v-model="mail"
      />
      <vueinput
        :icon="phone"
        type="text"
        placeholder="Phone Number (Optional)"
        :v-model="password"
      />
      <button type="submit" class="button3 but-style">Proceed</button>
      <button class="btn-sign but-style" @click="handlelogin">
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
@import "./signup.scss";
</style>
