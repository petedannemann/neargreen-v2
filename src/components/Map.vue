<template></template>

<script>
import { mapState } from 'vuex'
import * as L from 'leaflet'

export default {
  name: 'Map',
  props: ['location'],
  data() {
    return {
      defaultLocation: [39.9523893, -75.1636291],
      locationMarker: null,
      map: null,
    }
  },
  computed: mapState({
    stores: state => state.stores.stores
  }),
  mounted() {
    this.map = this.initMap()
    this.addBasemap()
    this.placeLocationMarker()
    this.placeStoreMarkers()
  },
  methods: {
    getLocation() {
      return this.location || this.defaultLocation;
    },
    initMap() {
      return L.map(this.$el).setView(this.getLocation(), 18)
    },
    addBasemap() {
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(this.map)
    },
    placeStoreMarkers() {
      let storeFeatures = []
      this.stores.forEach(store => {
        storeFeatures.push(L.marker([store.location.coordinates[1], store.location.coordinates[0]]))
      })
      L.featureGroup(storeFeatures).addTo(this.map)
    },
    placeLocationMarker() {
      const location = this.getLocation()
      if (this.locationMarker !== null) {
        this.map.removeLayer(this.locationMarker)
      }
      this.locationMarker = L.marker(location).addTo(this.map)
      this.map.panTo(location)
    },
  },
  watch: {
    location() {
      this.placeLocationMarker()
    },
  }
}
</script>