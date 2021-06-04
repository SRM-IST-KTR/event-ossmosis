<template>
  <div
    class="lg:w-7/12 w-full flex flex-col justify-between items-center h-full"
  >
    <div>
      <div class="w-full lg:hidden text-center">
        <a
          class="
            text-md
            font-extrabold
            uppercase
            py-3
            shadow-lg
            rounded
            block
            leading-normal
            cursor-pointer
            text-gray-600
            bg-white
          "
          href="#form"
        >
          Apply Now!
        </a>
      </div>
      <Details />
    </div>

    <div class="w-full">
      <div class="flex justify-center items-center m-5 text-white">
        <ClockIcon class="text-white text-7xl w-7 h-7" />
        <span class="mx-4">Deadline : 12 June 2021, 11:59 PM</span>
      </div>
      <Footer class="pb-8 lg:pb-0 hidden lg:flex w-8/12 mx-auto" />
    </div>
  </div>
</template>

<script>
import { ClockIcon } from "@heroicons/vue/outline";
import Details from "./Details";
import Footer from "../components/Footer";

export default {
  name: "Left",
  components: {
    ClockIcon,
    Details,
    Footer,
  },
};
</script>

<style></style>
