<template>
  <div id="app">
    <app-header></app-header>
    <app-posts></app-posts>
    <!-- <router-link :to="{ name: 'home' }">Home</router-link> -->
  </div>
</template>

<style>
</style>

<script>
import Header from '@/components/Header'
import Posts from '@/components/Posts'

export default {
  components: {
    appHeader: Header,
    appPosts: Posts
    // appPosts: Posts
  }
};
</script>
