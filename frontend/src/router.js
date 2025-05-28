import { createRouter, createWebHistory } from "vue-router";
import login from "./views/login.vue";
import register from "./views/register.vue";
import student from "./views/student/student.vue";

const routes = [
    { path: '/login', name: 'Login', component: login}, 
    { path: '/register', name: 'Register', component: register}, 
    { path: '/student', name: 'Student', component: student, meta: { requiresAuth: true } }, 
]; 

const router = createRouter({
    history: createWebHistory(), 
    routes,
}); 

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('isAuthenticated') === 'true'

  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login') 
  } else {
    next() 
  }
})

export default router; 