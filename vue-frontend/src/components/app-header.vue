<script>
export default {
  data() {
    return {
      Homepage: "src/assets/image/Homepage.png",
      FocusPoint: "src/assets/image/FocusPoint.png",
      Rewards: "src/assets/image/Rewards.png",
      Profile: "src/assets/image/Profile.png",
      Mystatistic: "src/assets/image/My statistic.png",
      Pricing: "src/assets/image/Pricing.png",
      Logout: "src/assets/image/Logout.png",
      butmenu: "src/assets/image/menu-04.png",
    };
  },
  handleLogout() {
    this.$router.push("/signup");
  },
};
</script>

<template>
  <div class="focus-bar">
    <div class="logo-size2"></div>
    <div class="btn-container">
      <button class="btn-Focus">
        <img :src="Homepage" alt="home" />
        <p class="btn-p">Homepage</p>
      </button>
      <button class="btn-Focus btn-underline">
        <img :src="FocusPoint" alt="focuspoint" />
        <p class="btn-p">Focus Point</p>
      </button>
      <button class="btn-Focus">
        <img :src="Rewards" alt="rewards" />
        <p class="btn-p">Rewards</p>
      </button>
      <button class="btn-Focus">
        <img :src="Profile" alt="profile" />
        <p class="btn-p">Profile</p>
      </button>
      <button class="btn-Focus">
        <img :src="Mystatistic" alt="mystatistic" />
        <p class="btn-p">My statistic</p>
      </button>
      <button class="btn-Focus">
        <img :src="Pricing" alt="pricing" />
        <p class="btn-p">Pricing</p>
      </button>
    </div>
    <div class="btn-log">
      <button class="btn-Focus">
        <img :src="Logout" alt="logout" />
        <p class="btn-p">Log out</p>
      </button>
    </div>
    <div class="btn-menu">
      <img :src="butmenu" alt="butmenu" @click="handleLogout" />
    </div>
  </div>
</template>

<style scoped>
@import "./app-header.scss";
</style>
