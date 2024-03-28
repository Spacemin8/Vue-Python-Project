<script>
export default {
  props: {
    icon: {
      type: String,
      required: true,
    },
    type: String,
    placeholder: String,
  },
  value: "",
};
</script>

<template>
  <div class="input-group">
    <div class="symbol">
      <img :src="icon" alt="src" />
    </div>
    <input
      :type="type"
      class="input-control"
      required
      v-model="value"
      :placeholder="placeholder"
    />
  </div>
</template>

<style scoped lang="scss">
@import "./input";
</style>