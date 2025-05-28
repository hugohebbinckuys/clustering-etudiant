<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref("")
const password = ref("")
const router = useRouter()

const createUser = async (event) => {
    event.preventDefault()

    try {
        const data = {
            username: username.value,
            password: password.value
        }

        const response = await axios.post("http://localhost:5000/api/users", data)  

        console.log("Utilisateur créé :", response.data)
        router.push("/student") 
    } catch (error) {
        console.error("Erreur lors de la création :", error)
        alert("Erreur dans création de l'utilisateur")
    }
}
</script>

<template>
    <p>/sign up view/</p>
    <form @submit="createUser">
        <label>Sign up</label><br>
        <input type="text" v-model="username" placeholder="username" required>
        <input type="password" v-model="password" placeholder="password" required>
        <input type="submit" value="S'inscrire">
    </form>
</template>
