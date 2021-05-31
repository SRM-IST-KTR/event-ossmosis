<template>
  <div>
    <div
      class="w-full md:items-center max-w-sm"
      v-if="field.name.includes('Description')"
    >
      <div class="md:flex md:items-center mb-6">
        <div class="md:w-1/3">
          <label
            class="block text-gray-500 font-bold mb-1 md:mb-0 pr-4"
            for="inline-full-name"
          >
            {{ field.name }}
          </label>
        </div>
        <div class="md:w-2/3">
          <textarea
            :class="
              error.length > 0
                ? 'bg-gray-200 appearance-none border-2 border-red-500 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
                : ' bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
            "
            v-model="fielddata"
            type="text"
            :placeholder="field.name"
            @change="mutate"
            @blur="handleBlur"
          />
        </div>
      </div>
    </div>
    <div
      class="w-full md:items-center max-w-sm"
      v-else-if="field.name === 'Email'"
    >
      <div class="md:flex md:items-center mb-6">
        <div class="md:w-1/3">
          <label
            class="block text-gray-500 font-bold mb-1 md:mb-0 pr-4"
            for="inline-full-name"
          >
            {{ field.name }}
          </label>
        </div>
        <div class="md:w-2/3">
          <input
            :class="
              error.length > 0
                ? 'bg-gray-200 appearance-none border-2 border-red-500 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
                : ' bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
            "
            v-model="fielddata"
            type="email"
            :placeholder="field.name"
            @change="mutate"
            @blur="handleBlur"
          />
        </div>
      </div>
    </div>
    <div class="w-full md:items-center max-w-sm" v-else>
      <div class="md:flex md:items-center mb-6">
        <div class="md:w-1/3">
          <label
            class="block text-gray-500 font-bold mb-1 md:mb-0 pr-4"
            for="inline-full-name"
          >
            {{ field.name }}
          </label>
        </div>
        <div class="md:w-2/3">
          <input
            :class="
              error === undefined || error.length > 0
                ? 'bg-gray-200 appearance-none border-2 border-red-500 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
                : ' bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
            "
            v-model="fielddata"
            type="text"
            :placeholder="field.name"
            @change="mutate"
            @blur="handleBlur"
          />
        </div>
      </div>
    </div>
    <span v-if="error.length > 0" class="text-xs text-red-700">{{
      error
    }}</span>
  </div>
</template>

<script>
import { validate } from "./validate";
export default {
  name: "Field",
  props: ["field"],
  data() {
    return {
      fielddata: "",
      error: "",
    };
  },
  methods: {
    mutate: async function () {
      this.$emit("mutate", this.fielddata);
      this.error = await validate(this.$props.field.name, this.fielddata);
    },
    async handleBlur() {
      this.error = await validate(this.$props.field.name, this.fielddata);
    },
  },
};
</script>

<style></style>
