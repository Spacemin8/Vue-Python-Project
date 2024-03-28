<script>
import logo from "../components/logo.vue";
import menubar from "../components/menubar.vue";
import login from "../components/login.vue";
export default {
  components: {
    logo,
    menubar,
    login,
  },
};
</script>

<template>
  <div>
    <menubar />
    <div class="Login-page">
      <div class="Login-back">
        <logo />
      </div>
      <div class="Login-set">
        <login />
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "./loginpage.scss";
</style>
