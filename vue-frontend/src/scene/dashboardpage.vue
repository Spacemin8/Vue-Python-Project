<script>
import appheader from "../components/app-header.vue";
import focus from "../components/focus.vue";
import appfooter from "../components/app-footer.vue";
export default {
  components: {
    appheader,
    focus,
    appfooter,
  },
};
</script>

<template>
  <div class="dashboard-back">
    <div class="dashbar">
      <appheader />
    </div>
    <div>
      <focus />
    </div>
    <div>
      <appfooter />
    </div>
  </div>
</template>

<style scoped>
@import "./dashboardpage.scss";
</style>
