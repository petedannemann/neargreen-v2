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
      location: [39.9523893, -75.1636291]
    }
  },
  beforeMount() {
    this.getLocation()
  },
  mounted() {
    this.$store.dispatch('stores/getStores', { latitude: this.location[0], longitude: this.location[1] })
  },
  methods: {
    zoomToLocation(coordinates) {
      this.location = coordinates
    },
    getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
          this.location = [position.coords.latitude, position.coords.longitude]
        })
      }
    }
  }
}
</script>
