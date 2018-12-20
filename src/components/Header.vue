<template>
  <div>
    <nav class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">Instamap</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <form class="navbar-form navbar-left" role="search">
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Search">
            </div>
          </form>
          <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
              <a
                href="#"
                class="dropdown-toggle"
                data-toggle="dropdown"
                @click="showRegisterModal = true"
              >
                <b>Register</b>
                <span class="caret"></span>
              </a>
            </li>
            <li class="dropdown">
              <a
                href="#"
                class="dropdown-toggle"
                data-toggle="dropdown"
                @click="showLoginModal = true"
              >
                <b>Login</b>
                <span class="caret"></span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div v-if="showRegisterModal">
      <transition name="modal">
        <app-register v-if="showRegisterModal" @close="showRegisterModal = false"></app-register>
      </transition>
    </div>
    <div v-if="showLoginModal">
      <transition name="modal">
        <app-login v-if="showLoginModal" @close="showLoginModal = false"></app-login>
      </transition>
    </div>
  </div>
</template>

<script>
import Register from './Register'
import Login from './Login'

export default {
  data() {
    return {
      showRegisterModal: false,
      showLoginModal: false
    }
  },
  components: {
    appRegister: Register,
    appLogin: Login
  }
}
</script>

<style scoped>
</style>

