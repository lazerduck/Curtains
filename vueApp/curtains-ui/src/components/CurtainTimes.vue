<template>
  <div>
    <hr />
    <div>
      <label>Open time: {{openTime}} |</label>
      <label>New Time:</label>
      <input :value="openTime" type="number" min="0" ref="newOpen"/>
    </div>
      <div>
      <label>Close time: {{closeTime}} |</label>
      <label>New Time:</label>
      <input :value="closeTime" type="number" min="0" ref="newClose" />
    </div>
    <div>
      <button @click="setTravelTime">Submit</button>
    </div>
    <hr />
    <div>
      <label>Morning: {{morning}} |</label>
      <label>New Time:</label>
      <input :value="morning" type="time" ref="newMorning"/>
    </div>
      <div>
      <label>Evening: {{evening}} |</label>
      <label>New Time:</label>
      <input :value="evening" type="time" ref="newEvening" />
    </div>
    <div>
      <button @click="setLightTime">Submit</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CurtainTimes',
  data() {
    return {
      openTime: 0,
      closeTime: 0,
      morning: new Date(),
      evening: new Date(),
    };
  },
  created() {
    this.getLightTime();
    this.getTravelTime();
  },
  props: {
    baseUrl: null,
  },
  methods: {
    getTravelTime() {
      const that = this;
      fetch(`${this.baseUrl}travelTimes`)
        .then((resp) => resp.json())
        .then((data) => {
          that.openTime = data.open;
          that.closeTime = data.close;
        });
    },
    getLightTime() {
      const that = this;
      fetch(`${this.baseUrl}lighttimes`)
        .then((resp) => resp.json())
        .then((data) => {
          that.morning = data.morning;
          that.evening = data.evening;
        });
    },
    setTravelTime() {
      const open = this.$refs.newOpen.value;
      const close = this.$refs.newClose.value;
      fetch(`${this.baseUrl}setmovetimes`,
        {
          method: 'POST',
          body: JSON.stringify({
            openTime: open,
            closeTime: close,
          }),
        });
      this.getTravelTime();
    },
    setLightTime() {
      const morning = this.$refs.newMorning.value;
      const evening = this.$refs.newEvening.value;
      fetch(`${this.baseUrl}setlighttimes`,
        {
          method: 'POST',
          body: JSON.stringify({
            morning,
            evening,
          }),
        });
      this.getLightTime();
    },
  },
};
</script>
