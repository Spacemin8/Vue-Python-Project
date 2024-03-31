<script>
import logo from "../components/logo.vue";
import appmenu from "../components/app-menu.vue";
import verifyemail from "../components/verify-email.vue";
export default {
  components: {
    logo,
    appmenu,
    verifyemail,
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
        <verifyemail />
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "./Verify-email.scss";
</style>
