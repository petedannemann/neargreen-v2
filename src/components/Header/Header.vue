<template>
  <div>
    <nav class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">
            <img id="neargreenLogo" src="../../assets/images/neargreenlogo.png" alt>
          </a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <form class="navbar-form navbar-left" role="search">
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Search">
            </div>
          </form>
          <ul class="nav navbar-nav navbar-right" v-if="status !== 'success'">
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
          <ul class="nav navbar-nav navbar-right" v-else>
            <li class="dropdown">
              <a href="/profile" class="dropdown-toggle" data-toggle="dropdown">
                <b>Logged in as {{ user.username }}</b>
                <span class="caret"></span>
              </a>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" @click="logout">
                <b>Logout</b>
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
import { mapState } from 'vuex'

import Register from './Register'
import Login from './Login'

export default {
  data() {
    return {
      showRegisterModal: false,
      showLoginModal: false
    }
  },
  computed: mapState({
    status: state => state.auth.status,
    user: state => state.auth.user
  }),
  methods: {
    logout() {
      this.$store.dispatch('auth/logout')
    }
  },
  components: {
    appRegister: Register,
    appLogin: Login
  }
}
</script>

<style scoped>
.navbar-default {
  background-color: #d7f0cf;
  border-color: #e7e7e7;
}

#neargreenLogo {
  width: 64px;
  height: 42px;
  margin-top: -15px;
}
</style>

