import api from '@/services/api'
import authApi from '@/services/auth-api'

export default {
  fetchPosts() {
    return api.get(`posts/`).then(response => response.data)
  },
  addPost(payload) {
    return authApi
      .post(`posts/`, payload)
      .then(response => response.data)
      .catch(err => console.log(err))
  },
  deletePost(postId) {
    return authApi.delete(`posts/${postId}`).then(response => response.data)
  }
}
