<script>
import focusbar from "../components/focusbar.vue";
import focus from "../components/focus.vue";
import focusfooter from "../components/focusfooter.vue";
export default {
  components: {
    focusbar,
    focus,
    focusfooter,
  },
};
</script>

<template>
  <div class="dashboard-back">
    <div class="dashbar">
      <focusbar />
    </div>
    <div>
      <focus />
    </div>
    <div>
      <focusfooter />
    </div>
  </div>
</template>

<style scoped>
@import "./dashboardpage.scss";
</style>
