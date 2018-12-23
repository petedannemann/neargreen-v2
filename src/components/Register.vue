<template>
  <div class="modal-mask">
    <div class="modal-wrapper">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Register</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true" @click="$emit('close')">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                <label for="username" class="col-form-label">Username</label>
                <input type="text" class="form-control" id="username" v-model="username">
              </div>
              <div class="form-group">
                <label for="email" class="col-form-label">Email</label>
                <input type="text" class="form-control" id="email" v-model="email">
              </div>
              <div class="form-group">
                <label for="password" class="col-form-label">Password</label>
                <input type="password" class="form-control" id="password" v-model="password1">
              </div>
              <div class="form-group">
                <label for="password-confirm" class="col-form-label">Confirm Password</label>
                <input
                  type="password"
                  class="form-control"
                  id="password-confirm"
                  v-model="password2"
                >
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="$emit('close')">Close</button>
            <button
              type="button"
              class="btn btn-primary"
              @click="register(username, email, password1, password2); $emit('close')"
            >Register</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
      username: '',
      email: '',
      password1: '',
      password2: ''
    }
  },
  methods: {
    register(username, email, password1, password2) {
      const payload = {
        username,
        email,
        password1,
        password2
      }
      this.$store.dispatch('auth/register', payload)
    }
  }
}
</script>

<style scoped>
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
