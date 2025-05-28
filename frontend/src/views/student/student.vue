<script setup>
import { ref } from 'vue';

// let count = 0
const student_total = ref(5)
const nb_points = ref(100) 

// function qui au clique ajoute a une liste les elements un  par un pour concserver le rang 
// const addToList = () => {

// }

// const pointManager = (number) => {
//     nb_points.value -= number
// }
const incrementer = () => {
    nb_points.value ++; 
}
const decrementer = () => {
    nb_points.value --; 
}

</script>

<template>
    <p> / student / </p>

    <p v-if="student_total==0"> Pas de Form acutellement </p>
    <div v-if="student_total>0">
        <p> number to allocate : {{ nb_points }}</p>
        <form v-for="elt in student_total">
            <input type="text"> etudiant n°{{ elt }}
            <input type="number" v-model="number" placeholder="points pour l'étudiant"> <span> <button :disabled="nb_points<=0" @click="decrementer()" value="number"> - </button> <button :disabled="nb_points>=100" @click="incrementer()" value="number"> + </button></span>
        </form>
    </div>
</template>