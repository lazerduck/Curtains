<template>
  <div id="app">
    <DataStream />
    <Controls />
  </div>
</template>

<script>
import DataStream from './components/DataStream.vue';
import Controls from './components/Controls.vue';

export default {
  name: 'App',
  components: {
    DataStream,
    Controls,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
