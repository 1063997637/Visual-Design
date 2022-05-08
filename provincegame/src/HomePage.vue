<template>
  <div class="content-body">
    <div class="title">
      <div class="left"><router-link to="/">首页</router-link></div>
      <div class="right"><router-link to="/pricepage">数据详情</router-link></div>
    </div>
    <div class="leftmap">
      <div id="Home" style="width: 100%; height: 100%" v-if="true"></div>
      <span class="border_bg_leftTop"></span>
      <span class="border_bg_rightBottom"></span>
    </div>
    <div class="right-top">
      <weather-show />
      <!-- <time-view /> -->
      <span class="border_bg_leftTop"></span>
      <span class="border_bg_rightBottom"></span>
    </div>
    <div class="righttest">
      <news-show @click="show" /><news-view
        :showModel="this.showModel"
        :newstitle="newsti"
        :newsbody="newsbo"
        @click="showModel = false"
      />
      <span class="border_bg_leftTop"></span>
      <span class="border_bg_rightBottom"></span>
    </div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import * as HuNanMap from "./湖南省.json";
import NewsShow from "./components/NewsShow.vue";
import NewsView from "./components/NewsView.vue"; //弹窗
// import TimeView from "./component/TimeView.vue";
import WeatherShow from "./components/WeatherShow.vue";
export default {
  components: { NewsShow, NewsView, WeatherShow },
  data() {
    return {
      newsti: "通道:旅游推动乡村振兴 皇都侗寨动力十足",
      newsbo:
        "  五一前夕，万佛山侗寨风景名胜区管理处工作人员杨秀仟——网络达人潇洒仟哥来到皇都侗文化村，实地品尝特色美食、体验农耕文化等，用镜头推介皇都村美丽的乡村风貌，感受乡村振兴发展成果。皇都村依山傍水，一栋栋民居错落有致，横跨江面两岸的普修桥与袅袅炊烟的侗寨、风光秀丽、和美富足……在乡村振兴中，皇都村村居面貌焕然一新，乡村秩序、环境面貌大幅改善，基础设施建设和公共服务配套得到有效提升，同时还培育了中药材、果蔬、茶叶、稻田养鱼等优势特色农业，不断助推乡村振兴发展，产业兴旺、生态宜居、乡风文明、治理有效、生活富裕的乡村已初步形成，人民群众获得感显著提升。近年来，我县加快“文旅 ”融合发展，激发市场活力，积极探索走出一条乡村振兴的特色文旅线路。在“旅游+产业”上，依托传统村落、民俗风情文化、重点培育中药材、果蔬、茶叶、羊肚菌、稻田养鱼等优势特色农业，建成以观光采摘、农事体验、生态休闲、民俗文化体验为主的风情体验旅游业态，村级产业已经实现产业分红。",
      staticdata: [
        { name: "湘西土家族苗族自治州", value: 10000 },
        { name: "张家界市", value: 13000 },
        { name: "常德市", value: 11000 },
        { name: "益阳市", value: 12000 },
        { name: "岳阳市", value: 13000 },
        { name: "怀化市", value: 14000 },
        { name: "娄底市", value: 15000 },
        { name: "长沙市", value: 16000 },
        { name: "湘潭市", value: 17000 },
        { name: "株洲市", value: 18000 },
        { name: "邵阳市", value: 19000 },
        { name: "衡阳市", value: 20000 },
        { name: "永州市", value: 21000 },
        { name: "郴州市", value: 23000 },
      ],
      showModel: false,
    };
  },
  methods: {
    show() {
      this.showModel = true;
      console.log(this.showModel);
    },
    initCharts(Dom) {
      var myChart = echarts.init(Dom);
      console.log("开始加载");
      // myChart.showLoading();
      // 注册地图
      echarts.registerMap("hunan", HuNanMap);
      //配置数据
      var option = {
        title: {
          left: "center",
          text: "湖南省",
          textStyle: {
            color: "#5881c4",
          },
        },
        tooltip: {
          trigger: "item",
        },
        series: [
          {
            name: "粮食总产量(万吨)",
            data: this.staticdata,
            type: "map",
            map: "hunan",
            itemStyle: {
              //区域样式
              borderColor: "yellow",
              areaColor: "#5881c4",
            },
            emphasis: {
              itemStyle: {
                //高亮区域样式
                borderColor: "blue",
                areaColor: "green",
              },
            },
          },
        ],
        visualMap: {
          textStyle: {
            color: "#5881c4",
          },
          label: {
            show: true,
          },
          min: 10000,
          max: 50000,
          text: ["High", "Low"],
          bottom: 100,
          left: 10,
          realtime: false,
          calculable: true,
          inRange: {
            color: ["orangered", "yellow", "lightskyblue"],
          },
        },
      };
      myChart.setOption(option, true);
      // myChart.hideLoading();
      // myChart.on("click", function (params) {
      // });
    },
  },
  mounted() {
    this.initCharts(document.getElementById("Home"));
  },
};
</script>

<style scoped>
.content-body {
  background: url("./img/newbg.jpg");
  /* background:white; */
  width: 100%;
  height: 100%;
  /* background-size: 100% 100%; */
  position: absolute;
  /* border: 1px solid red; */
}
.content-body .title {
  /* color: #ffffff; */
  /* margin: 0; */
  height: 5%;
  width: 100%;
  /* text-align: center; */
  /* border: 1px solid red; */

  /* position: relative; */
}
.title .left {
  width: 49%;
  height: 100%;
  float: left;
  text-align: center;
  
  /* border: 1px solid red; */
}
.title .right {
  width: 50%;
  height: 100%;
  float: left;
  /* border: 1px solid green; */

  position: relative;
}
.content-body .leftmap {
  top: 3.5%;
  left: 1.5%;
  width: 50%;
  height: 90%;
  float: left;
  position: relative;
  border: 1px solid #05d1fc;

  /* border: 1px solid red; */
}
.content-body .righttest {
  position: relative;
  top: 13%;
  left: 2%;
  width: 46.5%;
  height: 50%;
  float: left;
  border: 1px solid #05d1fc;
}
.border_bg_leftTop {
  position: absolute;
  /* left:-5rem; */
  top: -1.1rem;
  width: 5rem;
  height: 1rem;
  display: block;
  background: url("./img/title_left_bg.png");
  /* background-size: cover; */
  background-size: 100% 100%;
}
.border_bg_rightTop {
  position: absolute;
  right: -0.1rem;
  top: -0.1rem;
  width: 1.5rem;
  height: 1.5rem;
  display: block;
  background: url(./img/border_bg.jpg) no-repeat;
  background-size: 100% 100%;
}
.border_bg_leftBottom {
  position: absolute;
  left: -0.1rem;
  bottom: -0.1rem;
  width: 1.5rem;
  height: 1.5rem;
  display: block;
  background: url(./img/border_bg.jpg) no-repeat;
  background-size: 100% 100%;
}
.border_bg_rightBottom {
  position: absolute;
  right: -0.2rem;
  bottom: -0.2rem;
  width: 1.5rem;
  height: 1.5rem;
  display: block;
  background: url(./img/title_right_bg.png) no-repeat;
  background-size: 100% 100%;
}
.content-body .right-top {
  margin: 0;
  position: relative;
  top: 8%;
  left: 2%;
  width: 46.5%;
  height: 30%;
  float: left;
  border: 1px solid #05d1fc;
}
.fl {
  float: left;
}
.tith1 {
  width: 33%;
  text-align: center;
  padding: 0;
  margin: 0;
  font-weight: bold;
  letter-spacing: 8px;
  font-size: 36px;
  color: #fff;
}
</style>