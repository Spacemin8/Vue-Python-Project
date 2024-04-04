<script>
export default {
  data() {
    return {
      isVisible: false,
      title: "",
      description: "",
      editMode: false,
      currentItem: null,
    };
  },
  methods: {
    createOrUpdateItem() {
      // Emit an event with the new item data
      if (this.editMode) {
        // Update logic
        this.$emit("update", {
          ...this.currentItem,
          title: this.title,
          description: this.description,
        });
      } else {
        this.$emit("create", {
          title: this.title,
          description: this.description,
        });
      }
      this.closeModal();
    },
    cancel() {
      // Emit an event for cancel
      this.$emit("cancel");
      this.closeModal();
    },
    editItem(item) {
      this.editMode = true;
      this.currentItem = item;
      this.title = item.title;
      this.description = item.description;
      this.openModal();
    },
    createItem() {
      this.editMode = false;
      this.openModal();
    },
    closeModal() {
      this.isVisible = false;
      this.title = "";
      this.description = "";
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
        <h2>{{ editMode ? "Edit" : "Create" }} FocusPoints</h2>
        <div appearance="fill" class="form-field">
          <label for="title">Title</label>
          <input
            matInput
            placeholder="Enter title"
            id="title"
            v-model="title"
          />
        </div>
        <div class="form-field">
          <label for="description">Description</label>
          <textarea
            id="description"
            v-model="description"
            placeholder="Enter description"
            rows="5"
            cols="100"
          ></textarea>
        </div>
        <div>
          <button @click="createOrUpdateItem">
            {{ editMode ? "Edit" : "Create" }}
          </button>
          <button @click="cancel">Cancel</button>
        </div>
      </div>
    </div>
  </transition>
</template>

<style scoped>
@import "./modal.scss";
</style>
