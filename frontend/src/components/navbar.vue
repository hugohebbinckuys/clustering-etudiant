<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const isAuthenticated = localStorage.getItem('isAuthenticated') === 'true'
const logout = () => {
  localStorage.removeItem('isAuthenticated') 
  router.push('/login') 
}

</script>

<template>
    <router-link to="/"> LOGO </router-link>
    <button @click="logout()" v-if="isAuthenticated" value="logout"> logout </button>
    <p> / navbar /</p>
    <p v-if="isAuthenticated"> Utilisateur connecté </p>
    <p v-else> Utilisateur déconnecté </p>
    
    /* implémenter logout */
    <hr>
</template>