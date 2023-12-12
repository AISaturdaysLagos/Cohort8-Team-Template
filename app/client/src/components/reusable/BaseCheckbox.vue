<template>
  <input
    :checked="modelValue"
    @change="$emit('update:modelValue', $event.target.checked)"
  />
  <label v-if="label" for="">{{ label }}</label>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      default: "",
    },
    modelValue: {
      type: [String, Number],
      default: "",
    },
    value: {
      type: [String, Number],
      required: true,
    },
  },
};
</script>

<style></style>
