<script>
import http from "../http";
import focuspoint from "./focuspoint.vue";
import modal from "./modal.vue";
import deletemodal from "./delete-modal.vue";
export default {
  components: { focuspoint, modal, deletemodal },
  data() {
    return {
      focusPoints: [],
      apiUrl: "http://127.0.0.1:8000/product",
      editingId: 0,
    };
  },
  created() {
    this.sendLoadReq();
  },
  methods: {
    showCreateModal() {
      this.editingId = 0;
      this.$refs.myModal.createItem();
    },
    showUpdateModal(item) {
      this.editingId = item.id;
      this.$refs.myModal.editItem(item);
    },
    sendCreateData(item) {
      http
        .post(`${this.apiUrl}/create/`, item)
        .then((response) => {
          // Handle success
          item.id = response.data.id;
          console.log("Item stored in database:", response.data, item.id);
        })
        .catch((error) => {
          // Handle error
          console.error("Error storing item:", error);
        });
    },
    sendLoadReq() {
      // console.log("here");
      http
        .get(`${this.apiUrl}/load/`)
        .then((response) => {
          // Extract only title and description fields from the response data
          this.focusPoints = response.data;
          if (this.focusPoints.length !== 0) {
            const para = document.getElementById("desc");
            console.log("data loaded");
            para.classList.add("hidden");
          } else {
            para.classList.remove("hidden");
          }
        })
        .catch((error) => {
          // Handle error
          console.error("Error fetching data:", error);
        });
    },
    sendUpdateData(item) {
      http
        .put(`${this.apiUrl}/update/${this.editingId}/`, item)
        .then((response) => {
          // Update the item in the focusPoints array
          const index = this.focusPoints.findIndex(
            (focuspoint) => focuspoint.id === this.editingId
          );
          console.log(index);
          this.focusPoints[index].title = item.title;
          this.focusPoints[index].description = item.description;
        })
        .catch((error) => {
          console.error("Error updating item:", error);
        });
    },
    sendDeleteId(index) {
      http
        .delete(`${this.apiUrl}/delete/${index}/`)
        .then(() => {
          this.focusPoints.splice(index, 1);
          if (this.focusPoints.length == 0) {
            const para = document.getElementById("desc");
            para.classList.remove("hidden");
          }
        })
        .catch((error) => {
          console.error("Error deleting item:", error);
        });
    },

    handleCreate(item) {
      console.log("Item created:", item);
      this.focusPoints.push(item);
      // Handle the creation logic here, such as sending data to an API
      this.sendCreateData(item);
      if (this.focusPoints.length !== 0) {
        const para = document.getElementById("desc");
        console.log("data loaded");
        para.classList.add("hidden");
      }
    },
    handleUpdate(item) {
      this.sendUpdateData(item);
    },
    handleDelete(id, index) {
      console.log({ id, index });
      // Confirm deletion before proceeding
      if (confirm("Are you sure you want to delete this item?")) {
        this.sendDeleteId(id);
        this.focusPoints.splice(index, 1);
      }
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
        <button type="button" class="btn-add" @click="showCreateModal">
          + Add new focus point
        </button>
      </div>
      <div class="hr"></div>
      <div class="focus-field">
        <modal
          @create="handleCreate"
          @cancel="handleCancel"
          @update="handleUpdate"
          ref="myModal"
        />
        <focuspoint
          v-for="(item, index) in focusPoints"
          :key="index"
          :title="item.title"
          :description="item.description"
          :id="item.id"
          @edit="showUpdateModal(item)"
          @delete="handleDelete(item.id, index)"
        />
        <p id="desc">
          No Focus Points added <br />
          <span>
            Focus Point to start you Journey towards <br />
            self-development !
          </span>
        </p>
        <button class="more-button">Load More</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "./focus.scss";
</style>
