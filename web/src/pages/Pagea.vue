<template>
  <section class="w-full">
    <Field
      v-for="(field, i) in fields"
      :key="field.name"
      :field="field"
      :icon="icons[i]"
      @mutate="change($event, field.name)"
    />

    <div class="flex justify-evenly items-center mt-6">
      <div
        v-if="disabledButton"
        class="w-full text-xs text-red-500 font-bold text-center"
      >
        {{ warning }}
      </div>
      <div v-else class="w-full"></div>
      <Button
        :disable="disabledButton"
        :button="button"
        @click="submitHandler"
      />
    </div>
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
          error: "",
        },
        {
          index: "registrationNum",
          name: "Registration Number",
          data: sessionStorage.getItem("formdata")
            ? JSON.parse(sessionStorage.getItem("formdata"))["registrationNum"]
            : "",
          placeholder: "RAxxxxxxxxxxxxx",
          error: "",
        },
        {
          index: "email",
          name: "College Email",
          data: sessionStorage.getItem("formdata")
            ? JSON.parse(sessionStorage.getItem("formdata"))["email"]
            : "",
          placeholder: "gs0000@srmist.edu.in",
          error: "",
        },
        {
          index: "githubId",
          name: "Github ID",
          data: sessionStorage.getItem("formdata")
            ? JSON.parse(sessionStorage.getItem("formdata"))["githubId"]
            : "",
          placeholder: "srm-ist-ktr",
          error: "",
        },
      ],
      icons: ["UserIcon", "HashtagIcon", "MailIcon", "GithubSVG"],
      button: {
        name: "Next",
        state: false,
      },
      warning: "",
      disabledButton: false,
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
        this.warning = "Please check your inputs.";
        this.disabledButton = true;
      }
    },
    change(value, name) {
      for (let i in this.fields) {
        if (name === this.fields[i]["name"]) {
          this.fields[i]["data"] = value.data;
        }
      }
      if (value.error.length > 0) {
        this.disabledButton = true;
      } else {
        this.disabledButton = false;
      }
    },
  },
};
</script>
