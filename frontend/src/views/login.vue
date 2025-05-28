<script setup>

import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const message = ref('')
const router = useRouter()

const login = async (e) => {
  e.preventDefault()

  try {
    const response = await axios.post('http://127.0.0.1:5000/api/login', {
      username: username.value,
      password: password.value
    })

    if (response.data.success) {
        localStorage.setItem('isAuthenticated', 'true') // <- ajoute ceci

        router.push('/student')
    } else {
      message.value = 'Identifiants invalides.'
    }
  } catch (error) {
    console.error(error)
    message.value = 'Erreur serveur ou de connexion.'
  }
}
</script>

<template>
  <div>
    <p>/login view/</p>

    <form @submit="login">
      <label>Nom d'utilisateur</label><br>
      <input type="text" v-model="username" placeholder="username" required><br>

      <label>Mot de passe</label><br>
      <input type="password" v-model="password" placeholder="password" required><br>

      <input type="submit" value="Se connecter">
    </form>

    <p style="color: red; margin-top: 1rem">{{ message }}</p>
  </div>
</template>
