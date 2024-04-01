<script>
export default {
  methods: {
    handlelogin() {
      this.$router.push("/login");
    },
    handlesignup() {
      this.$router.push("/signup");
    },
  },
};
</script>

<template>
  <div class="menu-bar">
    <div class="logo-size1"></div>
    <div class="button-container">
      <button class="btn-login" @click="handlelogin">Log in</button>
      <button class="btn-signup btn-eff" @click="handlesignup">Sign up</button>
    </div>
  </div>
</template>

<style scoped>
@import "./app-menu.scss";
</style>
