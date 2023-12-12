<template>
  <div class="bg-primary h-[97vh] w-full relative">
    <MultiFormStepper :currentStep="currentStep" />
    <form
      @submit="submit"
      class="w-full h-full flex justify-center items-center"
    >
      <transition name="fade">
        <AppDescription v-if="currentStep === 0" />
      </transition>
      <transition name="fade">
        <div
          v-if="currentStep === 1"
          class="w-[80%] h-[70%] flex flex-col justify-center items-center"
        >
          <div class="mb-4 grid grid-cols-2 gap-10 w-full">
            <BaseInput
              :modelValue="firstName"
              placeholder="Please enter your first name"
              label="First name"
              type="text"
              name="firstName"
              :error="errors.firstName"
              :required="true"
              @change="handleChange"
            />
            <BaseInput
              :modelValue="lastName"
              placeholder="Please enter your last name"
              label="Last name"
              type="text"
              name="lastName"
              :error="errors.lastName"
              :required="true"
              @change="handleChange"
            />
          </div>
          <div class="mb-4 grid grid-cols-2 gap-10 w-full">
            <BaseInput
              :modelValue="age"
              placeholder="Please enter your age"
              label="Age"
              type="number"
              name="age"
              :error="errors.age"
              :required="true"
              @change="handleChange"
            />
            <BaseSelect
              :modelValue="gender"
              placeholder="Please select your gender"
              label="Gender"
              name="gender"
              :error="errors.gender"
              :required="true"
              @change="handleChange"
              :options="['Male', 'Female']"
            />
          </div>
          <div class="mb-4 grid grid-cols-1 w-full">
            <BaseInput
              :modelValue="email"
              placeholder="Please enter your email"
              label="Email"
              type="email"
              name="email"
              :error="errors.email"
              :required="true"
              @change="handleChange"
            />
          </div>
        </div>
      </transition>
      <transition name="fade">
        <div
          v-if="currentStep === 2"
          class="w-[50%] h-[70%] flex flex-col justify-center items-center"
        >
          <div class="w-full mb-8">
            <BaseRadioGroup
              :modelValue="hypertension"
              label="Have you ever been
            diagnosed with hypertension or high blood pressure?"
              name="hypertension"
              :error="errors.hypertension"
              :required="true"
              @change="handleChange"
              :vertical="true"
              :in-vertical="false"
              :options="[
                { label: 'Yes', value: 1 },
                { label: 'No', value: 0 },
              ]"
            />
          </div>
          <div class="mb-8 w-full">
            <BaseRadioGroup
              :modelValue="heartDisease"
              label="Have you ever been
            diagnosed with any heart disease?"
              name="heartDisease"
              :error="errors.heartDisease"
              :required="true"
              @change="handleChange"
              :vertical="true"
              :in-vertical="false"
              :options="[
                { label: 'Yes', value: 1 },
                { label: 'No', value: 0 },
              ]"
            />
          </div>
          <div class="w-full">
            <BaseRadioGroup
              :modelValue="diabetes"
              label="Have you ever been
            diagnosed with diabetes?"
              name="diabetes"
              :error="errors.diabetes"
              :required="true"
              :in-vertical="false"
              @change="handleChange"
              :vertical="true"
              :options="[
                { label: 'Yes', value: 1 },
                { label: 'No', value: 0 },
              ]"
            />
          </div>
        </div>
      </transition>
      <transition name="fade">
        <div
          v-if="currentStep === 3"
          class="w-[80%] h-[70%] flex flex-col justify-center items-center"
        >
          <div class="mb-4 grid grid-cols-2 gap-10 w-full">
            <BaseSelect
              :modelValue="smokingHistory"
              label="Smoking History"
              name="smokingHistory"
              :error="errors.smokingHistory"
              :required="true"
              @change="handleChange"
              :options="[
                'not current',
                'former',
                'No Info',
                'current',
                'never',
                'ever',
              ]"
            />
            <BaseInput
              :modelValue="bmi"
              placeholder="Please enter your BMI information"
              label="BMI"
              type="number"
              name="bmi"
              :error="errors.bmi"
              :required="true"
              @change="handleChange"
            />
          </div>
          <div class="mb-4 grid grid-cols-2 gap-10 w-full">
            <BaseInput
              :modelValue="hbA1cLevel"
              placeholder="What's your Hemoglobin A1c Level"
              label="Hemoglobin A1c Level"
              type="number"
              name="hbA1cLevel"
              :error="errors.hbA1cLevel"
              :required="true"
              @change="handleChange"
            />
            <BaseInput
              :modelValue="bloodGlucoseLevel"
              placeholder="Please enter blood glucose level"
              label="Blood Glucose Level"
              type="number"
              name="bloodGlucoseLevel"
              :error="errors.bloodGlucoseLevel"
              :required="true"
              @change="handleChange"
            />
          </div>
        </div>
      </transition>
      <StepperNavigation
        @next="nextStep"
        @prev="prevStep"
        :currentStep="currentStep"
      />
    </form>
    <pre class="text-white">{{ errors }}</pre>
  </div>
</template>

<script>
import axios from "axios";
import { useField, useForm } from "vee-validate";
import * as yup from "yup";
import { ref, inject } from "vue";
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
  setup() {
    const swal = inject("$swal");
    const initialValue = ref({});

    const currentStep = ref(0);
    const maxStep = 3;
    const minStep = 0;

    // Define methods
    const submitHandler = (payload) => {
      console.log(payload);
    };

    const nextStep = () => {
      if (currentStep.value < maxStep) {
        currentStep.value++;
      }
    };

    const prevStep = () => {
      if (currentStep.value > minStep) {
        currentStep.value--;
      }
    };

    const validationSchema = yup.object({
      firstName: yup.string().required().min(3).max(100),
      lastName: yup.string().required().min(3).max(100),
      gender: yup.string().oneOf(["Male", "Female", "Others"]).ensure(),
      age: yup.number().required(),
      email: yup.string().email().required(),
      hbA1cLevel: yup.number(),
      smokingHistory: yup.string(),
      bloodGlucoseLevel: yup.number(),
      bmi: yup.number(),
    });

    const { handleSubmit, errors, setFieldValue, resetForm } = useForm({
      validationSchema,
      initialValues: {
        firstName: "",
        lastName: "",
        gender: "",
        age: 0,
        email: "",
        hypertension: 0,
        heartDisease: 0,
        diabetes: 0,
        hbA1cLevel: "",
        smokingHistory: "",
        bmi: "",
        bloodGlucoseLevel: "",
      },
    });

    const { value: firstName } = useField("firstName");
    const { value: lastName } = useField("lastName");
    const { value: age } = useField("age");
    const { value: gender } = useField("gender");
    const { value: email } = useField("email");
    const { value: hypertension } = useField("hypertension");
    const { value: heartDisease } = useField("heartDisease");
    const { value: diabetes } = useField("diabetes");
    const { value: hbA1cLevel } = useField("hbA1cLevel");
    const { value: bmi } = useField("bmi");
    const { value: smokingHistory } = useField("smokingHistory");
    const { value: bloodGlucoseLevel } = useField("bloodGlucoseLevel");

    const handleChange = ({ target }) => {
      setFieldValue(target.name, target.value);
    };

    const submit = handleSubmit((values) => {
      const {
        heartDisease,
        hbA1cLevel,
        smokingHistory,
        bloodGlucoseLevel,
        age,
        bmi,
        diabetes,
        ...rest
      } = values;

      axios
        .post("http://localhost:5000/api/diabetic-checker", {
          ...rest,
          age: +age,
          bmi: +bmi,
          heart_disease: +heartDisease,
          HbA1c_level: +hbA1cLevel,
          smoking_history: smokingHistory,
          blood_glucose_level: +bloodGlucoseLevel,
          diabetes: +diabetes,
        })
        .then((response) => {
          if (response.status === 200) {
            console.log(response);
            swal({
              icon: "success",
              title: response.data.message,
              showConfirmButton: false,
              timer: 8500,
            });
          }

          setTimeout(() => {
            currentStep.value = 0;
            resetForm();
          }, 2000);
        })
        .catch((err) => {
          swal({
            icon: "error",
            title: err.message,
            showConfirmButton: false,
            timer: 1500,
          });
        });
    });

    // Return variables and methods for use in the template
    return {
      initialValue,
      currentStep,
      maxStep,
      minStep,
      submitHandler,
      nextStep,
      prevStep,
      firstName,
      lastName,
      age,
      gender,
      email,
      heartDisease,
      hypertension,
      diabetes,
      hbA1cLevel,
      smokingHistory,
      bloodGlucoseLevel,
      bmi,
      errors,
      submit,
      handleChange,
    };
  },
};
</script>

<style>
.fade-enter-from {
  opacity: 0;
}

.fade-enter-active {
  transition: all cubic-bezier(0.25, 0.46, 0.45, 0.94) ease;
}

.fade-leave-to {
  opacity: 0;
}

.fade-leave-active {
  transition: all cubic-bezier(0.25, 0.46, 0.45, 0.94) ease;
}
</style>
