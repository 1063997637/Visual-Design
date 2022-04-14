<template>
  <div class="whole-body">
    <div class="bnt-view">
      <div class="topbnt_left fl">
        <ul>
          <li><router-link to="/"> 主页 </router-link></li>
          <li><router-link to="/nongguide"> 展览馆 </router-link></li>
        </ul>
      </div>
      <h1 class="tith1 fl">农业基地</h1>
      <div class="fr topbnt_right">
        <ul>
          <li><router-link to="/nongmonitor"> 监测馆 </router-link></li>
          <li class="active">
            <router-link to="/nongview"> 数据馆 </router-link>
          </li>
        </ul>
      </div>
    </div>
    <div class="content">
      <div class="content-con">
        <div class="left-body">
          <div class="left-top" v-if="true">
            <total-production />
          </div>
          <div class="left-con">
            <sow-size />
          </div>
        </div>

        <div class="center-body">
          <div class="map" id="midmap" v-if="true"></div>
        </div>

        <div class="right-body">
          <div class="right-top" v-if="true">
            <area-production />
          </div>

          <div class="right-con" v-if="true">
            <area-leida/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import * as chinaMap from ".././china.json";
import TotalProduction from "./nongcomponent/TotalProduction.vue";
import SowSize from "./nongcomponent/SowSize.vue";
import AreaProduction from './nongcomponent/AreaProduction.vue';
import AreaLeida from './nongcomponent/AreaLeida.vue';

export default {
  components: { TotalProduction,SowSize,AreaProduction, AreaLeida},
  data() {
    return {};
  },
  methods: {
    initCharts_mid() {
      var myChart = echarts.init(document.getElementById("midmap"));
      // 注册地图
      echarts.registerMap("china", chinaMap);
      //配置数据
      var option = {
        title: {
          text: "粮食产量全国地图",
          textStyle: {
            color: "#5881c4",
          },
        },
        tooltip: {
          trigger: "item",
        },
        series: [
          {
            data: [
              { name: "湖南省", value: 1000 },
              { name: "湖北省", value: 1100 },
              { name: "北京市", value: 1200 },
              { name: "天津市", value: 1300 },
              { name: "山西省", value: 1400 },
              { name: "内蒙古自治区", value: 1500 },
              { name: "辽宁省", value: 1600 },
              { name: "吉林省", value: 1700 },
              { name: "黑龙江省", value: 1800 },
              { name: "上海市", value: 1900 },
              { name: "江苏省", value: 2000 },
              { name: "浙江省", value: 2100 },
              { name: "安徽省", value: 2300 },
              { name: "福建省", value: 2500 },
              { name: "江西省", value: 2600 },
              { name: "山东省", value: 2800 },
              { name: "河南省", value: 2690 },
              { name: "广东省", value: 2900 },
              { name: "广西壮族自治区", value: 2952 },
              { name: "海南省", value: 2999 },
              { name: "贵州省", value: 3050 },
              { name: "四川省", value: 3060 },
              { name: "重庆市", value: 3200 },
              { name: "西藏自治区", value: 3300 },
              { name: "陕西省", value: 3500 },
              { name: "甘肃省", value: 3600 },
              { name: "青海省", value: 3700 },
              { name: "宁夏回族自治区", value: 3800 },
              { name: "新疆维吾尔自治区", value: 3900 },
              { name: "云南省", value: 3500 },
            ],
            type: "map",
            map: "china",
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
          type: "continuous",
          label: {
            show: true,
          },
          min: 10,
          max: 4000,
          text: ["High", "Low"],
          bottom: 100,
          left: 10,
          realtime: false,
          calculable: true,
          inRange: {
            color: ["lightskyblue", "yellow", "orangered"],
          },
        },
      };
      myChart.setOption(option, true);
    },
  },
  mounted() {
    this.initCharts_mid();
  },
};
</script>

<style scoped>
.whole-body {
  background: url("../../img/bg.jpg");
  background-size: 100% 100%;
  width: 100%;
  height: 100%;
  position: fixed;
}
.bnt-view {
  height: 10%;
  width: 100%;
  /* display: inline-block; */
  /* border: 1px solid red; */
}
.fl {
  float: left;
}
.fr {
  float: right;
}
.topbnt_left {
  width: 33%;
  height: 100%;
}
.topbnt_left ul {
  padding-top: 15px;
  padding-left: 10%;
  width: 100%;
}
.topbnt_left li {
  background: url("../../img/bnt.png") center;
  font-size: 14px;
  line-height: 33px;
  background-repeat: no-repeat;
  width: 18%;
  height: 35px;
  float: left;
  text-align: center;
  margin-left: 15%;
}
.topbnt_left li a {
  text-decoration: none;
  color: #fff;
}
.topbnt_left li.active,
.topbnt_right li.active {
  background: url("../../img/bntactive.png") no-repeat center;
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
.topbnt_right {
  width: 33%;
  height: 100%;
}
.topbnt_right ul {
  padding-top: 15px;
  padding-left: 10%;
  width: 100%;
}
.topbnt_right li {
  background: url("../../img/bnt.png") center;
  font-size: 14px;
  line-height: 33px;
  background-repeat: no-repeat;
  width: 18%;
  height: 35px;
  float: right;
  text-align: center;
  margin-right: 25%;
}
.topbnt_right li a {
  text-decoration: none;
  color: #fff;
}
.map {
  width: 100%;
  height: 100%;
}
.content {
  /* border: 1px solid red; */
  width: 97%;
  /* height: calc(100% - 75px); */
  height: 83%;
  margin: 1.5%;
  /* border: 1px solid red; */
  position: relative;
}
.content .content-con {
  height: 100%;
}
.content .content-con .left-body {
  width: 30%;
  height: 100%;
  float: left;
  /* margin: 0 0.3%; */
  /* border: 1px solid red; */
}
.left-body .left-top {
  width: 100%;
  height: 50%;
  /* border: 1px solid red; */
}
.left-body .left-top .top-body {
  width: 100%;
  height: calc(100% - 30px);
}
.left-body .left-top .top-body .top-left {
  float: left;
  width: 50%;
  height: 100%;
}
/* .public-bg {
  background: rgba(12, 26, 63, 0.3);
} */
.public-title {
  width: calc(100% - 20px);
  height: 30px;
  position: abs;
  top: 0;
  left: 5px;
  color: white;
  padding-left: 16px;
  line-height: 30px;
  font-size: 13px;
}
.left-body .left-con {
  width: 100%;
  height: 50%;
  /* margin-top: 1.6%; */
  /* border: 1px solid red; */
}
.left-body .left-bottom {
  width: 100%;
  height: 32%;
  /* margin-top: 1.6%; */
}
.center-body {
  width: 39%;
  height: 100%;
  /* margin: 0 0.3%; */
  float: left;
  /* border: 1px solid red; */
}
.right-body {
  width: 30%;
  height: 100%;
  float: left;
  /* margin: 0 0.3%; */
  /* border: 1px solid red; */
}
.right-body .right-top {
  width: 100%;
  height: 50%;
}
.right-body .right-con {
  width: 100%;
  height: 50%;
  /* margin-top: 2%; */
}
.right-body .right-bottom {
  width: 100%;
  height: 39%;
  /* margin-top: 2%; */
}
</style>