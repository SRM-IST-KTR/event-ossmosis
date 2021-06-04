<template>
  <div class="relative h-screen overflow-hidden">
    <div class="text w-11/12">
      <div class="flex flex-col items-center justify-center">
        <p class="text-7xl mb-4">404</p>
        <button
          class="
            text-2xl
            border-white border-2 border-opacity-25
            rounded-lg
            p-2
          "
        >
          <a href="/"> Go back home </a>
        </button>
      </div>
    </div>
    <div class="space">
      <div class="orbit-1"></div>
      <div class="moon-1 sm"></div>
      <div class="orbit-2"></div>
      <div class="moon-2 sm"></div>
      <div class="orbit-3"></div>
      <div class="moon-3"></div>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    setInterval(() => this.$router.push("/"), 15000);
  },
};
</script>

<style>
html,
body {
  background: #0d1117;
  width: 100%;
  height: 100%;
  letter-spacing: 0.1em;
  font-smooth: antialiased;
}
#app {
  background: #0d1117 !important;
}
.space {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 50%;
  left: 50%;
}
.space > div {
  position: absolute;
}
.text {
  z-index: 100;
  color: #fff;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.space .text h1 {
  font-size: 140px;
  line-height: 0.01em;
}
.space div[class^="moon"] {
  background: url("https://i.imgur.com/0i18KL5.png");
  background-size: 60px;
  width: 60px;
  height: 60px;
  z-index: 4;
}
.space div[class^="moon"].sm {
  background-size: 30px;
  width: 30px;
  height: 30px;
}
.space .moon-1 {
  margin-top: -15px;
  margin-left: -15px;
  background-size: 50% auto;
  animation: orbit1 15s linear infinite;
}
.space .moon-2 {
  margin-top: -15px;
  margin-left: -15px;
  animation: orbit2 -6s 18s linear infinite;
}
.space .moon-3 {
  margin-top: -30px;
  margin-left: -30px;
  animation: orbit3 -12s 22s linear infinite;
}
.space .orbit-1 {
  margin-top: -250px;
  margin-left: -250px;
  width: 500px;
  height: 500px;
  border-radius: 250px;
  background: #3f5468;
  z-index: 3;
}
.space .orbit-2 {
  margin-top: -340px;
  margin-left: -340px;
  width: 680px;
  height: 680px;
  border-radius: 340px;
  background: #3a4f64;
  z-index: 2;
}
.space .orbit-3 {
  margin-top: -395px;
  margin-left: -395px;
  width: 790px;
  height: 790px;
  border-radius: 395px;
  background: #374c61;
  z-index: 1;
}
@keyframes orbit1 {
  from {
    transform: rotate(0deg) translateX(250px);
  }
  to {
    transform: rotate(360deg) translateX(250px);
  }
}
@keyframes orbit2 {
  from {
    transform: rotate(0deg) translateX(340px);
  }
  to {
    transform: rotate(360deg) translateX(340px);
  }
}
@keyframes orbit3 {
  from {
    transform: rotate(0deg) translateX(395px);
  }
  to {
    transform: rotate(360deg) translateX(395px);
  }
}
</style>
