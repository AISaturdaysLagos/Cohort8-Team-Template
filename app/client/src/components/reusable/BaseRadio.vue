<template>
  <div
    :class="{
      horizontal: !vertical,
      vertical: vertical,
    }"
  >
    <label
      v-if="label"
      for="uuid"
      class="block text-sm font-medium text-[#d9dce0] mb-1 mr-2 capitalize"
      >{{ label }}</label
    >
    <input
      :checked="modelValue === value"
      :value="value"
      @change="$emit('update:modelValue', value)"
      v-bind="$attrs"
      :id="uuid"
    />
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
