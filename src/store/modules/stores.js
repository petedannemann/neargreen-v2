import storeService from '../../services/modules/stores-service'

const state = {
  stores: []
}

const getters = {
  stores: state => {
    return state.stores
  }
}

const actions = {
  async getStores({ commit }, payload) {
    storeService.fetchStores(payload).then(stores => {
      commit('setStores', stores)
    })
  }
}

const mutations = {
  setStores(state, stores) {
    state.stores = stores
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
