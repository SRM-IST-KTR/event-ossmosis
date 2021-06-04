<template>
  <button
    class="
      w-full
      mx-2
      first:ml-0
      last:mr-0
      py-2
      text-white
      font-semibold
      rounded-lg
      shadow-md
      focus:outline-none
    "
    :disabled="disable"
    :class="check && disable ? 'bg-gray-500 cursor-not-allowed' : 'bg-black'"
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
