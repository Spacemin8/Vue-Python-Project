<template>
  <div>
    <logo></logo>
  </div>
</template>
<script>
export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    Login() {
      // Handle login logic here
      console.log("Logging in with:", this.email, this.password);
      // Redirect to another route or perform login actions
    },
  },
};
</script>
<style lang="sass" scoped>
</style>