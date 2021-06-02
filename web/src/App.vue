<template>
  <section class="text-gray-800 section body-font flex md:h-screen sm:h-full">
    <div class="container px-5 py-5 mx-auto flex flex-wrap items-center center">
      <div
        class="
          lg:w-3/5
          md:w-1/2
          md:pr-16
          lg:pr-0
          pr-0
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
        class="
          lg:w-2/6
          md:w-1/2
          bg-white
          rounded-lg
          p-8
          flex flex-col
          md:ml-auto
          w-full
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
  </section>
</template>

<script>
import Pagea from "./pages/Pagea.vue";
import Pageb from "./pages/Pageb.vue";
import Pagec from "./pages/Pagec.vue";
import Left from "./pages/Left.vue";

export default {
  name: "App",
  components: {
    Pagea,
    Pageb,
    Pagec,
    Left,
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
  mounted() {
    this.state = 0;
    this.fields = {};
    this.loading = false;
    sessionStorage.clear();
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
      this.loading = true;
      this.token = value;
      const response = await fetch(
        `${process.env.VUE_APP_SERVER}/api/v1/data/`,
        {
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
        }
      );
      this.loading = false;
      if (response.status === 201) {
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
