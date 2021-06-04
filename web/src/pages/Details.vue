<template>
  <div class="flex flex-wrap mt-2 lg:mt-0">
    <div class="w-full">
      <ul
        class="
          flex
          justify-between
          mb-0
          list-none
          pb-4
          flex-row
          uppercase
          font-bold
          text-xxs
          sm:text-xs
        "
      >
        <li class="-mb-px w-full text-center">
          <a
            class="py-3 shadow-lg rounded block leading-normal cursor-pointer"
            v-on:click="toggleTabs(1)"
            v-bind:class="{
              'text-gray-600 bg-white': openTab !== 1,
              'text-white bg-gray-600': openTab === 1,
            }"
          >
            Description
          </a>
        </li>
        <li class="-mb-px mx-2 w-full text-center">
          <a
            class="py-3 shadow-lg rounded block leading-normal cursor-pointer"
            v-on:click="toggleTabs(2)"
            v-bind:class="{
              'text-gray-600 bg-white': openTab !== 2,
              'text-white bg-gray-600': openTab === 2,
            }"
          >
            Rules
          </a>
        </li>
        <li class="-mb-px w-full text-center">
          <a
            class="py-3 shadow-lg rounded block leading-normal cursor-pointer"
            v-on:click="toggleTabs(3)"
            v-bind:class="{
              'text-gray-600 bg-white': openTab !== 3,
              'text-white bg-gray-600': openTab === 3,
            }"
          >
            Criteria
          </a>
        </li>
      </ul>
      <div
        class="
          relative
          flex flex-col
          min-w-0
          break-words
          bg-white
          w-full
          shadow-lg
          rounded
        "
      >
        <div class="p-2 sm:p-4 md:p-8 flex-auto">
          <div class="tab-content tab-space">
            <div v-bind:class="{ hidden: openTab !== 1, block: openTab === 1 }">
              <p>Ever wondered how far your project meets OSS criteria?</p>
              <p>Does your project have a proper commit history?</p>
              <p>A license and a readme?</p>
              <p>Are your pull requests up to the mark?</p>
              <br />
              <p>
                We wondered about it too, and we ended up with OSSmosis, a
                chance for you to flex your OSS projects and win exciting
                schwags from GitHub Community SRM!
              </p>
              <p>
                All you need is to submit your best OSS project done till date
                and stand a chance to be awarded the honour of "Best OSS
                Project" by the community.
              </p>
              <br />
              <p>
                Visit the link in the bio to know more about the participation
                rules.
              </p>
            </div>
            <div v-bind:class="{ hidden: openTab !== 2, block: openTab === 2 }">
              <ul class="list-disc ml-4">
                <li>
                  Your project must be hosted over GitHub and the visibility
                  must be public.
                </li>
                <li>
                  Your project should be your own. If it is a collaboration
                  project, your contribution must be sufficient to qualify for
                  the prize.
                </li>
                <li>
                  Your project should not promote any illegal purpose or action.
                </li>
                <li>
                  You agree to give GitHub Community SRM the rights to showcase
                  your project over our channels (with the proper credits to
                  you) by participating in this contest.
                </li>
              </ul>
            </div>
            <div v-bind:class="{ hidden: openTab !== 3, block: openTab === 3 }">
              <ul class="list-disc ml-4">
                <li>
                  A proper readme and a license file are required for all OSS
                  projects.
                </li>
                <li>
                  A regular and clear commit history is the marker of a good OSS
                  project.
                </li>
                <li>
                  Issues are a great tool to maintain the track of a project.
                  They are also an excellent way of letting the maintainers know
                  about a bug in the project.
                </li>
                <li>
                  Pull Requests are the backbone of any OSS project. A detailed
                  PR helps the maintainers a lot.
                </li>
                <li>
                  It is a bonus (but is not required) if you have a CI/CD
                  pipeline set up in your project.
                </li>
                <li>
                  It would also help (but is not required) to have a good track
                  record of Contributions in your GitHub account.
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "tabs",
  data() {
    return {
      openTab: 1,
    };
  },
  methods: {
    toggleTabs: function (tabNumber) {
      this.openTab = tabNumber;
    },
  },
};
</script>
