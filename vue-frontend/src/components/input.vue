<script setup>
import { defineModel } from "vue";
const props = defineProps({
  icon: {
    type: String,
    required: true,
  },
  type: String,
  placeholder: String,
});
const value = defineModel();
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
      :placeholder="placeholder"
      v-model="value"
    />
  </div>
</template>

<style scoped lang="scss">
@import "./input";
</style>