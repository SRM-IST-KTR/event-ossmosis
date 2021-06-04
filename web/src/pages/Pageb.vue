<template>
  <section class="w-full">
    <Field
      v-for="(field, i) in fields"
      :key="field.name"
      :field="field"
      :icon="icons[i]"
      @mutate="change($event, field.name)"
    />

    <div class="w-full md:items-center">
      <div class="mb-6">
        <label
          class="block text-gray-500 font-bold mb-1 md:mb-0"
          for="inline-full-name"
          v-if="!state"
        >
          {{ otp.name }}
        </label>

        <div v-if="!state" class="mt-1">
          <Button :button="{ name: 'Get OTP' }" @click="clickHandler" />
        </div>

        <div class="" v-else>
          <Field
            :field="otp"
            @mutate="change($event, otp.name)"
            :icon="'LockClosedIcon'"
          />
        </div>
      </div>
    </div>

    <div class="flex justify-evenly">
      <Button :button="{ name: 'Back' }" @click="backHandler" />
      <Button
        :button="button"
        :disabled="!state"
        :disable="!state"
        :check="true"
        @click="submitHandler"
      />
    </div>

    <div class="flex flex-col items-center mt-1">
      <p v-if="error.status" class="text-red-700 flex justify center">
        {{ error.body }}
      </p>

      <div class="flex space-x-2 justify center items-center" v-if="loading">
        <p class="inline-block">Submitting</p>
        <Loader class="inline-block" />
      </div>
    </div>
  </section>
</template>

<script>
import Field from "../components/Field";
import Button from "../components/Button.vue";
import Loader from "../components/SVG/loader";
export default {
  name: "Pageb",
  props: ["email", "error", "loading"],
  components: { Field, Button, Loader },
  data() {
    return {
      fields: [
        {
          index: "projectTitle",
          name: "Project Title",
          data: sessionStorage.getItem("formdata")
            ? JSON.parse(sessionStorage.getItem("formdata"))["projectTitle"]
            : "",
          placeholder: "Landing Page",
        },
        {
          index: "projectDescription",
          name: "Project Description",
          data: sessionStorage.getItem("formdata")
            ? JSON.parse(sessionStorage.getItem("formdata"))[
                "projectDescription"
              ]
            : "",
          placeholder: "This project is the landing page for GitHub SRM. It...",
        },
        {
          index: "projectLink",
          name: "Project Link",
          placeholder: "https://github.com/SRM-IST-KTR/githubsrm",
          data: sessionStorage.getItem("formdata")
            ? JSON.parse(sessionStorage.getItem("formdata"))["projectLink"]
            : "",
        },
      ],
      otp: {
        index: "otp",
        name: "Validate E-mail",
        placeholder: "OTP received in E-mail",
        data: "",
      },
      button: {
        name: "Submit",
      },
      icons: ["AnnotationIcon", null, "LinkIcon"],
      token: "",
      state: false,
    };
  },
  mounted() {
    sessionStorage.getItem("otp") ? (this.state = true) : (this.state = false);
  },
  methods: {
    submitHandler(e) {
      e.preventDefault();
      const self = this;
      window.grecaptcha.ready(function () {
        window.grecaptcha
          .execute(process.env.VUE_APP_SITE_KEY, {
            action: "submit",
          })
          .then(async (token) => {
            this.token = await Promise.resolve(token);
          })
          .then(() => {
            self.emit(this.token);
          });
      });
      this.$emit("mutate", this.fields);
      this.$emit("otp", this.otp);
    },
    backHandler() {
      this.$emit("mutate", this.fields);
      this.$emit("back", "0");
    },
    change(value, name) {
      if (name !== "Validate E-mail") {
        for (let i in this.fields) {
          if (name === this.fields[i]["name"]) {
            this.fields[i]["data"] = value;
          }
        }
      } else {
        this.otp.data = value;
      }
    },
    async clickHandler() {
      // if (!this.$props.email.email) {
      //   return;
      // }
      this.state = true;
      sessionStorage.setItem("otp", true);
      await fetch(`/api/v1/email/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: this.$props.email["email"],
          name: this.$props.email["name"],
        }),
      })
        .then(async (res) => {
          const d = await res.json();
          this.jwt = await d["jwt"];
        })
        .then(() => {
          this.send(this.jwt);
        });
    },
    send(value) {
      this.$emit("jwt", value);
    },
    emit(value) {
      this.$emit("token", value);
    },
  },
};
</script>
