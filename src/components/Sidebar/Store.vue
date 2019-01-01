<template>
  <div>
    <p class="store-name" v-html="store.name"></p>
    <p class="store-address" v-html="store.address"></p>
    <p class="store-distance" v-html="store.distance"></p>
  </div>
</template>

<script>
export default {
  name: 'Store',
  props: ['store'],
}
</script>
