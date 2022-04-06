import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'daohang',
    component: () => import('../views/DaoHang.vue')
  },
  {
    path: '/mapuse',
    name: 'mapuse',
    component: () => import('../views/MapUse.vue')
  },
  {
    path: '/maptest',
    name: 'maptest',
    component: () => import('../views/MapTest.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
