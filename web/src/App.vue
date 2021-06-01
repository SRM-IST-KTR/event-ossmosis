<template>
  <div class="flex flex-col justify-center items-center">
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
</template>

<script>
import Pagea from "./pages/Pagea.vue";
import Pageb from "./pages/Pageb.vue";
import Pagec from "./pages/Pagec.vue";

export default {
  name: "App",
  components: {
    Pagea,
    Pageb,
    Pagec,
  },
  data() {
    return {
      state: 0,
      fields: [],
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
    this.fields = [];
    this.loading = false;
  },
  methods: {
    back() {
      this.state = 0;
    },
    changea(value) {
      value.map((i) => this.fields.push(i));
      this.state = 1;
    },
    changeb(value) {
      value.map((i) => this.fields.push(i));
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
      this.token = value;
      this.loading = true;
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
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
