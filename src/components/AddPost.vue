<template>
  <div>
    <input type="text" placeholder="Hello" v-model="title">
    <p>Post</p>
    <input type="text" placeholder="From the other side" v-model="content">
    <br>
    <br>
    <input type="submit" value="Add" @click="addPost" :disabled="!title || !content">
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      content: ''
    };
  },
  methods: {
    addPost() {
      const payload = { title: this.title, content: this.content }
      this.$backend.$addPost(payload).then(() => {
        this.title = ''
        this.content = ''
      })
    }
  }
}
</script>
