import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/views/Home.vue"),
  },
  {
    path: "/signup",
    name: "Signup",
    component: () => import("@/views/signup.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("@/views/Login.vue"),
  },
  {
    path: "/orders",
    name: "Orders",
    component: () => import("@/views/orders.vue"),
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
