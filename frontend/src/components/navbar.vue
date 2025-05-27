<script setup>
const connected = 1; 
</script>

<template>
    <router-link to="/"> LOGO </router-link>
    <input type="submit" v-if="connected" value="logout">
    <p> / navbar /</p>
    
    /* implémenter logout */
    <hr>
</template>