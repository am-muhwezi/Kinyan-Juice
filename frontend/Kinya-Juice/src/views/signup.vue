<template>
  <div class="auth-container">
    <h2>Signup</h2>
    <form @submit.prevent="handleSignup">
      <input type="text" v-model="fullname" placeholder="Full Name" required />
      <input type="email" v-model="email" placeholder="Email" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Signup</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>


<script>
import { ref } from "vue";
import { useRouter } from "vue-router"; // ✅ Import router for navigation
import { signup } from "@/services/api.js";

export default {
  setup() {
    const fullname = ref("");
    const email = ref("");
    const password = ref("");
    const error = ref("");
    const router = useRouter(); // ✅ Initialize router

    const handleSignup = async () => {
      try {
        await signup({ fullname: fullname.value, email: email.value, password: password.value });

        alert("Signup successful! Redirecting to login...");
        router.push("/login"); // ✅ Redirect to login page
      } catch (err) {
        error.value = err.response?.data?.message || "Signup failed!";
      }
    };

    return { fullname, email, password, handleSignup, error };
  },
};
</script>

<style scoped>
.auth-container { max-width: 300px; margin: auto; }
input { display: block; margin: 10px 0; padding: 8px; width: 100%; }
button { background: #42b883; color: white; border: none; padding: 10px; cursor: pointer; }
.error { color: red; }
</style>
