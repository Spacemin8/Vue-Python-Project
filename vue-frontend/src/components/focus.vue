<script>
import focuspoint from "./focuspoint.vue";
import modal from "./modal.vue";

export default {
  components: { focuspoint, modal },
  data() {
    return {
      focusPoints: [],
    };
  },
  methods: {
    showModal() {
      this.$refs.myModal.openModal();
    },
    handleCreate(item) {
      console.log("Item created:", item);
      this.focusPoints.push(item);

      // Handle the creation logic here, such as sending data to an API
    },

    handleCancel() {
      console.log("Modal cancelled");
      // Handle the cancel logic here
    },
  },
};
</script>

<template>
  <div>
    <h1>Your Focus</h1>
  </div>
  <div class="focus-menu">
    <div class="focus-title">
      <button>In progress</button>
      <button>completed</button>
    </div>
    <div class="focus-main">
      <div class="focus-head">
        <div class="tex-g">
          <h6>Focus Points</h6>
          <div class="tex-1">
            <p>12, 254</p>
            <span>points</span>
          </div>
        </div>
        <button type="button" class="btn-add" @click="showModal">
          + Add new focus point
        </button>
      </div>
      <div class="hr"></div>
      <div class="focus-field">
        <modal @create="handleCreate" @cancel="handleCancel" ref="myModal" />
        <focuspoint
          v-for="(item, index) in focusPoints"
          :key="index"
          :title="item.title"
          :description="item.description"
        />
        <p id="desc">
          No Focus Points added <br />
          <span>
            Focus Point to start you Journey towards <br />
            self-development !
          </span>
        </p>
        <button class="morebutton">Load More</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "./focus.scss";
</style>
