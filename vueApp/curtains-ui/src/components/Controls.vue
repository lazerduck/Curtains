<template>
    <div>
      <div>
        <button class="buttonPassive" @click="startLeft">left</button>
        <button class="buttonPassive" @click="left">open</button>
      </div>
      <div>
        <button class="buttonAlert" @click="stop">stop</button>
      </div>
      <div>
        <button class="buttonPassive" @click="startRight">right</button>
        <button class="buttonPassive" @click="right">close</button>
      </div>
      <div>
        <button class="buttonPassive" @click="lightOn">light sensor on</button>
        <button class="buttonPassive" @click="lightOff">light sensor off</button>
      </div>
      <CurtainTimes :baseUrl="baseUrl" />
    </div>
</template>

<script>
import CurtainTimes from './CurtainTimes.vue';

export default {
  name: 'DataStream',
  components: {
    CurtainTimes,
  },
  data() {
    return {
      baseUrl: 'http://192.168.2.152:8080/',
    };
  },
  methods: {
    startLeft() {
      fetch(`${this.baseUrl}startopen`);
    },
    startRight() {
      fetch(`${this.baseUrl}startclose`);
    },
    left() {
      fetch(`${this.baseUrl}open`);
    },
    right() {
      fetch(`${this.baseUrl}close`);
    },
    stop() {
      fetch(`${this.baseUrl}stop`);
    },
    lightOn() {
      fetch(`${this.baseUrl}lighton`);
    },
    lightOff() {
      fetch(`${this.baseUrl}lightoff`);
    },
  },
};
</script>

<style scoped>

.buttonPassive {
  box-shadow: 0px 0px 0px 2px #9fb4f2;
  background:linear-gradient(to bottom, #7892c2 5%, #476e9e 100%);
  background-color:#7892c2;
  border-radius:10px;
  border:1px solid #4e6096;
  display:inline-block;
  cursor:pointer;
  color:#ffffff;
  font-family:Arial;
  font-size:19px;
  padding:32px 76px;
  text-decoration:none;
  text-shadow:0px 1px 0px #283966;
}
.buttonPassive:hover {
  background:linear-gradient(to bottom, #476e9e 5%, #7892c2 100%);
  background-color:#476e9e;
}
.buttonPassive:active {
  position:relative;
  top:1px;
}

.buttonAlert {
  box-shadow:inset 0px 39px 0px -24px #e67a73;
  background-color:#e4685d;
  border-radius:4px;
  border:1px solid #ffffff;
  display:inline-block;
  cursor:pointer;
  color:#ffffff;
  font-family:Arial;
  font-size:15px;
  padding:32px 76px;
  text-decoration:none;
  text-shadow:0px 1px 0px #b23e35;
}
.buttonAlert:hover {
  background-color:#eb675e;
}
.buttonAlert:active {
  position:relative;
  top:1px;
}
</style>
