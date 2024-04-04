<script>
export default {
  props: {
    id: Number,
    title: String,
    description: String,
  },
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
    onEdit() {
      this.$emit("edit", {
        id: this.$props.id,
        title: this.$props.title,
        description: this.$props.description,
      });
      console.log(this.$props.id, this.$props.title);
    },
    onDelete() {
      this.$emit("delete");
    },
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
