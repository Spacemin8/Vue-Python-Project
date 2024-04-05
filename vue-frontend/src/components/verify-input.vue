<script>
import axios from "axios";
export default {
  data() {
    return {
      codeInputs: ["", "", "", "", "", ""],
    };
  },
  methods: {
    handleInput(index) {
      if (
        this.codeInputs[index].length === 1 &&
        index < this.codeInputs.length - 1
      ) {
        this.$refs.codeInputs[index + 1].focus();
      }
    },
    handleKeyup(index, event) {
      if (event.key === "Backspace" && index > 0) {
        if (this.codeInputs[index].length === 0) {
          this.$refs.codeInputs[index - 1].focus();
        }
      }
    },
    async verifyCode() {
      const hasEmptyInput = this.codeInputs.some((val) => val === "");
      if (hasEmptyInput) {
        alert("Input correctly!");
        return;
      }
      const code = this.codeInputs.join("");
      const post_data = {
        email: localStorage.getItem("email"),
        verification_code: code,
      };
      console.log(post_data);
      const response = await axios.post(
        "http://localhost:8000/user/signup/verify/",
        post_data
      );
      console.log(response.data);
      if (response.data.message === "success verified") {
        localStorage.removeItem("email");
        this.$router.push("/signup/setpassword");
      } else {
        alert(response.data.message);
        return;
      }
    },
  },
};
</script>

<template>
  <div class="verify">
    <div class="verify-group">
      <input
        v-for="(div, index) in codeInputs"
        :key="index"
        type="text"
        maxlength="1"
        class="in-element"
        v-model="codeInputs[index]"
        @input="handleInput(index)"
        @keyup="handleKeyup(index, $event)"
        ref="codeInputs"
      />
    </div>
  </div>
  <div class="bar">
    <button @click="verifyCode" class="button3 but-style">Proceed</button>
  </div>
</template>

<style scoped lang="sass">
@import "./verify-input.scss"
</style>