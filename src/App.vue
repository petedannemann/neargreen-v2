<template>
  <div id="app">
    <app-header @triggerZoomToLocation="zoomToLocation"></app-header>
    <div class="container-fluid">
      <div class="map-container">
        <app-map v-bind:location="location"></app-map>
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
  data() {
    return {
      location: null
    }
  },
  created() {
    this.$store.dispatch('stores/getStores')
  },
  methods: {
    zoomToLocation(coordinates) {
      this.location = coordinates
    }
  }
}
</script>
