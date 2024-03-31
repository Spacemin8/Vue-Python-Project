<script>
import logo from "../components/logo.vue";
import appmenu from "../components/app-menu.vue";
import signup from "../components/signup.vue";
export default {
  components: {
    logo,
    appmenu,
    signup,
  },
};
</script>

<template>
  <div>
    <appmenu />
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
