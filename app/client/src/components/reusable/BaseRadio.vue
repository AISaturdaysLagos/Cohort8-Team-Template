<template>
  <div
    :class="{
      horizontal: !vertical,
      vertical: vertical,
    }"
    class="w-full h-8 mb-3 flex items-center border-2 p-6 border-secondary"
  >
    <input
      :checked="modelValue === value"
      :value="value"
      @change="$emit('update:modelValue', value)"
      v-bind="$attrs"
      :id="uuid"
      class="mr-4"
    />
    <label
      v-if="label"
      for="uuid"
      class="block text-base font-medium text-[#d9dce0] capitalize"
      >{{ label }}</label
    >
  </div>
</template>

<script>
import UniqueID from "@/features/UniqueID";

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
      default: "",
    },
    vertical: {
      type: Boolean,
      default: false,
    },
  },
  setup() {
    const uuid = UniqueID().getID();
    return { uuid };
  },
};
</script>

<style>
.horizontal {
  margin-right: 20px;
}
.vertical {
  margin-bottom: 20px;
}
</style>
