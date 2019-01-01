<template>
  <div class="modal-mask">
    <div class="modal-wrapper">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add a Post</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true" @click="$emit('close')">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                <label for="post-title" class="col-form-label">Title:</label>
                <input type="text" class="form-control" id="post-title" v-model="title">
              </div>
              <div class="form-group">
                <label for="content-text" class="col-form-label">Content:</label>
                <textarea class="form-control" id="content-text" v-model="content"></textarea>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="$emit('close')">Close</button>
            <button
              type="button"
              class="btn btn-primary"
              @click="addPost(title, content); $emit('close')"
            >Submit</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Post',
  data() {
    return {
      title: '',
      content: ''
    }
  },
  methods: {
    addPost(title, content) {
      const payload = {
        title, content
      }
      this.$store.dispatch('posts/addPost', payload)
    }
  }
}
</script>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
</style>
