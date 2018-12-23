<template>
  <div>
    <p class="post-author" v-html="post.user"></p>
    <p class="post-title" v-html="post.title"></p>
    <p class="post-content" v-html="post.content"></p>
    <input
      type="submit"
      value="Delete"
      v-if="post.user.username == user.username && post.user.username"
      @click="deletePost(p.pk)"
    >
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Post',
  props: ['post'],
  computed: mapState({
    user: state => state.auth.user
  }),
  methods: mapActions('posts', [
    'deletePost'
  ]),
}
</script>
