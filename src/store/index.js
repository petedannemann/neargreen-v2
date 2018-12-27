import Vue from 'vue'
import Vuex from 'vuex'
import stores from './modules/stores'
import auth from './modules/auth'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    stores,
    auth
  }
})
