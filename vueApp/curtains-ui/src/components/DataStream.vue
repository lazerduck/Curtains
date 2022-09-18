<template>
    <div>
      <p>is left: {{isLeft}} | is moving: {{isMoving}}</p>
      <p>is light: {{isLight}} | is Night: {{isNight}}
        | light Count: {{lightCount}} | light On: {{lightOn}}</p>
    </div>
</template>

<script>
export default {
  name: 'DataStream',
  data() {
    return {
      isLight: false,
      isLeft: false,
      isMoving: false,
      isNight: false,
      lightCount: 0,
      lightOn: true,
      openTime: 0,
      closeTime: 0,
      morning: '',
      evening: '',
      baseUrl: 'http://192.168.2.152:8080/',
    };
  },
  created() {
    this.timer = setInterval(this.updateCurtainData, 1000);
    this.updateCurtainData();
  },
  methods: {
    updateCurtainData() {
      const that = this;
      fetch(`${this.baseUrl}state`)
        .then((resp) => resp.json())
        .then((data) => {
          that.isLight = data.isLight;
          that.isLeft = data.isLeft;
          that.isMoving = data.isMoving;
          that.isNight = data.isNight;
          that.lightCount = data.lightCount;
          that.lightOn = data.lightOn;
          that.openTime = data.openTime;
          that.closeTime = data.closeTime;
          that.morning = data.morning;
          that.evening = data.evening;

          that.$emit('update', {
            openTime: that.openTime,
            closeTime: that.closeTime,
            morning: that.morning,
            evening: that.evening,
          });
        });
    },
  },
};
</script>
