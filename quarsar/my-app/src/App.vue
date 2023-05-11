<template>

  <div class="q-pa-md">
    <bmi-calculator />
  </div>
</template>

<script>
/* eslint-disable */
import BMICalculator from './components/BMICalculator.vue';

export default {
  components: {
    BMICalculator
  }
};
</script>


<!-- 12:5  error  The "BMICalculator" component has been registered but not used  -->
<!--  ADD disable warning /* eslint-disable */ -->
<!--  running but not work /* eslint-disable */ -->
