<template>
  <div>
    <hr />
    <div>
      <label>Open time: {{automationDetails.openTime}} |</label>
      <label>New Time:</label>
      <input v-model="openTime" type="number" min="0"/>
    </div>
      <div>
      <label>Close time: {{automationDetails.closeTime}} |</label>
      <label>New Time:</label>
      <input v-model="closeTime" type="number" min="0"/>
    </div>
    <div>
      <button @click="setTravelTime">Submit</button>
    </div>
    <hr />
    <div>
      <label>Morning: {{automationDetails.morning}} |</label>
      <label>New Time:</label>
      <input v-model="morning" type="time"/>
    </div>
      <div>
      <label>Evening: {{automationDetails.evening}} |</label>
      <label>New Time:</label>
      <input v-model="evening" type="time"/>
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
      morning: null,
      evening: null,
    };
  },
  props: {
    baseUrl: null,
    automationDetails: {},
  },
  methods: {
    setTravelTime() {
      const that = this;
      fetch(`${this.baseUrl}setmovetimes`,
        {
          method: 'POST',
          body: JSON.stringify({
            openTime: that.openTime,
            closeTime: that.closeTime,
          }),
        });
    },
    setLightTime() {
      const that = this;
      fetch(`${this.baseUrl}setlighttimes`,
        {
          method: 'POST',
          body: JSON.stringify({
            morning: that.morning,
            evening: that.evening,
          }),
        });
    },
  },
};
</script>
