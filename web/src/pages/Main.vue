<template>
  <section class="text-gray-800 section body-font flex md:h-screen sm:h-full pb-10">
    <div class="m-4 absolute top-0 left-0">
      <a href="http://githubsrm.tech" class="flex justify-center items-center">
        <GCSRM class="w-32 h-32" />
      </a>
    </div>
    <div
      class="
        w-10/12
        max-w-6xl
        mx-auto
        flex flex-wrap
        justify-between
        items-center
      "
    >
      <div
        class="
          lg:w-7/12
          w-full
          flex
          space-x-5
          justify-center
          items-center
          center
        "
      >
        <Left />
      </div>
      <div
        id="form"
        class="
          lg:w-4/12
          w-full
          bg-white
          rounded-lg
          p-8
          flex flex-col
          mt-10
          md:mt-0
          h-auto
        "
      >
        <Pagea
          v-if="state == 0"
          @mutate="changea($event)"
          @email="checkmail($event)"
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
        />
        <Pagec v-if="state == 2" />
      </div>
    </div>
    <router-view />
  </section>
</template>

<script>
import Pagea from "./Pagea.vue";
import Pageb from "./Pageb.vue";
import Pagec from "./Pagec.vue";
import Left from "./Left.vue";
import GCSRM from "../components/SVG/githubsrmsvg";

export default {
  name: "Main",
  components: {
    Pagea,
    Pageb,
    Pagec,
    Left,
    GCSRM,
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
