<script setup>
import { ref } from 'vue';

const student_total = ref(7);
const nb_points = ref(100);


const pointsByEtudiants = ref(Array(student_total.value).fill(0));
// ici on a créé un tableau de zéros basé sur le nb d(etudiant 

const incrementer = (index) => {
  if (nb_points.value > 0) {
    pointsByEtudiants.value[index]++;
    nb_points.value--;
  }
};

const decrementer = (index) => {
  if (pointsByEtudiants.value[index] > 0) {
    pointsByEtudiants.value[index]--;
    nb_points.value++;
  }
};
</script>

<template>
  <p v-if="student_total === 0">Pas de Form actuellement</p>

  <div v-else>
    <p>Nombre de points a allouer : {{ nb_points }}</p>

    <form v-for="(elt, index) in student_total" :key="index">
      <label>Étudiant n°{{ index + 1 }}</label>
      <input type="number" :value="pointsByEtudiants[index]" readonly />

      <button type="button" :disabled="nb_points <= 0" @click="incrementer(index)">+</button>
      <button type="button" :disabled="pointsByEtudiants[index] <= 0" @click="decrementer(index)">-</button>
    </form>
  </div>
  <button> envoyer </button>

</template>
