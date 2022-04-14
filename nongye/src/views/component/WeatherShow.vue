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
      localnews: [
        { id: 1, title: "2022年大学生志愿服务西部计划启动" },
        { id: 2, title: "农业经营主体信贷直通车授信金额已达205.77亿元" },
        {
          id: 3,
          title: "三部门:2025年,在具备条件的地区基本实现村村通快递",
        },
        {
          id: 4,
          title: "第八届中国国际“互联网+”大学生创新创业大赛启动",
        },
        {
          id: 5,
          title: "“中国减贫事业取得非凡成就”",
        },
        {
          id: 6,
          title: "城乡残疾人就业规模达881.6万人",
        },
        {
          id: 7,
          title: "全国农业社会化服务典型开始征集",
        },
        {
          id: 8,
          title:
            "习近平:解放思想开拓创新团结奋斗攻坚克难 加快建设具有世界影响力的中...",
        },
        {
          id: 9,
          title: "李克强主持召开国务院常务会议",
        },
        {
          id: 10,
          title: " 国家级制种基地增加到216个“十四五”末供种保障能力将提高到80%",
        },
        {
          id: 11,
          title: " 农业农村部印发《国家级农作物种质资源库(圃)管理规范》",
        },
        {
          id: 12,
          title:
            " 重拳整治违法活动 切实维护渔业秩序    ——农业农村部有关部门负责人...",
        },
        {
          id: 13,
          title: "重拳整治违法活动 切实维护渔业秩序",
        },
        {
          id: 14,
          title:
            "农业农村部召开部领导专题会强调积极应对疫情影响 维护农业生产流通秩...",
        },
        {
          id: 15,
          title: "商务部多措并举促进货运物流畅通保障市场供应",
        },
      ],
      weatherdata: [],
      cityname: [
        110000, 120000, 340000, 140000, 130000, 210000, 220000,440000,330000,310000,
        430000, 420000,
      ],
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
        // console.log("test");
        // console.log(url);
        axis.get(url).then((res) => {
          //   console.log(res.data.lives[0]);
          //   console.log(res.data.lives[0].city);
          //   console.log(res.data.lives[0].weather);
          //   console.log(res.data.lives[0].reporttime);
          //   console.log(res.data.lives[0].winddirection);
          //   console.log(res.data.lives[0].windpower);
          that.weatherdata.push({
            city: res.data.lives[0].city,
            weather: res.data.lives[0].weather,
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