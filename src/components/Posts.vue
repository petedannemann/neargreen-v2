<template>
  <div>
    <div class="post" v-for="(post, index) in posts" :key="index">
      <app-post v-bind:post="post"></app-post>
    </div>
    <button
      id="show-modal"
      class="btn btn-primary"
      v-if="status === 'success'"
      @click="showModal = true"
    >Add a Post</button>
    <div v-if="showModal">
      <transition name="modal">
        <app-add-post v-if="showModal" @close="showModal = false"></app-add-post>
      </transition>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Post from './Post'
import AddPost from './AddPost'

export default {
  name: 'Posts',
  data() {
    return {
      showModal: false
    }
  },
  computed: mapState({
    posts: state => state.posts.posts,
    status: state => state.auth.status,
    user: state => state.auth.user
  }),
  mounted() {
    this.$store.dispatch('posts/getPosts')
  },
  components: {
    appPost: Post,
    appAddPost: AddPost
  }
}
</script>

<style scoped>
</style>
