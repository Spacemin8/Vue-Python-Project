<script>
import logo from "../components/logo.vue";
import menubar from "../components/menubar.vue";
import signup from "../components/signup.vue";
export default {
  components: {
    logo,
    menubar,
    signup,
  },
};
</script>

<template>
  <div>
    <menubar />
    <div class="signup-page">
      <div class="signup-back">
        <logo />
      </div>
      <div class="signup-set">
        <signup />
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "./signuppage.scss";
</style>
