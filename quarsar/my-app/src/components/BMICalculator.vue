<template>
  <div>
    <h1>Calculate BMI</h1>
    <label for="weight">Weight (kg):</label>
    <input type="text" v-model="weight" id="weight"><br><br>
    <label for="height">Height (m):</label>
    <input type="text" v-model="height" id="height"><br><br>
    <q-btn label="Calculate" color="primary" @click="calculateBMI" />
    <p v-if="bmi">Your BMI is: {{ bmi }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      weight: '',
      height: '',
      bmi: null
    };
  },
  methods: {
    calculateBMI() {
      const payload = {
        weight: parseFloat(this.weight),
        height: parseFloat(this.height)
      };
      axios.post('/calculate-bmi', payload)
        .then(response => {
          this.bmi = response.data.bmi;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
