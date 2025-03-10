<template>
  <div class="auth-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <input type="email" v-model="email" placeholder="Email" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import { ref } from "vue";
import { login } from "@/services/api.js";

export default {
  setup() {
    const email = ref("");
    const password = ref("");
    const error = ref("");

    const handleLogin = async () => {
      try {
        const response = await login(email.value, password.value);
        alert("Login successful!");
      } catch (err) {
        error.value = err.response?.data?.message || "Login failed!";
      }
    };


    return { email, password, handleLogin, error };
  },
};
</script>

<style scoped>
.auth-container { max-width: 300px; margin: auto; }
input { display: block; margin: 10px 0; padding: 8px; width: 100%; }
button { background: #42b883; color: white; border: none; padding: 10px; cursor: pointer; }
.error { color: red; }
</style>
