<template>
  <div class="mapwrap">
    <div class="results-container">
      <app-sidebar @zoomToLocation="zoomToLocation"></app-sidebar>
    </div>
    <div id="map"></div>
  </div>
</template>

<script>
import Sidebar from './Sidebar/Sidebar'
import { mapState } from 'vuex'
import * as L from 'leaflet'
import * as LeafImage from '../assets/images/leaf.png'

const leafIcon = L.icon({
  iconUrl: LeafImage,
  iconSize: [32, 37],
  iconAnchor: [16, 37],
  popupAnchor: [0, -28]
})

export default {
  name: 'Map',
  props: ['location'],
  components: {
    appSidebar: Sidebar
  },
  data() {
    return {
      locationMarker: null,
      map: null,
      storeLayer: null
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
    initMap() {
      const map = L.map('map', { zoomControl: false }).setView(this.location, 18)

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
      if (this.storeLayer !== null) {
        this.map.removeLayer(this.storeLayer)
      }

      // Lat - Lon are vice versa from Django -> Leaflet
      const storePoints = this.stores.map(store => {
        const popup = `<p>${store.name}<br/>${store.address}</p>`
        const marker = L.marker([store.location.coordinates[1], store.location.coordinates[0]], { icon: leafIcon }).bindPopup(popup)
        return marker
      })
      this.storeLayer = L.layerGroup(storePoints)
      this.map.addLayer(this.storeLayer)
    },
    placeLocationMarker() {
      if (this.locationMarker !== null) {
        this.map.removeLayer(this.locationMarker)
      }
      this.locationMarker = L.marker(this.location).addTo(this.map)
      this.map.panTo(this.location)
    },
    zoomToLocation(coords) {
      this.map.setView([coords[1], coords[0]], 20)
    }
  },
  watch: {
    location() {
      this.placeLocationMarker()
    },
    stores() {
      this.placeStoreMarkers()
    }
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
