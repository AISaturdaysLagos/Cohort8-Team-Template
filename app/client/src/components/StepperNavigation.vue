<template>
  <div class="fixed bottom-4 w-full">
    <div class="flex justify-center">
      <button
        class="bg-secondary mr-4 py-2 px-8 rounded-full text-white text-sm font-light cursor-pointer font-primary"
        @click="prev"
        v-if="back"
        type="button"
        :disabled="loading"
        :class="{ disable: loading }"
      >
        Back
      </button>
      <button
        class="bg-secondary mr-4 py-2 px-8 rounded-full text-white text-sm font-light cursor-pointer font-primary"
        @click="next"
        :type="currentStep === 3 ? 'submit' : 'button'"
        :disabled="loading"
        :class="{ disable: loading }"
      >
        <template v-if="!loading">
          {{ action }}
        </template>
        <template v-else>
          <pause-loader :loading="loading" size="20px" color="#fff" />
        </template>
      </button>
    </div>
  </div>
</template>

<script>
import { computed } from "vue";
import PauseLoader from "@/components/PauseLoader.vue";

export default {
  name: "StepperNavigation",
  components: {
    PauseLoader,
  },
  props: {
    currentStep: {
      type: Number,
      default: 0,
    },
    loading: {
      type: Boolean,
      default: false,
    },
  },
  setup(props, { emit }) {
    const back = computed(() => props.currentStep > 0);

    const next = () => {
      emit("next");
    };

    const prev = () => {
      emit("prev");
    };

    const action = computed(() => {
      if (props.currentStep === 0) {
        return "Start";
      } else if (props.currentStep === 3) {
        return "Submit";
      } else {
        return "Next";
      }
    });

    return {
      back,
      next,
      prev,
      action,
    };
  },
};
</script>

<style scoped>
.disable {
  background-color: #eee;
  cursor: not-allowed;
}
</style>
