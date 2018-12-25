import api from '@/services/api'
import authApi from '@/services/auth-api'

export default {
  register(payload) {
    return api
      .post('register/', payload)
      .then(response => response.data)
      .catch(err => console.log(err))
  },
  login(payload) {
    return api
      .post(`auth/login/`, payload)
      .then(response => response.data)
      .catch(err => console.log(err))
  },
  logout() {
    return authApi
      .post(`auth/logout/`)
      .then(response => response.data)
      .catch(err => console.log(err))
  }
}
