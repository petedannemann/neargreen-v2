import api from '@/services/api'

export default {
  fetchStores(payload) {
    return api.get(`stores/`, payload).then(response => response.data.results)
  }
}
