<template>
  <div class="flex items-end justify-evenly">
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
</template>

<script>
import Octocat from "../components/SVG/octocat";
import Twitter from "../components/SVG/twitter";
import Linkedin from "../components/SVG/linkedin";
import Instagram from "../components/SVG/instagram";
import { MailIcon } from "@heroicons/vue/outline";

export default {
  components: {
    Octocat,
    Twitter,
    Linkedin,
    Instagram,
    MailIcon,
  },
};
</script>

<style></style>
