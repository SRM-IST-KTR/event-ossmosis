<template>
  <section class="form">
    <Field
      v-for="(field, i) in fields"
      :key="field.name"
      :field="field"
      :icon="icons[i]"
      @mutate="change($event, field.name)"
      @error="errorCheck($event)"
    />
    <div class="flex float-right">
      <Button :button="button" @click="submitHandler" />
    </div>
    <p v-if="error.length > 0" class="text-red-700">{{ error }}</p>
  </section>
</template>

<script>
import Field from "../components/Field";
import Button from "../components/Button.vue";
import { validate } from "../components/validate";

export default {
  name: "Pagea",
  components: { Field, Button },
  data() {
    return {
      fields: [
        {
          index: "name",
          name: "Name",
          data: sessionStorage.getItem("formdata")
            ? JSON.parse(sessionStorage.getItem("formdata"))["name"]
            : "",
          placeholder: "GitHub SRM",
        },
        {
          index: "registrationNum",
          name: "Registration Number",
          data: sessionStorage.getItem("formdata")
            ? JSON.parse(sessionStorage.getItem("formdata"))["registrationNum"]
            : "",
          placeholder: "RAxxxxxxxxxxxxx",
        },
        {
          index: "email",
          name: "College Email",
          data: sessionStorage.getItem("formdata")
            ? JSON.parse(sessionStorage.getItem("formdata"))["email"]
            : "",
          placeholder: "gs0000@srmist.edu.in",
        },
        {
          index: "githubId",
          name: "Github ID",
          data: sessionStorage.getItem("formdata")
            ? JSON.parse(sessionStorage.getItem("formdata"))["githubId"]
            : "",
          placeholder: "srm-ist-ktr",
        },
      ],
      icons: ["UserIcon", "HashtagIcon", "MailIcon", "GithubSVG"],
      button: {
        name: "Next",
        state: false,
      },
      error: "",
    };
  },
  methods: {
    async submitHandler() {
      let a = 0;
      for (let i in this.fields) {
        if (
          this.fields[i]["data"] === undefined ||
          (await validate(this.fields[i]["name"], this.fields[i]["data"])) !==
            ""
        ) {
          a += 1;
        }
      }
      if (a === 0) {
        this.$emit("email", {
          email: this.fields[2]["data"],
          name: this.fields[0]["data"],
        });
        this.$emit("mutate", this.fields);
      } else {
        this.error = "Form validation error";
      }
    },
    change(value, name) {
      for (let i in this.fields) {
        if (name === this.fields[i]["name"]) {
          this.fields[i]["data"] = value;
        }
      }
    },
  },
};
</script>

<style></style>
