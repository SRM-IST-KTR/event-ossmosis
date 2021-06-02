<template>
  <div>
    <div class="mb-24">
      <a href="http://githubsrm.tech" class="flex justify-center items-center"
        ><GCSRM class="w-1/3 h-1/3 text-white"
      /></a>
    </div>
    <div class="mb-32">
      <div
        class="flex justify-center items-center font-bold text-white text-4xl"
      >
        Lorem ipsum
      </div>
      <div class="m-5 text-white">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla risus
        dolor, ullamcorper et molestie et, molestie ut mi. Maecenas vel leo
        condimentum arcu cursus tempor. Sed eu nibh turpis. Etiam vitae
        convallis tellus.
      </div>
      <div class="flex justify-center items-center m-5 text-white">
        <ul class="text-white text-xl">
          <li class="flex">
            <ClockIcon class="w-7 h-7" /><span class="mx-4">Time</span>
          </li>
          <li class="flex">
            <MailIcon class="w-7 h-7" /><a
              href="mailto:community@githubsrm.tech"
              class="mx-4"
              >community@githubsrm.tech</a
            >
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
    </div>
  </div>
</template>

<script>
import GCSRM from "../components/SVG/githubsrmsvg";
import Octocat from "../components/SVG/octocat";
import Twitter from "../components/SVG/twitter";
import Linkedin from "../components/SVG/linkedin";
import Instagram from "../components/SVG/instagram";
import { ClockIcon, MailIcon } from "@heroicons/vue/outline";

export default {
  name: "Left",
  components: {
    GCSRM,
    Octocat,
    Twitter,
    Linkedin,
    Instagram,
    ClockIcon,
    MailIcon,
  },
};
</script>

<style></style>
