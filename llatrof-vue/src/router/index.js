import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPageView from '@/views/MainPageView'
import MyTest from '@/views/MyTest'
import CategoryPageView from '@/views/CategoryPageView'
import BrandPageView from '@/views/BrandPageView'

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
  },
  {
    path: '/category/:categoryName',
    name: 'category',
    component: CategoryPageView
  },
  {
    path: '/brand/:brandName',
    name: 'brand',
    component: BrandPageView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
