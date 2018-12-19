<template>
  <div id="app">
    <app-header></app-header>
    <!-- <app-posts :posts="posts"></app-posts> -->
    <router-link :to="{ name: 'home' }">Home</router-link>
    <router-link :to="{ name: 'addpost' }">Add Post</router-link>
    <router-view/>
  </div>
</template>

<style>
</style>

<script>
import Header from "@/components/Header";
// import Posts from "@/components/Posts";

export default {
  components: {
    appHeader: Header
    // appPosts: Posts
  }
};
</script>
