<template>
  <button
    class="
      py-2
      px-4
      bg-black
      text-white
      font-semibold
      rounded-lg
      shadow-md
      focus:outline-none
    "
  >
    {{ button.name }}
  </button>
</template>

<script>
export default {
  name: "Button",
  props: ["button"],
};
</script>

<style></style>
