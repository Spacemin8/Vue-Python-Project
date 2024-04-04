<script>
export default {
  data() {
    return {
      isVisible: false,
    };
  },
  methods: {
    deleteitem() {
      this.$emit("delete");
      this.closeModal();
    },
    cancel() {
      // Emit an event for cancel
      this.$emit("cancel");
      this.closeModal();
    },
    closeModal() {
      this.isVisible = false;
    },
    openModal() {
      this.isVisible = true;
    },
  },
};
</script>

<template>
  <transition name="modal">
    <div class="modal" v-if="isVisible">
      <div class="modal-content">
        <h2>Delete FocusPoints</h2>
        <div>
          <h4>Do you really delete focuspoint?</h4>
        </div>
        <div>
          <button @click="deleteitem">Delete</button>
          <button @click="cancel">Cancel</button>
        </div>
      </div>
    </div>
  </transition>
</template>

<style scoped>
@import "./delete-modal.scss";
</style>
