import Vue from 'vue'
import Router from 'vue-router'
import Posts from '@/components/Posts'
import AddPost from '@/components/AddPost'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      components: [Posts, AddPost]
    }
  ]
})
