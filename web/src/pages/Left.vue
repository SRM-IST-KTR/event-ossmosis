<template>
  <div class="mt-40 lg:mt-0">
    <h1 class="font-bold text-white text-5xl mb-3">OSSmosis</h1>

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

    <div class="space-x-4 flex justify-center items-center">
      <a href="https://github.com/SRM-IST-KTR"
        ><Octocat class="w-10 h-10 text-white inline-block"
      /></a>
      <a href="https://twitter.com/githubsrm"
        ><Twitter class="w-10 h-10 text-white inline-block"
      /></a>
      <a href="https://instagram.com/githubsrm"
        ><Instagram class="w-10 h-10 text-white inline-block"
      /></a>
      <a href="https://www.linkedin.com/company/githubsrm/"
        ><Linkedin class="w-10 h-10 text-white inline-block"
      /></a>
      <a href="mailto:community@githubsrm.tech"
        ><MailIcon class="w-10 h-10 text-white inline-block"
      /></a>
    </div>
  </div>
</template>

<script>
import Octocat from "../components/SVG/octocat";
import Twitter from "../components/SVG/twitter";
import Linkedin from "../components/SVG/linkedin";
import Instagram from "../components/SVG/instagram";
import { ClockIcon, MailIcon } from "@heroicons/vue/outline";
import Details from "./Details";

export default {
  name: "Left",
  components: {
    Octocat,
    Twitter,
    Linkedin,
    Instagram,
    ClockIcon,
    MailIcon,
    Details,
  },
};
</script>

<style></style>
