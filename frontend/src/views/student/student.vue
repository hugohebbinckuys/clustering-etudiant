<script setup>

// let count = 0
let count = 5

// function qui au clique ajoute a une liste les elements un  par un pour concserver le rang 
// const addToList = () => {

// }

</script>

<template>
    <p> / student / </p>
    <p v-if="count==0"> Pas de Form acutellement </p>
    <form v-else v-for="elt in count">
        <input type="checkbox" onclick="addToLit(elt)"> etudiant n°{{ elt }}
    </form>
</template>