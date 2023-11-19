<template>
  <div>
    <div>{{ label }}</div>
    <input
      class=""
      :type="type"
      :name="name"
      :disabled="disabled"
      :placeholder="placeholder"
      v-field-capitalize="capitalize"
      v-model="model"
    />
  </div>
</template>

<script>
export default {
  name: "InputText",
  computed: {
    model: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
        this.$emit("change", value);
      },
    },
  },
  mounted() {
    if (this.preFocus) {
      this.$refs.field.focus();
    }
  },
  props: {
    value: {
      type: String,
      default: "",
    },
    placeholder: {
      type: String,
    },
    name: {
      type: String,
      required: true,
    },
    capitalize: {
      type: Boolean,
      default: false,
    },
    label: {
      type: String,
      default: "",
    },
    type: {
      type: String,
      default: "text",
    },
    preFocus: {
      type: Boolean,
      default: false,
    },
    required: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style></style>
