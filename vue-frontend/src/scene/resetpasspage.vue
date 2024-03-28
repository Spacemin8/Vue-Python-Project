<script>
import logo from "../components/logo.vue";
import menubar from "../components/menubar.vue";
import resetpass from "../components/resetpass.vue";
export default {
  components: {
    logo,
    menubar,
    resetpass,
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
        <resetpass />
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "./resetpasspage.scss";
</style>
