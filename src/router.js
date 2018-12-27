import Vue from 'vue'
import Router from 'vue-router'
import Stores from '@/components/Stores'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Stores
    }
  ]
})
