<template>
  <div>
    <div
      class="w-auto md:items-center "
      v-if="field.name.includes('Description')"
    >
      <div class="mb-6">
        <div>
          <label
            class="block text-gray-500 font-bold mb-1 md:mb-0 pr-4"
            for="inline-full-name"
          >
            {{ field.name }}
          </label>
        </div>
        <div>
          <textarea
            :class="
              error.length > 0
                ? 'mr-0 bg-gray-200 appearance-none border-2 border-red-500 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
                : 'mr-0 bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
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
      class="w-auto md:items-center "
      v-else-if="field.name === 'College Email'"
    >
      <div class="mb-6">
        <div>
          <label
            class="block text-gray-500 font-bold mb-1 md:mb-0 pr-4"
            for="inline-full-name"
          >
            {{ field.name }}
          </label>
        </div>
        <div class="relative flex flex-wrap items-stretch mb-3">
          <span
            class="
              z-10
              h-full
              leading-snug
              font-normal
              absolute
              text-center text-blueGray-300
              absolute
              bg-transparent
              rounded
              text-base
              items-center
              justify-center
              w-8
              pl-3
              py-3
            "
            ><MailIcon class="h-5 w-5 text-black"
          /></span>
          <input
            :class="
              error.length > 0
                ? 'bg-gray-200 appearance-none border-2 border-red-500 rounded w-full py-3 px-9  text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
                : ' bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-3 px-9  text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
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
    <div class="w-auto md:items-center " v-else>
      <div class="mb-6">
        <div class="">
          <label
            class="block text-gray-500 font-bold mb-1 md:mb-0 pr-4"
            for="inline-full-name"
          >
            {{ field.name }}
          </label>
        </div>
        <div class="relative flex flex-wrap items-stretch mb-3">
          <span
            v-if="icon === 'UserIcon'"
            class="
              z-10
              h-full
              leading-snug
              font-normal
              absolute
              text-center text-blueGray-300
              absolute
              bg-transparent
              rounded
              text-base
              items-center
              justify-center
              w-8
              pl-3
              py-3
            "
          >
            <UserIcon class="h-5 w-5 text-black" />
          </span>
          <span
            v-else-if="icon === 'HashtagIcon'"
            class="
              z-10
              h-full
              leading-snug
              font-normal
              absolute
              text-center text-blueGray-300
              absolute
              bg-transparent
              rounded
              text-base
              items-center
              justify-center
              w-8
              pl-3
              py-3
            "
          >
            <HashtagIcon class="h-5 w-5 text-black" />
          </span>
          <span
            v-else-if="icon === 'GithubSVG'"
            class="
              z-10
              h-full
              leading-snug
              font-normal
              absolute
              text-center text-blueGray-300
              absolute
              bg-transparent
              rounded
              text-base
              items-center
              justify-center
              w-8
              pl-3
              py-3
            "
          >
            <GithubSVG class="h-5 w-5 text-black" />
          </span>
          <span
            v-else-if="icon === 'LinkIcon'"
            class="
              z-10
              h-full
              leading-snug
              font-normal
              absolute
              text-center text-blueGray-300
              absolute
              bg-transparent
              rounded
              text-base
              items-center
              justify-center
              w-8
              pl-3
              py-3
            "
          >
            <LinkIcon class="h-5 w-5 text-black" />
          </span>
          <span
            v-else-if="icon === 'AnnotationIcon'"
            class="
              z-10
              h-full
              leading-snug
              font-normal
              absolute
              text-center text-blueGray-300
              absolute
              bg-transparent
              rounded
              text-base
              items-center
              justify-center
              w-8
              pl-3
              py-3
            "
          >
            <AnnotationIcon class="h-5 w-5 text-black" />
          </span>
          <input
            :class="
              error === undefined || error.length > 0
                ? 'bg-gray-200 appearance-none border-2 border-red-500 rounded w-full py-3 px-9 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
                : ' bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-3 px-9 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
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
import { UserIcon, MailIcon, AnnotationIcon } from "@heroicons/vue/solid";
import { HashtagIcon, LinkIcon } from "@heroicons/vue/outline";
import GithubSVG from "./SVG/githubsvg";

export default {
  name: "Field",
  props: ["field", "icon"],
  components: {
    UserIcon,
    MailIcon,
    HashtagIcon,
    GithubSVG,
    AnnotationIcon,
    LinkIcon,
  },
  data() {
    return {
      fielddata: "",
      error: "",
    };
  },
  mounted() {
    console.log(this.$props.icon);
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
