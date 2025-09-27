import { createRouter, createWebHistory } from 'vue-router'
import landing from '../views/LandingPage.vue'
import LoginView from '../views/loginView.vue'
import principalView from '../views/principalView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/', name: 'landingpage', component:landing, meta: {title: "CONTROL DE CITAS"}},
    {path: '/login', name: 'login', component: LoginView, meta: {title: "Login - Control de citas"}},
    {path: '/dashboard', name: 'dashboard', component: principalView, meta: {title: "Dashboard - Control de citas"}},
  ],
})

export default router
