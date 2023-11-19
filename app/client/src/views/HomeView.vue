<template>
  <div class="bg-primary h-[97vh] w-full relative">
    <MultiFormStepper :currentStep="currentStep" />
    <form class="w-full h-full flex justify-center items-center">
      <AppDescription v-if="currentStep === 0" />
    </form>
    <StepperNavigation
      @next="nextStep"
      @prev="prevStep"
      :currentStep="currentStep"
    />
  </div>
</template>

<script>
import MultiFormStepper from "@/components/MultiFormStepper.vue";
import StepperNavigation from "@/components/StepperNavigation.vue";
import AppDescription from "@/components/AppDescription.vue";

export default {
  name: "HomeView",
  components: {
    MultiFormStepper,
    StepperNavigation,
    AppDescription,
  },
  data() {
    return {
      currentStep: 0,
      maxStep: 10,
      minStep: 0,
    };
  },
  methods: {
    nextStep() {
      if (this.currentStep < this.maxStep) {
        this.currentStep++;
      }
    },
    prevStep() {
      if (this.currentStep > this.minStep) {
        this.currentStep--;
      }
    },
  },
};
</script>
