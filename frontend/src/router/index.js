import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import PageNotFound from '../components/PageNotFound'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect:'Home',
  },
  {
    path: '/Home',
   // name: 'Home',
    component: Home
  },
  {
    path:'*',
    name:'PageNotFound',
    component:PageNotFound
  }

 
]

const router = new VueRouter({
  routes
})

export default router
