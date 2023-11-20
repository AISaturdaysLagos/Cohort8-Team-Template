<template>
  <div>
    <label
      v-if="label"
      class="block text-sm font-medium text-[#d9dce0] mb-1 capitalize"
      >{{ label }}</label
    >
    <div
      :class="{
        horizontal: !vertical,
        vertical: vertical,
      }"
    >
      <BaseRadio
        v-for="option in options"
        :key="option.value"
        :label="option.label"
        :value="option.value"
        :modelValue="modelValue"
        type="radio"
        @update:modelValue="$emit('update.modelValue', $event)"
        :name="name"
        :vertical="vertical"
      />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      default: "",
    },
    options: {
      type: Array,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
    modelValue: {
      type: [String, Number],
      required: true,
    },
    vertical: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style>
.horizontal {
  display: flex;
  margin-right: 20px;
}
.vertical {
  margin-bottom: 10px;
}
</style>
