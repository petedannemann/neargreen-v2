<template>
  <div>
    <hr>
    <h3>Posts on Database</h3>
    <p v-if="posts.length === 0">No Posts</p>
    <div class="post" v-for="(p, index) in posts" :key="index">
      <p class="post-index">[{{ index }}]</p>
      <p class="post-title" v-html="p.title"></p>
      <p class="post-content" v-html="p.content"></p>
      <input type="submit" @click="deletePost(p.pk)" value="Delete">
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Posts',
  computed: mapState({
    posts: state => state.posts.posts
  }),
  methods: mapActions('posts', [
    'deletePost'
  ]),
  mounted() {
    this.$store.dispatch('posts/getPosts')
  }
}
</script>

<style scoped>
</style>
