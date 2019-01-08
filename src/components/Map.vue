<template>
  <div class="mapwrap">
    <div class="results-container">
      <app-sidebar @zoomToStore="onZoomToStore"></app-sidebar>
    </div>
    <div id="map"></div>
  </div>
</template>

<script>
import Sidebar from './Sidebar/Sidebar'
import { mapState } from 'vuex'
import * as L from 'leaflet'
import * as LeafImage from '../assets/images/leaf.png'

export default {
  name: 'Map',
  props: ['location'],
  components: {
    appSidebar: Sidebar
  },
  data() {
    return {
      defaultLocation: [39.9523893, -75.1636291],
      locationMarker: null,
      map: null
    }
  },
  computed: mapState({
    stores: state => state.stores.stores
  }),
  mounted() {
    this.map = this.initMap()
    this.addBasemaps()
    this.placeLocationMarker()
    this.placeStoreMarkers()
  },
  methods: {
    getLocation() {
      return this.location || this.defaultLocation
    },
    initMap() {
      const map = L.map('map', { zoomControl: false }).setView(this.getLocation(), 18)

      L.control.zoom({
        position: 'bottomright'
      }).addTo(map)

      return map
    },
    addBasemaps() {
      const streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v10/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoicGJkMjgxIiwiYSI6ImNqcThtdnR2MDAwdWMzeG1qdW00Y2wwMTcifQ.al7JyXv2B7kpvwgNNb49Bg', {
        attribution: '© <a href="https://www.mapbox.com/about/maps/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>'
      })
      const light = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NDg1bDA1cjYzM280NHJ5NzlvNDMifQ.d6e-nNyBDtmQCVwVNivz7A#2/0/0', {
        attribution: '© <a href="https://www.mapbox.com/about/maps/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>'
      })
      this.map.addLayer(streets)
      L.control.layers({ 'Streets': streets, 'Light': light }).addTo(this.map)
    },
    placeStoreMarkers() {
      // Lat - Lon are vice versa from Django -> Leaflet
      const leafIcon = L.icon({
        iconUrl: LeafImage,
        iconSize: [32, 37],
        iconAnchor: [16, 37],
        popupAnchor: [0, -28]
      })
      const storeFeatures = this.stores.map(store => {
        const popup = `<p>${store.name}<br/>${store.address}</p>`
        const marker = L.marker([store.location.coordinates[1], store.location.coordinates[0]], { icon: leafIcon }).bindPopup(popup)
        return marker
      })
      this.map.addLayer(L.layerGroup(storeFeatures))
    },
    placeLocationMarker() {
      const currentLocation = this.getLocation()
      if (this.locationMarker !== null) {
        this.map.removeLayer(this.locationMarker)
      }
      this.locationMarker = L.marker(currentLocation).addTo(this.map)
      this.map.panTo(currentLocation)
    },
    onZoomToStore(coords) {
      this.map.setView([coords[1], coords[0]], 20)
    }
  },
  watch: {
    location() {
      this.placeLocationMarker()
    },
  }
}
</script>

<style scoped>
.mapwrap {
  width: 100%;
  height: 100%;
  border: 1px solid #333;
  position: relative;
  overflow: hidden;
}

#map {
  height: 100%;
  width: 100%;
  z-index: 1;
}
</style>
