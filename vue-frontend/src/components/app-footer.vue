<script>
export default {
  data() {
    return {
      tglogo: "src/assets/image/Telegram logo.png",
      twitter: "src/assets/image/twitter logo.png",
      capLogo: "src/assets/image/Capture.PNG",
      send: "src/assets/image/image 10.png",
      logo: "src/assets/image/Logo111.png",
    };
  },
};
</script>

<template>
  <div class="focusfooter-menu">
    <div class="focusfooter-field">
      <div class="focusfooter-mark">
        <div class="logo-size3">
          <img :src="logo" alt="logo" />
        </div>
        <div class="gap2"></div>
        <div class="btn_eff">contact us</div>
      </div>
      <div class="focusfooter-dec">
        <div class="mark-btn">
          <button class="btn-opa">
            <img :src="tglogo" alt="tglogo" />
          </button>
          <button class="btn-opa">
            <img :src="twitter" alt="twitter" />
          </button>
        </div>
        <p>
          FAQ <br />
          Terms & Conditions <br />
          <span>Founded by:</span>
        </p>
        <div class="mark-img">
          <img :src="capLogo" alt="CPALOGO" />
          <img :src="send" alt="SEND" />
        </div>
      </div>
    </div>
    <div class="hr1"></div>
    <div class="focusfooter-des">© 2023 Design. All right reserves</div>
  </div>
</template>

<style scoped>
@import "./app-footer.scss";
</style>
