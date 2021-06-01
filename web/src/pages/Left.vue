<template>
  <div>
    <div class="flex justify-center items-center">
      <a href="http://githubsrm.tech" class="flex justify-center items-center"
        ><GCSRM class="w-1/3 h-1/3 text-white"
      /></a>
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

export default {
  name: "Left",
  components: {
    GCSRM,
    Octocat,
    Twitter,
    Linkedin,
    Instagram,
  },
};
</script>

<style></style>
