import api from '@/services/api'

export default {
  fetchStores(payload) {
    return api
      .get(`stores/`, { params: payload })
      .then(response => response.data.results)
  }
}
