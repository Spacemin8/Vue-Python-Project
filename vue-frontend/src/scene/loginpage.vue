<script>
import logo from "../components/logo.vue";
import appmenu from "../components/app-menu.vue";
import login from "../components/login.vue";
export default {
  components: {
    logo,
    appmenu,
    login,
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
        <login />
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "./loginpage.scss";
</style>
