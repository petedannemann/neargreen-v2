<template>
  <div id="app">
    <app-header></app-header>
    <div class="container-fluid">
      <div class="map-container">
        <app-map></app-map>
      </div>
    </div>
  </div>
</template>

<style>
.map-container {
  position: fixed;
  top: 50px;
  bottom: 0px;
  right: 0;
  left: 0;
}
</style>

<script>
import Header from '@/components/Header/Header'
import _Map from '@/components/Map'

export default {
  components: {
    appHeader: Header,
    appMap: _Map
  },
  created() {
    this.$store.dispatch('stores/getStores')
  }
}
</script>
