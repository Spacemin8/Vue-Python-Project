<script>
export default {
  data() {
    return {
      Edit: "src/assets/image/Frame 1000003654.png",
      save: "src/assets/image/Frame 1000003663.png",
      del: "src/assets/image/Frame 1000003660.png",
      user2: "src/assets/image/users-02.png",
      fizz: "src/assets/image/FIZZ.png",
    };
  },
  methods: {
    onEdit() {},
    onDelete() {},
  },
  props: {
    title: String,
    description: String,
  },
};
</script>

<template>
  <div class="focuspoint">
    <div>
      <span>{{ title }}</span>
    </div>
    <div>
      <span>{{ description }}</span>
    </div>
    <button id="user">
      <img :src="user2" alt="" />
      1234
    </button>
    <button id="fizz"><img :src="fizz" alt="" />1000</button>
    <img :src="Edit" alt="" id="edit" @click="onEdit()" />
    <img :src="save" alt="" id="save" />
    <img :src="del" alt="" id="del" @click="onDelete()" />
  </div>
</template>

<style scoped>
@import "./focuspoint.scss";
</style>
