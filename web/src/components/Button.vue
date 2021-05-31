<template>
  <button
    class="
      py-2
      px-4
      bg-green-500
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
