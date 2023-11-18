<template>
  <div class="form-stepper">
    <div class="progress-bar">
      <div class="progress" :style="`width: ${progress}%`"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FormStepper",
  props: {
    currentStep: {
      type: Number,
      default: 0,
    },
  },
  computed: {
    progress() {
      return (this.currentStep / 10) * 100;
    },
  },
};
</script>

<style scoped>
.form-stepper {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background-color: #ccc;
  position: relative;
  margin-top: 10px;
}

.progress {
  height: 100%;
  background-color: #3490dc;
  transition: width 0.3s ease-in-out;
}
</style>
