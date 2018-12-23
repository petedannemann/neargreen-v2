import postService from '../../services/modules/posts-service'

const state = {
  posts: []
}

const getters = {
  posts: state => {
    return state.posts
  }
}

const actions = {
  getPosts({ commit }) {
    postService.fetchPosts().then(posts => {
      commit('setPosts', posts)
    })
  },
  addPost({ commit }, post) {
    postService
      .addPost(post)
      .then(() => {
        commit('addPost', post)
      })
      .catch(err => {
        console.log(err)
      })
  },
  deletePost({ commit }, postId) {
    postService.deletePost(postId).then(() => {
      commit('deletePost', postId)
    })
  }
}

const mutations = {
  setPosts(state, posts) {
    state.posts = posts
  },
  addPost(state, post) {
    state.posts.push(post)
  },
  deletePost(state, postId) {
    state.posts = state.posts.filter(obj => obj.pk !== postId)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
