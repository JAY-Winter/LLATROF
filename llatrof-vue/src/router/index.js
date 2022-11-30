import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPageView from '@/views/MainPageView'
import MyTest from '@/views/MyTest'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'mainpage',
    component: MainPageView
  },
  {
    path: '/test',
    name: 'test',
    component: MyTest
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
