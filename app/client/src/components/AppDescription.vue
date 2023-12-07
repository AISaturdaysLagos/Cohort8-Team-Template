<template>
  <div class="background-container">
    <div
      class="w-full md:w-[50%] bg-transparent p-4 md:p-8 absolute top-[50%] translate-y-[-50%]"
    >
      <h1 class="text-4xl tracking-[.25em] font-thin text-white mb-2">
        YOUR HEALTHY
      </h1>
      <h3
        class="text-4xl md:text-6xl tracking-[.25em] font-extrabold text-white mb-4"
      >
        OUR PRIORITY
      </h3>
      <p class="text-white font-extralight text-xs md:text-lg font-light mb-4">
        Discover your diabetic risk level with our innovative Diabetic Risk
        Assessment web application. This user-friendly tool simplifies the
        process of understanding your potential risk for diabetes. Answer a few
        quick questions, and let our advanced machine learning model analyze the
        data to provide you with personalized insights.
      </p>
      <p class="text-white text-xs font-normal italic mb-4">
        FYI: This assessment checker is not a substitute for professional
        medical diagnosis, treatments, or advice.
      </p>
      <button class="bg-[#000] text-white py-4 px-12" @click="next">
        GET STARTED
      </button>
    </div>
  </div>
</template>

<script>
export default {
  setup(_, { emit }) {
    const next = () => {
      emit("next");
    };

    return {
      next,
    };
  },
};
</script>

<style scoped>
.background-container {
  @apply w-full h-screen bg-cover;
  background-image: url("./bg.png");
  background-attachment: fixed;
  background-position: left;
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  position: relative;
}
</style>
