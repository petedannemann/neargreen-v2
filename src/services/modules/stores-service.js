import api from '@/services/api'

export default {
  fetchStores() {
    return api.get(`stores/`).then(response => response.data.results)
  }
}
