<template>
  <div>
    <label
      v-if="label"
      :for="uuid"
      class="block text-sm font-medium text-[#d9dce0] mb-1 capitalize"
      >{{ label }}</label
    >
    <input
      v-bind="$attrs"
      :placeholder="placeholder"
      :value="modelValue"
      class="mt-1 p-4 w-full bg-[#262d3b] border-2 border-solid border-secondary rounded-md shadow-sm focus:outline-none text-[#d9dce0] placeholder-[#949AA6]"
      @input="$emit('update:modelValue', $event.target.value)"
      aria-describedby="error ? `${uuid}-error` : null"
      :id="uuid"
      :aria-invalid="error ? true : null"
      :arial-required="required ? true : null"
      :required="required"
    />
    <div
      v-if="error"
      class="errorMessage text-white"
      :id="`${uuid}-error`"
      aria-live="assertive"
    >
      {{ error }}
    </div>
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
    placeholder: {
      type: String,
      default: "",
    },
    modelValue: {
      type: [String, Number],
      default: "",
    },
    error: {
      type: String,
      default: "",
    },
    required: {
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

<style></style>
