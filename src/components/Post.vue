<template>
  <div>
    <p class="post-author" v-html="post.user"></p>
    <p class="post-title" v-html="post.title"></p>
    <p class="post-content" v-html="post.content"></p>
    <input
      type="submit"
      value="Delete"
      v-if="post.user == user.username && post.user"
      @click="deletePost(post.pk)"
    >
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Post',
  props: ['post'],
  computed: mapState({
    user: state => state.auth.user
  }),
  methods: {
    deletePost(postId) {
      this.$store.dispatch('posts/deletePost', postId)
    }
  }
}
</script>
