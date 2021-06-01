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
    <div class="flex justify-center items-center">
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
        { name: "Name" },
        { name: "Registration Number" },
        { name: "College Email" },
        { name: "Github Id" },
      ],
      icons: ["UserIcon", "HashtagIcon", "MailIcon", "GithubSVG"],
      button: {
        name: "Next",
        state: false,
      },
      error: "",
    };
  },
  mounted() {
    this.fields = [
      { name: "Name" },
      { name: "Registration Number" },
      { name: "College Email" },
      { name: "Github Id" },
    ];
    this.button = {
      name: "Next",
      state: false,
    };
    this.error = "";
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
