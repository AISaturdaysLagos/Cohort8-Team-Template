<template>
  <div class="fixed bottom-4 w-full">
    <div class="flex justify-center">
      <button
        class="bg-secondary mr-4 py-2 px-8 rounded-full text-white text-sm font-light cursor-pointer font-primary"
        @click="prev"
        v-show="back()"
      >
        Back
      </button>
      <button
        class="bg-secondary mr-4 py-2 px-8 rounded-full text-white text-sm font-light cursor-pointer font-primary"
        @click="next"
      >
        {{ action }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "StepperNavigation",
  props: {
    currentStep: {
      type: Number,
      default: 0,
    },
  },
  methods: {
    next() {
      this.$emit("next");
    },
    prev() {
      this.$emit("prev");
    },
    back() {
      return this.currentStep > 0;
    },
  },
  computed: {
    action() {
      return this.currentStep === 10 ? "Submit" : "Next";
    },
  },
};
</script>

<style scoped></style>
