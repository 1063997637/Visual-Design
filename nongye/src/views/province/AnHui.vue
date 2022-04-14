<template>
  <div class="whole-body">
    <div class="bnt-view">
      <div class="topbnt_left fl">
        <!-- <li><router-link to="/nongguide"> 展览馆 </router-link></li> -->
      </div>
      <li>
        <router-link to="/"> <h1 class="tith1 fl">安徽省</h1> </router-link>
      </li>

      <div class="fr topbnt_right">
        <ul></ul>
      </div>
    </div>
    <div class="content">
      <div class="content-con">
        <div class="left-body">
          <div class="left-top" v-if="true">
            <total-production
              :xvalue="this.province"
              :yvalue="this.tempvalue"
            />
            <span class="border_bg_leftTop"></span>
            <span class="border_bg_rightTop"></span>
            <span class="border_bg_leftBottom"></span>
            <span class="border_bg_rightBottom"></span>
          </div>
          <div class="left-con">
            <sow-size-change />
          </div>
          <div class="left-bottom">
            <mu-ye />
            <span class="border_bg_leftTop"></span>
            <span class="border_bg_rightTop"></span>
            <span class="border_bg_leftBottom"></span>
            <span class="border_bg_rightBottom"></span>
          </div>
        </div>

        <div class="center-body">
          <div class="center-top">
            <sow-size />
            <span class="border_bg_leftTop"></span>
            <span class="border_bg_rightTop"></span>
            <span class="border_bg_leftBottom"></span>
            <span class="border_bg_rightBottom"></span>
          </div>
          <div class="center-bottom">
            <lin-ye />
            <span class="border_bg_leftTop"></span>
            <span class="border_bg_rightTop"></span>
            <span class="border_bg_leftBottom"></span>
            <span class="border_bg_rightBottom"></span>
          </div>
        </div>

        <div class="right-body">
          <div class="right-top" v-if="true">
            <div class="map" id="midmap" v-if="true"></div>
          </div>

          <div class="right-con" v-if="true">
            <yu-ye />
            <span class="border_bg_leftTop"></span>
            <span class="border_bg_rightTop"></span>
            <span class="border_bg_leftBottom"></span>
            <span class="border_bg_rightBottom"></span>
          </div>
          <div class="right-bottom">
            <shui-guo />
            <span class="border_bg_leftTop"></span>
            <span class="border_bg_rightTop"></span>
            <span class="border_bg_leftBottom"></span>
            <span class="border_bg_rightBottom"></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import * as AnHuiMap from "./安徽省.json";
import axis from "axios";
import TotalProduction from "../component/TotalProduction.vue";
import SowSize from "../component/SowSize.vue";
import SowSizeChange from "../component/SowSizeChange.vue";
import LinYe from "../component/LinYe.vue";
import MuYe from "../component/MuYe.vue";
import YuYe from "../component/YuYe.vue";
import ShuiGuo from "../component/ShuiGuo.vue";

export default {
  components: {
    TotalProduction,
    SowSize,
    SowSizeChange,
    LinYe,
    MuYe,
    YuYe,
    ShuiGuo,
  },
  data() {
    return {
      //省份名称
      province: [],
      //临时value
      tempvalue: [],
      //各粮食产量
      foodname: [],
      provalue: [],
      //种植面积
      sowsize: [],
      //播种面积变化
      sowsizechange: [],
      //林业产量
      linproduction: [],
      //牧业产量
      muproduction: [],
      //渔业产量
      yuproduction: [],
      //水果产量
      shuiguo: [],
      onlinedata: [],
      staticdata: [
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
      ],
    };
  },
  methods: {
    getlsdatas() {
      var that = this;
      axis.get("http://127.0.0.1:8000/shuiziyuan/").then((res) => {
        console.log("连接成功");
        for (let i = 0; i < res.data.length; i++) {
          that.foodname.push(res.data[i].fields.省份);
          that.provalue.push(res.data[i].fields.水资源总量_亿立方米_field);
        }
      });
    },
    getdatas() {
      var that = this;
      axis.get("http://127.0.0.1:8000/shuiziyuan/").then((res) => {
        console.log("连接成功");
        for (let i = 0; i < res.data.length; i++) {
          // var it1 = res.data[i].fields.省份;
          // var it2 = res.data[i].fields.水资源总量_亿立方米_field;
          // var item = { name: it1, value: it2 };
          // that.onlinedata.push(item);
          that.province.push(res.data[i].fields.省份);
          that.tempvalue.push(res.data[i].fields.水资源总量_亿立方米_field);
        }
      });
    },
    initCharts_mid() {
      var myChart = echarts.init(document.getElementById("midmap"));
      myChart.showLoading();
      // 注册地图
      echarts.registerMap("anhui", AnHuiMap);
      //配置数据
      var option = {
        title: {
          left:"70%",
          top:"20%",
          text: "安徽",
          textStyle: {
            color: "#5881c4",
          fontSize:"40",
          },
        },
        tooltip: {
          trigger: "item",
        },
        // zoom:3.0,
        series: [
          {
            // data: this.onlinedata,
            type: "map",
            map: "anhui",
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
        // visualMap: {
        //   type: "continuous",
        //   label: {
        //     show: true,
        //   },
        //   min: 10,
        //   max: 4000,
        //   text: ["High", "Low"],
        //   bottom: 100,
        //   left: 10,
        //   realtime: false,
        //   calculable: true,
        //   inRange: {
        //     color: ["lightskyblue", "yellow", "orangered"],
        //   },
        // },
      };
      setTimeout(() => {
        myChart.setOption(option, true);
        myChart.hideLoading();
      }, 1000);
    },
  },
  mounted() {
    this.getlsdatas();
    this.initCharts_mid();
  },
};
</script>

<style scoped>
.whole-body {
  background: url("../../img/bg2.jpg");
  background-size: 100% 100%;
  width: 100%;
  height: 100%;
  position: fixed;
}
.bnt-view {
  height: 5%;
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
  /* margin-left: 100%; */
  margin-bottom: 10%;
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
  margin-bottom: 50%;
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
  height: 88%;
  margin: 1.5%;
  /* border: 1px solid red; */
  position: relative;
}
.content .content-con {
  position: relative;
  height: 100%;
}
.content .content-con .left-body {
  margin: 0.5%;
  position: relative;
  width: 30%;
  height: 100%;
  float: left;
  /* margin: 0 0.3%; */
  /* border: 1px solid red; */
}
.left-body .left-top {
  margin-top: 5%;
  /* margin: 0.5%; */
  position: relative;
  width: 100%;
  height: 30%;
  border: 1px solid #05d1fc;
}
.left-body .left-con {
  /* margin: 0.5%; */
  margin-top: 5%;
  position: relative;
  width: 100%;
  height: 30%;
  /* margin-top: 1.6%; */
  border: 1px solid #05d1fc;
}
.left-body .left-bottom {
  /* margin: 0.5%; */
  margin-top: 5%;
  position: relative;
  width: 100%;
  height: 30%;
  border: 1px solid #05d1fc;
  /* margin-top: 1.6%; */
}
.center-body {
  margin: 0.5%;
  position: relative;
  width: 35%;
  height: 100%;
  /* margin: 0 0.3%; */
  float: left;
  /* border: 1px solid red; */
}
.center-body .center-top {
  margin-top: 5%;
  position: relative;
  width: 100%;
  height: 46%;
  /* margin: 0 0.3%; */
  float: left;
  border: 1px solid #05d1fc;
}
.center-body .center-bottom {
  margin-top: 5%;
  position: relative;
  width: 100%;
  height: 46%;
  /* margin: 0 0.3%; */
  float: left;
  border: 1px solid #05d1fc;
}
.right-body {
  margin: 0.5%;
  position: relative;
  width: 32%;
  height: 100%;
  float: left;
  /* margin: 0 0.3%; */
  /* border: 1px solid red; */
}
.right-body .right-top {
  margin-top: 5%;
  position: relative;
  width: 100%;
  height: 15%;
  /* border: 1px solid #05d1fc; */
}
.right-body .right-con {
  margin-top: 5%;
  position: relative;
  width: 100%;
  height: 30%;
  border: 1px solid #05d1fc;
  /* margin-top: 2%; */
}
.right-body .right-bottom {
  margin-top: 5%;
  position: relative;
  width: 100%;
  height: 44%;
  border: 1px solid #05d1fc;
}

/* 边框样式 */
.border_bg_leftTop {
  position: absolute;
  /* left:-5rem; */
  top: -0.99rem;
  width: 5rem;
  height: 1rem;
  display: block;
  background: url(../../img/title_left_bg.png);
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
  background: url(../../img/border_bg.jpg) no-repeat;
  background-size: 100% 100%;
}
.border_bg_leftBottom {
  position: absolute;
  left: -0.06rem;
  bottom: -0.04rem;
  width: 1.5rem;
  height: 1.5rem;
  display: block;
  background: url(../../img/border_bg.jpg) no-repeat;
  background-size: 100% 100%;
}
.border_bg_rightBottom {
  position: absolute;
  right: -0.2rem;
  bottom: -0.2rem;
  width: 1.5rem;
  height: 1.5rem;
  display: block;
  background: url(../../img/title_right_bg.png) no-repeat;
  background-size: 100% 100%;
}
</style>