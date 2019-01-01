<template>
  <div>
    <div class="store" v-for="(store, index) in stores" :key="index">
      <app-store v-bind:store="store"></app-store>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Store from './Store'

export default {
  name: 'Stores',
  computed: mapState({
    stores: state => state.stores.stores,
    status: state => state.auth.status,
    user: state => state.auth.user
  }),
  components: {
    appStore: Store
  }
}
</script>

<style scoped>
</style>
