import authService from '../../services/modules/auth-service'
// import api from '../../services/api'
import { reject } from 'assert'

const state = {
  status: '',
  token: localStorage.getItem('token') || '',
  user: {}
}

const actions = {
  register({ commit }, payload) {
    authService
      .register(payload)
      .then(data => {
        commit('authSuccess', { token: data.key, user: payload })
      })
      .catch(err => {
        commit('authError')
        reject(err)
      })
  },
  login({ commit }, payload) {
    authService
      .login(payload)
      .then(data => {
        commit('authSuccess', { token: data.key, user: payload })
      })
      .catch(err => {
        commit('authError')
        reject(err)
      })
  },
  logout({ commit }) {
    commit('logout')
  }
}

const mutations = {
  authSuccess(state, payload) {
    localStorage.setItem('token', payload.token)
    state.status = 'success'
    state.token = payload.token
    state.user = payload.user
  },
  authError(state) {
    localStorage.removeItem('token')
    state.status = 'error'
  },
  logout(state) {
    localStorage.removeItem('token')
    state.status = ''
    state.token = ''
    state.user = {}
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}
