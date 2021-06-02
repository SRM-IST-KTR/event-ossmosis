<template>
  <section class="form md:justify-center">
    <Field
      v-for="(field, i) in fields"
      :key="field.name"
      :field="field"
      :icon="icons[i]"
      @mutate="change($event, field.name)"
    />
    <div class="w-full md:items-center">
      <div class="mb-6">
        <div class="">
          <label
            class="block text-gray-500 font-bold mb-1 md:mb-0 pr-4"
            for="inline-full-name"
          >
            Validate Email
          </label>
        </div>
        <div v-if="!state">
          <Button :button="{ name: 'Get OTP' }" @click="clickHandler" />
        </div>
        <div class="" v-else>
          <input
            class="
              bg-gray-200
              appearance-none
              border-2 border-gray-200
              rounded
              w-full
              py-2
              px-4
              text-gray-700
              leading-tight
              focus:outline-none
              focus:bg-white
              focus:border-purple-500
            "
            v-model="otp"
            type="text"
            placeholder="OTP recieved in Email"
          />
        </div>
      </div>
    </div>
    <div class="flex space-x-5 float-right">
      <Button :button="{ name: 'Back' }" @click="backHandler" />
      <Button :button="button" @click="submitHandler" />
    </div>
    <p v-if="error.status" class="text-red-700">{{ error.body }}</p>
    <p v-if="loading">Submitting...</p>
  </section>
</template>

<script>
import Field from "../components/Field";
import Button from "../components/Button.vue";
export default {
  name: "Pageb",
  props: ["email", "error", "loading"],
  components: { Field, Button },
  data() {
    return {
      fields: [
        {
          index: "projectTitle",
          name: "Project Title",
          data: sessionStorage.getItem("formdata")
            ? JSON.parse(sessionStorage.getItem("formdata"))["projectTitle"]
            : "",
        },
        {
          index: "projectDescription",
          name: "Project Description",
          data: sessionStorage.getItem("formdata")
            ? JSON.parse(sessionStorage.getItem("formdata"))[
                "projectDescription"
              ]
            : "",
        },
        {
          index: "projectLink",
          name: "Project Link",
          placeholder: "https://github.com/profile/repo",
          data: sessionStorage.getItem("formdata")
            ? JSON.parse(sessionStorage.getItem("formdata"))["projectLink"]
            : "",
        },
      ],
      button: {
        name: "Submit",
      },
      icons: ["AnnotationIcon", null, "LinkIcon"],
      token: "",
      otp: "",
      state: false,
    };
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
      for (let i in this.fields) {
        if (name === this.fields[i]["name"]) {
          this.fields[i]["data"] = value;
        }
      }
    },
    async clickHandler() {
      this.state = true;
      await fetch(`${process.env.VUE_APP_SERVER}/api/v1/email/`, {
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

<style></style>
