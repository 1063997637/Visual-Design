<template>
  <div class="scroll">
    <div>实时天气</div>
    <vue3-seamless-scroll :list="weatherdata" :step="0.5" :hover="true">
      <div class="item" v-for="(item, index) in weatherdata" :key="index">
        <span :data-obj="JSON.stringify(item)" @click="handleButton">{{
          item.city
        }}</span>
        <span>{{ item.weather }}</span>
        <span>{{ item.temperature }}°C</span>
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
      weatherdata: [],
      // cityname: [
      //   110000, 120000, 340000, 140000, 130000, 210000, 220000,440000,330000,310000,
      //   430000, 420000,
      // ],
      cityname: [
        "张家界市",
        "常德市",
        "益阳市",
        "岳阳市",
        "怀化市",
        "娄底市",
        "长沙市",
        "湘潭市",
        "株洲市",
        "邵阳市",
        "衡阳市",
        "永州市",
        "郴州市",
        "湘西土家族苗族自治州",
      ],
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
      for (let i = 0; i < this.cityname.length; i++) {
        var url =
          "https://restapi.amap.com/v3/weather/weatherInfo?city=" +
          this.cityname[i] +
          "&key=84fa7f220c9194d3af6a6485f17a6636";
        axis.get(url).then((res) => {
          that.weatherdata.push({
            city: res.data.lives[0].city,
            weather: res.data.lives[0].weather,
            temperature: res.data.lives[0].temperature,
            winddirection: res.data.lives[0].winddirection,
            windpower: res.data.lives[0].windpower,
            reporttime: res.data.lives[0].reporttime,
          });
        });
      }
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