<script>
import logo from "../components/logo.vue";
import appmenu from "../components/app-menu.vue";
import resetpass from "../components/resetpass.vue";
export default {
  components: {
    logo,
    appmenu,
    resetpass,
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
        <resetpass />
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "./resetpasspage.scss";
</style>
