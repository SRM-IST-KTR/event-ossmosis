<template>
  <div id="container" class="relative h-full overflow-hidden flex w-full">
    <div class="text-center flex flex-col items-center justify-center">
      <p
        class="
          2xl:text-4xl
          xl:text-3xl
          lg:text-2xl
          md:text-2xl
          text-3xl
          font-bold
        "
      >
        Congratulations
      </p>
      <p class="2xl:text-3xl xl:text-2xl lg:text-xl md:text-lg sm:text-xl">
        You have filled the form successfully
      </p>
    </div>
    <canvas
      id="my-canvas"
      class="absolute top-0 bottom-0 left-0 right-0"
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
      height:"500",
      width:"500"
    };
    const confetti = new ConfettiGenerator(confettiSettings);
    confetti.render();
    setInterval(function () {
      confetti.clear();
    }, 5000);
  },
};
</script>

