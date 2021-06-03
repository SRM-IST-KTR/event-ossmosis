<template>
  <div id="container" height="500px" weight="500px">
    <div id="overlay" class="text-center">
      <p
        class="
          2xl:text-5xl
          xl:text-4xl
          lg:text-3xl
          md:text-2xl
          sm:text-3xl
          font-bold
        "
      >
        Congratulations
      </p>
      <p class="2xl:text-3xl xl:text-2xl lg:text-xl md:text-lg sm:text-xl">
        You have filled the form successfully
      </p>
    </div>
    <canvas id="my-canvas"></canvas>
  </div>
</template>

<script>
import ConfettiGenerator from "../components/confetti";

export default {
  name: "Pagec",
  component: { ConfettiGenerator },
  mounted() {
    const confettiSettings = {
      target: "my-canvas",
      width: "450",
      height: "450",
    };
    const confetti = new ConfettiGenerator(confettiSettings);
    confetti.render();
    setInterval(function () {
      confetti.clear();
    }, 5000);
  },
};
</script>

<style>
#container {
  position: relative;
}
#container canvas {
  position: relative;
}
#overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
