<template>
  <pulse-loader :loading="loading" :color="color" :size="size"></pulse-loader>
</template>

<script>
import PulseLoader from "vue-spinner/src/PulseLoader.vue";

export default {
  components: {
    PulseLoader,
  },
  props: {
    loading: {
      type: Boolean,
      default: false,
    },
    color: {
      type: String,
      default: "green",
    },
    size: {
      type: String,
      default: "20px",
    },
  },
  setup(props) {
    return props;
  },
};
</script>

<style lang="scss" scoped></style>
