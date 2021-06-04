<template>
  <div class="flex items-end justify-evenly">
    <a
      rel="noopener noreferrer"
      target="_blank"
      href="https://github.com/SRM-IST-KTR"
      class="hover:bg-gray-700 hover:rounded-full transition-all duration-300"
    >
      <Octocat
        class="
          w-10
          h-10
          text-white
          inline-block
          hover:p-2
          transition-all
          duration-300
        "
      />
    </a>
    <a
      rel="noopener noreferrer"
      target="_blank"
      href="https://twitter.com/githubsrm"
      class="hover:bg-gray-700 hover:rounded-full transition-all duration-300"
    >
      <Twitter
        class="
          w-10
          h-10
          text-white
          inline-block
          hover:p-2
          transition-all
          duration-300
        "
      />
    </a>
    <a
      rel="noopener noreferrer"
      target="_blank"
      href="https://instagram.com/githubsrm"
      class="hover:bg-gray-700 hover:rounded-full transition-all duration-300"
    >
      <Instagram
        class="
          w-10
          h-10
          text-white
          inline-block
          hover:p-2
          transition-all
          duration-300
        "
      />
    </a>
    <a
      rel="noopener noreferrer"
      target="_blank"
      href="https://www.linkedin.com/company/githubsrm/"
      class="hover:bg-gray-700 hover:rounded-full transition-all duration-300"
    >
      <Linkedin
        class="
          w-10
          h-10
          text-white
          inline-block
          hover:p-2
          transition-all
          duration-300
        "
      />
    </a>
    <a
      rel="noopener noreferrer"
      target="_blank"
      href="mailto:community@githubsrm.tech"
      class="hover:bg-gray-700 hover:rounded-full transition-all duration-300"
    >
      <MailIcon
        class="
          w-10
          h-10
          text-white
          inline-block
          hover:p-2
          transition-all
          duration-300
        "
      />
    </a>
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
