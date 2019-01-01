<template>
  <div id="toolbar" :class="{ open: showSidebar }">
    <div class="hamburger" @click="showSidebar = !showSidebar">
      <span>Nearby&nbsp;Stores</span>
    </div>
    <div id="stores">
      <h2>Nearby Stores</h2>
      <app-stores></app-stores>
    </div>
  </div>
</template>

<script>
import Stores from './Stores'

export default {
  data() {
    return {
      showSidebar: false
    }
  },
  components: {
    appStores: Stores
  }
}
</script>

<style>
#toolbar {
  background: rgba(255, 255, 255, 1);
  opacity: 0.6;
  width: 300px;
  height: 100vh;
  position: absolute;
  left: -300px;
  z-index: 2;
  transition: 0.5s left;
  padding: 20px;
  box-sizing: border-box;
}

#toolbar.open {
  left: 0;
  opacity: 0.95;
}

#toolbar .hamburger {
  height: 100px;
  width: 25px;
  background: #000;
  box-shadow: 1px 0 2px rgba(0, 0, 0, 0.3);
  position: absolute;
  right: -25px;
  top: 40%;
  border-top-right-radius: 3px;
  border-bottom-right-radius: 3px;
  border: 1px solid #333;
  cursor: pointer;
}

.hamburger span {
  color: #fff;
  display: inline-block;
  position: relative;
  transform: rotate(90deg);
  top: 39px;
  left: -21px;
}

#stores {
  overflow-y: scroll;
  max-height: 95vh;
}

#toolbar ul {
  margin: 0;
  padding: 0;
}

#toolbar li {
  list-style-type: none;
  border-bottom: 1px solid #ccc;
  padding: 6px 3px;
  cursor: pointer;
}

#toolbar li:hover {
  color: #666;
}
</style>
