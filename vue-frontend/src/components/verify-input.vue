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
  <div class="verify-group">
    <div class="in-style">
      <input
        :type="text"
        class="in-element"
        required
        v-model="value"
        maxlength="1"
      />
      <div class="divider"></div>
    </div>
    <div class="in-style">
      <input
        :type="text"
        class="in-element"
        required
        v-model="value"
        maxlength="1"
      />
      <div class="divider"></div>
    </div>
    <div class="in-style">
      <input
        :type="text"
        class="in-element"
        required
        v-model="value"
        maxlength="1"
      />
      <div class="divider"></div>
    </div>
    <div class="in-style">
      <input
        :type="text"
        class="in-element"
        required
        v-model="value"
        maxlength="1"
      />
      <div class="divider"></div>
    </div>
    <div class="in-style">
      <input
        :type="text"
        class="in-element"
        required
        v-model="value"
        maxlength="1"
      />
      <div class="divider"></div>
    </div>
    <div class="in-style">
      <input
        :type="text"
        class="in-element"
        required
        v-model="value"
        maxlength="1"
      />
      <div class="divider"></div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import "./verify-input";
</style>