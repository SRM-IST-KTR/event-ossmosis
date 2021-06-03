<template>
  <div class="mt-32 lg:mt-20">
    <h1 class="font-bold text-white text-center text-5xl mb-1">OSSmosis</h1>
    <h3 class="font-thin  text-gray-300 text-center text-xl mb-5">Is your project OSS ready?</h3>

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


    <div class="mb-8">
      <Details />

      <div class="flex justify-center items-center m-5 text-white">
        <ul class="text-white text-xl">
          <li class="flex">
            <ClockIcon class="w-7 h-7" /><span class="mx-4">Time</span>
          </li>
        </ul>
      </div>
    </div>
    <Footer class="pb-8 hidden lg:flex w-8/12 mx-auto"/>
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
