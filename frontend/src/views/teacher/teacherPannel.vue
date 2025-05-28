<script setup> 

let FormList = [1, 2, 3]


</script>

<template>
<p v-if="FormList.length > 0">
    voici la liste de vos forms : 
</p>
<ul>
    <li v-for="elt in FormList">
        {{ elt }} 
    </li>
</ul>

</template>