<template>
  <div>
    <label
      v-if="label"
      class="block text-sm font-medium text-[#d9dce0] mb-1 capitalize"
      >{{ label }}</label
    >
    <select
      :value="modelValue"
      v-bind="{
        ...$attrs,
        onChange: ($event) => {
          $emit('update:modelValue', $event.target.value);
        },
      }"
      class="mt-1 p-4 w-full bg-[#262d3b] border-2 border-solid border-secondary rounded-md shadow-sm focus:outline-none text-[#d9dce0] placeholder-[#949AA6]"
    >
      <option
        v-for="option in options"
        :value="option"
        :key="option"
        :selected="option === modelValue"
      >
        {{ option }}
      </option>
    </select>
  </div>
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
    options: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style></style>
