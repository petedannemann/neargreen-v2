<template>
  <div id="app">
    <app-header></app-header>
    <div class="container-fluid">
      <div class="text-center">
        <div class="stores-container">
          <app-stores></app-stores>
        </div>
        <div class="map-container">
          <div class="col-lg-6 col-lg-offset-5">
            <app-map class="map"></app-map>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.stores-container {
  background-color: white;
  overflow: hidden;
  border: none;
  width: 300px;
  height: 600px;
  margin-left: 317px;
}

.stores-container-scrollable {
  overflow-x: hidden;
  overflow-y: scroll;
}

.map {
  min-width: 200px;
  min-height: 600px;
  height: 500px;
  width: 500px;
}

.map-container {
  margin-left: 24px;
  margin-right: auto;
  margin-top: -600px;
}
</style>

<script>
import Header from '@/components/Header'
import Stores from '@/components/Stores'
import _Map from '@/components/Map'

export default {
  components: {
    appHeader: Header,
    appStores: Stores,
    appMap: _Map
  }
}
</script>
