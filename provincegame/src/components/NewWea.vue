<template>
  <div class="scroll">
    <div>实时天气</div>
    <vue3-seamless-scroll :list="weatherdata" :step="0.5" :hover="true">
      <div class="item" v-for="(item, index) in weatherdata" :key="index">
        <span :data-obj="JSON.stringify(item)" @click="handleButton">{{
          item.city
        }}</span>
        <span>{{ item.weather }}</span>
        <span>{{ item.winddirection }}风{{ item.windpower }}级</span>
        <span>{{ item.reporttime }}</span>
      </div>
    </vue3-seamless-scroll>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { Vue3SeamlessScroll } from "vue3-seamless-scroll";
import axis from "axios";
export default defineComponent({
  data() {
    return {
      reporttime: "",
      weatherdata: [],
      // cityname: [
      //   110000, 120000, 340000, 140000, 130000, 210000, 220000,440000,330000,310000,
      //   430000, 420000,
      // ],
      // 110000, 120000, 340000, 140000, 130000, 210000, 220000,440000,330000,310000,
      //   430000, 420000,
    };
  },
  components: {
    Vue3SeamlessScroll,
  },
  methods: {
    getweatherdata() {
      var that = this;
      // var url =
      //   "https://restapi.amap.com/v3/weather/weatherInfo?city=" +
      //   this.cityname[i] +
      //   "&key=84fa7f220c9194d3af6a6485f17a6636";
      var url =
        "https://restapi.amap.com/v3/weather/weatherInfo?city=430000&key=84fa7f220c9194d3af6a6485f17a6636&extensions=all";
      axis.get(url).then((res) => {
        that.reporttime = res.data.forecasts[0].reporttime;
        console.log(res.data.forecasts[0]);
        for (let i = 0; i < 5; i++) {
          that.weatherdata.push({
            city: res.data.forecasts[0].city,
            weather: res.data.forecasts[0].casts[i].dayweather,
            winddirection: res.data.forecasts[0].casts[i].daywind,
            windpower: res.data.forecasts[0].casts[i].nightpower,
            reporttime: res.data.forecasts[0].casts[i].date,
          });
          that.weatherdata.push({
            city: res.data.forecasts[0].city,
            weather: res.data.forecasts[0].casts[i].dayweather,
            winddirection: res.data.forecasts[0].casts[i].daywind,
            windpower: res.data.forecasts[0].casts[i].nightpower,
            reporttime: res.data.forecasts[0].casts[i].date,
          });
        }
      });
    },
    handleButton(e) {
      let InfoAnync = JSON.parse(e.target.dataset.obj);
      console.log(InfoAnync);
      // location.href = "/NewsView"; //测试效果
    },
  },
  mounted() {
    this.getweatherdata();
    // this.getnewstitle();
    // setInterval(() => {
    //   this.list.push({
    //     title: "我是新增的一条数据",
    //     date: Date.now(),
    //   });
    // }, 10000);
  },
});
</script>



<style scoped>
.scroll {
  /* background: #fff; */
  display: inline-block;
  height: 100%;
  width: 100%;
  /* margin-top:5%;
  margin-left: 1%; */
  overflow: hidden;
  position: relative;
}

.scroll > div:first-child {
  font-weight: bold;
  color: darkcyan;
  text-align: center;
}

.scroll > div:last-child {
  margin-top: 15px;
  height: 260px;
  overflow: hidden;
}

.scroll .item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 3px 0;
  cursor: pointer;
}
.scroll .item span {
  color: orange;
  /* font-size: 17px; */
}
</style>