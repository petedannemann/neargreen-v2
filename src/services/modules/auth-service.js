import api from '@/services/api'

export default {
  register(payload) {
    return api.post('register/', payload).then(response => response.data)
  },
  login(payload) {
    return api
      .post(`auth/login/`, payload)
      .then(response => response.data)
      .catch(err => console.log(err))
  }
}
