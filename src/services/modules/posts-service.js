import api from "@/services/api"

export default {
  fetchPosts() {
    return api.get(`posts/`).then(response => response.data)
  },
  addPost(payload) {
    return api.post(`posts/`, payload).then(response => response.data)
  },
  deletePost(postId) {
    return api.delete(`posts/${postId}`).then(response => response.data)
  }
}
