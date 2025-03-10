<template>
  <nav>
    <router-link to="/signup">Signup</router-link>
    <router-link to="/login">Login</router-link>
    <router-link to="/orders">Orders</router-link>
  </nav>
  <router-view></router-view>
</template>

<style>
nav { display: flex; gap: 20px; padding: 10px; background: #f0f0f0; }
</style>
