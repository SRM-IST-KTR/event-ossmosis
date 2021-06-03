<template>
  <section
    class="text-gray-800 h-full items-center justify-center block mt-32 sm:mt-20 lg:mt-0 lg:flex"
  >
    <div class="m-4 absolute top-0 left-0">
      <a href="http://githubsrm.tech/" class="flex justify-center items-center">
        <GCSRM class="w-24 h-24 md:w-32 md:h-32" />
      </a>
    </div>

    <div class="flex flex-col min-h-80-screen">
      <div class="w-11/12 xl:w-full max-w-6xl mx-auto">
        <div class="lg:w-7/12 w-full">
          <h1 class="font-bold text-white text-center text-5xl mb-1">
            OSSmosis
          </h1>
          <h3 class="font-thin text-gray-300 text-center text-xl mb-5">
            Is your project OSS ready?
          </h3>
        </div>
      </div>

      <div
        class="w-11/12 xl:w-full max-w-6xl mx-auto flex flex-wrap justify-between items-start h-full"
      >
        <Left />
        <div
          id="form"
          class="lg:w-4/12 w-full bg-white rounded-lg flex flex-col items-center justify-center"
        >
          <Pagea
            v-if="state == 0"
            @mutate="changea($event)"
            @email="checkmail($event)"
            class="p-8"
          />
          <Pageb
            v-if="state == 1"
            @mutate="changeb($event)"
            @back="back"
            :error="error"
            :email="email"
            :loading="loading"
            @token="tokenCheck($event)"
            @otp="otpCheck($event)"
            @jwt="jwtCheck($event)"
            class="p-8"
          />
          <Pagec v-if="state == 2" />
        </div>
        <div class="w-11/12 xl:w-full mt-8 mb-8 lg:hidden mx-auto">
          <Footer />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Pagea from "./Pagea.vue";
import Pageb from "./Pageb.vue";
import Pagec from "./Pagec.vue";
import Left from "./Left.vue";
import Footer from "../components/Footer";
import GCSRM from "../components/SVG/githubsrmsvg";

export default {
  name: "Main",
  components: {
    Pagea,
    Pageb,
    Pagec,
    Left,
    GCSRM,
    Footer,
  },
  data() {
    return {
      state: 0,
      fields: {},
      email: "",
      token: "",
      error: {},
      otp: "",
      jwt: "",
      loading: false,
    };
  },
  beforeMount() {
    sessionStorage.clear();
  },
  mounted() {
    this.state = 0;
    this.fields = {};
    this.loading = false;
  },
  methods: {
    back() {
      this.state = 0;
    },
    changea(value) {
      value.map((i) => (this.fields[i["index"]] = i["data"]));
      sessionStorage.setItem("formdata", JSON.stringify(this.fields));
      this.state = 1;
    },
    changeb(value) {
      value.map((i) => (this.fields[i["index"]] = i["data"]));
      sessionStorage.setItem("formdata", JSON.stringify(this.fields));
    },
    otpCheck(value) {
      this.otp = value;
    },
    jwtCheck(value) {
      this.jwt = value;
    },
    checkmail(value) {
      this.email = value;
    },
    async tokenCheck(value) {
      this.error = {};
      this.loading = true;
      this.token = value;
      const response = await fetch(`/api/v1/data/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${this.jwt}`,
          "X-Recaptcha-Token": this.token,
        },
        body: JSON.stringify({
          fields: this.fields,
          otp: this.otp,
        }),
      });
      this.loading = false;
      if (response.status === 200) {
        this.state = 2;
      } else {
        this.error = { status: response.status, body: response.statusText };
      }
    },
  },
};
</script>

<style>
* {
  box-sizing: border-box;
}
html {
  scroll-behavior: smooth;
}
html,
body {
  margin: 0;
  padding: 0;
}
#app {
  font-family: "Montserrat", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #000;
  height: 100%;
}
.section {
  background-color: #0d1117;
}
</style>
