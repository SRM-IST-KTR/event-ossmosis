<template>
  <button
    :class="
      check && disable
        ? 'py-2 px-4 bg-gray-500 text-white font-semibold rounded-lg shadow-md focus:outline-none cursor-not-allowed'
        : 'py-2 px-4 bg-black text-white font-semibold rounded-lg shadow-md focus:outline-none'
    "
  >
    {{ button.name }}
  </button>
</template>

<script>
export default {
  name: "Button",
  props: ["button", "disable", "check"],
};
</script>

<style></style>
