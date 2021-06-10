<template>
  <div
    id="container"
    class="relative h-full overflow-hidden flex w-full min-h-detailBox"
  >
    <div class="text-center flex flex-col items-center justify-center m-auto">
      <p class="2xl:text-3xl xl:text-2xl lg:text-xl md:text-lg sm:text-xl p-4">
        That's a wrap for <b>OSSmosis</b>!<br />
        Follow us on our socials to stay tuned for future events!
      </p>
    </div>
    <canvas id="my-canvas" class="absolute m-auto"></canvas>
  </div>
</template>

<script>
export default {
  name: "Pagec",
};
</script>
