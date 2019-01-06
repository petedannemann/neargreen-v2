<template>
  <div class="row store-row">
    <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
      <div class="panel panel-primary">
        <div class="row padall">
          <div class="col-xs-12 col-sm-12 col-md-9 col-lg-9">
            <div>
              <h5>
                <strong>
                  <em>
                    <span>{{ store.name }}</span>
                  </em>
                </strong>
              </h5>
              <h5>
                <a href="#" alt="Get Directions">
                  <span>{{ store.address }}</span>
                  <br>
                  <span>
                    {{ store.distance }}
                    <span class="inline" v-if="store.distance <= 1">Mile</span>
                    <span class="inline" v-else>Miles</span>
                  </span>
                </a>
              </h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Store',
  props: ['store'],
}
</script>

<style scoped>
.map-store-icon {
  font-size: 50px;
}

.panel {
  box-shadow: none;
  width: 300px;
}

.panel-primary {
  width: 300px;
  height: 100px;
  border: none;
  border-radius: 0px;
  border-bottom: none;
  text-align: left;
}

.panel-primary a {
  text-decoration: none;
  color: #000;
}

.panel-primary:hover {
  background-color: rgba(66, 244, 69, 0.5);
  cursor: pointer;
}

.inline {
  display: inline-block;
}
</style>
