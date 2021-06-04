<template>
  <div id="container" class="relative h-full overflow-hidden flex w-full min-h-detailBox">
    <div class="text-center flex flex-col items-center justify-center m-auto">
      <p
        class="2xl:text-4xl xl:text-3xl lg:text-2xl md:text-2xl text-3xl font-bold"
      >
        Congratulations
      </p>
      <p class="2xl:text-3xl xl:text-2xl lg:text-xl md:text-lg sm:text-xl">
        You have filled the form successfully
      </p>
    </div>
    <canvas
      id="my-canvas"
      class="absolute m-auto"
    ></canvas>
  </div>
</template>

<script>
import ConfettiGenerator from "../components/confetti";

export default {
  name: "Pagec",
  component: { ConfettiGenerator },
  mounted() {
    // const div = document.getElementById("div");
    const confettiSettings = {
      target: "my-canvas",
      height: "750",
      width: "1024",
    };
    const confetti = new ConfettiGenerator(confettiSettings);
    confetti.render();
    setInterval(function () {
      confetti.clear();
    }, 7500);
  },
};
</script>

