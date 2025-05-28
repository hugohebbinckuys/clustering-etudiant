<script setup>
import { ref } from 'vue'
import axios from 'axios'

const openAt = ref('')
const closedAt = ref('')
const choiceNumber = ref(1)
const message = ref('')

const submitForm = async () => {
  try {
    const response = await axios.post('http://localhost:5000/api/forms', {
      open_at: openAt.value,
      closed_at: closedAt.value,
      choice_number: choiceNumber.value,
    })

    if (response.status === 200 || response.status === 201) {
      message.value = 'Formulaire créé avec succès !'
      openAt.value = ''
      closedAt.value = ''
      choiceNumber.value = 1
    } else {
      message.value = 'Erreur lors de la création du formulaire.'
    }
  } catch (error) {
    console.error(error)
    message.value = 'Erreur serveur.'
  }
}
</script>

<template>
  <div class="form-container">
    <h2>Créer un formulaire</h2>
    <form @submit.prevent="submitForm">
      <label for="open">Date d'ouverture :</label>
      <input type="datetime-local" id="open" v-model="openAt" required />

      <label for="closed">Date de fermeture :</label>
      <input type="datetime-local" id="closed" v-model="closedAt" required />

      <label for="choice">Nombre de choix possibles :</label>
      <input type="number" id="choice" v-model="choiceNumber" min="1" required />

      <button type="submit">Créer</button>
    </form>

    <p>{{ message }}</p>
  </div>
</template>
