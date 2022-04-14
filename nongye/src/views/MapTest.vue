<template>
  <div
    class="content-body"
    v-bind:style="{
      backgroundImage: 'url(' + bg + ')',
      backgroundRepeat: 'no-repeat',
      backgroundSize: '100% 100%',
    }"
  >
    <!-- <div class="header">
      <div class="header-left">
        <span>水资源分布情况</span>
      </div>
      <div class="header-time">
        <span id="time"></span>
      </div>
    </div> -->

    <div class="content">
      <div class="content-con">
        <div class="left-body">
          <div class="left-top public-bg">
            <!-- <div class="public-title">地表水和地下水资源</div> -->
            <!-- 加上v-if,使得每次加载都重新渲染 -->
            <div class="map" id="avragewater"></div>
          </div>
          <div class="left-con public-bg">
            <!-- <div class="public-title">各省人均水资源量</div> -->
            <!-- 加上v-if,使得每次加载都重新渲染 -->
            <div class="map" id="landwater" v-if="true"></div>
          </div>
        </div>

        <div class="center-body">
          <!-- 加上v-if,使得每次加载都重新渲染 -->
          <div class="map" id="midmap" v-if="true"></div>
        </div>

        <div class="right-body">
          <div class="right-top public-bg">
            <!-- <div class="public-title">水质污染TOP5</div> -->
            <!-- 加上v-if,使得每次加载都重新渲染 -->
            <div class="map" id="4" v-if="true"></div>
          </div>

          <div class="right-con public-bg">
            <!-- <div class="public-title">水质类别占比</div> -->
            <!-- 加上v-if,使得每次加载都重新渲染 -->
            <!-- <div class="map" id="5" v-if="true"></div> -->
            <router-link to="/">
              <img src="../img/发芽.png" style="width: 50%; height: 50%" />
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import * as chinaMap from "./china.json";
export default {
  data() {
    return {
      bg: require('../img/bg.jpg')
    };
  },
  methods: {
    initCharts_mid() {
      var myChart = echarts.init(document.getElementById("midmap"));
      // 注册地图
      echarts.registerMap("china", chinaMap);
      //配置数据
      var option = {
        title: {
          text: "全国水资源分布图",
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
            ],
            type: "map",
            map: "china",
            zoom: 1.2, //放大
            // scaleLimit: {
            //   min: 0.5,
            //   max: 2.0,
            // },
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
    initCharts_avragewater() {
      // const sdata = index.fetchData();
      var myChart = echarts.init(document.getElementById("avragewater"));
      var option = {
        legend: {
          show: false,
          left: "center",
          top: "bottom",
          data: [
            "湖南省",
            "湖北省",
            "北京市",
            "天津市",
            "山西省",
            "内蒙古自治区",
            "辽宁省",
            "吉林省",
            "黑龙江省",
            "上海市",
            "江苏省",
            "浙江省",
            "安徽省",
            "福建省",
            "江西省",
            "山东省",
            "河南省",
            "广东省",
            "广西壮族自治区",
            "海南省",
            "贵州省",
            "四川省",
            "重庆市",
            "西藏自治区",
            "陕西省",
            "甘肃省",
            "青海省",
            "宁夏回族自治区",
            "新疆维吾尔自治区",
          ],
        },
        series: [
          {
            name: "Radius Mode",
            type: "pie",
            radius: [5, 100],
            roseType: "radius",
            itemStyle: {
              borderRadius: 5,
            },
            label: {
              show: false,
            },
            emphasis: {
              label: {
                show: true,
              },
            },
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
            ],
          },
        ],
      };
      myChart.setOption(option);
    },
    initCharts_leftmid() {
      var myChart = echarts.init(document.getElementById("landwater"));
      var option = {
        title: {
          text: "主流游戏玩家占比",

          subtext: "虚拟数据",
          left: "center",
        },
        tooltip: {
          trigger: "item",
        },
        legend: {
          orient: "vertical",
          left: "left",
        },
        series: [
          {
            name: "Access From",
            type: "pie",
            radius: "50%",
            data: [
              { value: 1048, name: "LOL" },
              { value: 735, name: "csgo" },
              { value: 580, name: "Mincraft" },
              { value: 484, name: "永劫无间" },
              { value: 300, name: "航海狼人杀" },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      };
      myChart.setOption(option);
    },
    initCharts_leftdown() {
      var myChart = echarts.init(document.getElementById("3"));
      var option = {
        title: {
          text: "Basic Radar Chart",
        },
        legend: {
          data: ["Allocated Budget", "Actual Spending"],
        },
        radar: {
          // shape: 'circle',
          indicator: [
            { name: "Sales", max: 6500 },
            { name: "Administration", max: 16000 },
            { name: "Information Technology", max: 30000 },
            { name: "Customer Support", max: 38000 },
            { name: "Development", max: 52000 },
            { name: "Marketing", max: 25000 },
          ],
        },
        series: [
          {
            name: "Budget vs spending",
            type: "radar",
            data: [
              {
                value: [4200, 3000, 20000, 35000, 50000, 18000],
                name: "Allocated Budget",
              },
              {
                value: [5000, 14000, 28000, 26000, 42000, 21000],
                name: "Actual Spending",
              },
            ],
          },
        ],
      };
      myChart.setOption(option);
    },
    initCharts_righttop() {
      var myChart = echarts.init(document.getElementById("4"));
      var option = {
        // title: {
        //   text: "Stacked Area Chart",
        // },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
            label: {
              backgroundColor: "#6a7985",
            },
          },
        },
        legend: {
          data: ["Email", "Union Ads", "Video Ads", "Direct", "Search Engine"],
        },
        toolbox: {
          feature: {
            saveAsImage: {},
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: [
          {
            type: "category",
            boundaryGap: false,
            data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
          },
        ],
        yAxis: [
          {
            type: "value",
          },
        ],
        series: [
          {
            name: "Email",
            type: "line",
            stack: "Total",
            areaStyle: {},
            emphasis: {
              focus: "series",
            },
            data: [120, 132, 101, 134, 90, 230, 210],
          },
          {
            name: "Union Ads",
            type: "line",
            stack: "Total",
            areaStyle: {},
            emphasis: {
              focus: "series",
            },
            data: [220, 182, 191, 234, 290, 330, 310],
          },
          {
            name: "Video Ads",
            type: "line",
            stack: "Total",
            areaStyle: {},
            emphasis: {
              focus: "series",
            },
            data: [150, 232, 201, 154, 190, 330, 410],
          },
          {
            name: "Direct",
            type: "line",
            stack: "Total",
            areaStyle: {},
            emphasis: {
              focus: "series",
            },
            data: [320, 332, 301, 334, 390, 330, 320],
          },
          {
            name: "Search Engine",
            type: "line",
            stack: "Total",
            label: {
              show: true,
              position: "top",
            },
            areaStyle: {},
            emphasis: {
              focus: "series",
            },
            data: [820, 932, 901, 934, 1290, 1330, 1320],
          },
        ],
      };
      myChart.setOption(option);
    },
    initCharts_rightmid() {
      var myChart = echarts.init(document.getElementById("5"));
      var option = {
        xAxis: {},
        yAxis: {},
        series: [
          {
            symbolSize: 20,
            data: [
              [10.0, 8.04],
              [8.07, 6.95],
              [13.0, 7.58],
              [9.05, 8.81],
              [11.0, 8.33],
              [14.0, 7.66],
              [13.4, 6.81],
              [10.0, 6.33],
              [14.0, 8.96],
              [12.5, 6.82],
              [9.15, 7.2],
              [11.5, 7.2],
              [3.03, 4.23],
              [12.2, 7.83],
              [2.02, 4.47],
              [1.05, 3.33],
              [4.05, 4.96],
              [6.03, 7.24],
              [12.0, 6.26],
              [12.0, 8.84],
              [7.08, 5.82],
              [5.02, 5.68],
            ],
            type: "scatter",
          },
        ],
      };
      myChart.setOption(option);
    },
    initCharts_rightdown() {
      var myChart = echarts.init(document.getElementById("6"));
      var option = {
        graphic: {
          elements: [
            {
              type: "group",
              left: "center",
              top: "center",
              children: new Array(7).fill(0).map((val, i) => ({
                type: "rect",
                x: i * 20,
                shape: {
                  x: 0,
                  y: -40,
                  width: 10,
                  height: 80,
                },
                style: {
                  fill: "#5470c6",
                },
                keyframeAnimation: {
                  duration: 1000,
                  delay: i * 200,
                  loop: true,
                  keyframes: [
                    {
                      percent: 0.5,
                      scaleY: 0.3,
                      easing: "cubicIn",
                    },
                    {
                      percent: 1,
                      scaleY: 1,
                      easing: "cubicOut",
                    },
                  ],
                },
              })),
            },
          ],
        },
      };
      myChart.setOption(option);
    },
  },
  mounted() {
    this.initCharts_mid();
    this.initCharts_avragewater();
    // this.initCharts_leftmid();//做测试用
    // this.initCharts_leftdown();
    this.initCharts_righttop();
    // this.initCharts_rightmid();
    // this.initCharts_rightdown();
  },
};
</script>

<style>
.content-body {
  width: 100%;
  height: 100%;
  /* background-image: "../img/bg.jpg"; */
  /* background: #ffffff; */
  background-size: 100% 100%;
  position: absolute;
}
.header {
  height: 10%;
  width: 100%;
}
.header .header-left {
  width: 50%;
  float: left;
  line-height: 70px;
}
.map {
  width: 100%;
  height: 100%;
}
.header .header-left span {
  color: #ffffff;
  font-weight: bold;
  font-size: 24px;
  letter-spacing: 2px;
  padding: 0 20px;
}
.header .header-time {
  width: 48%;
  line-height: 70px;
  float: right;
  text-align: right;
  padding-right: 20px;
}
.header .header-time span {
  color: #ffffff;
}
.content {
  width: 100%;
  /* height: calc(100% - 75px); */
  height: 100%;
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
}
.left-body .left-top {
  width: 100%;
  height: 50%;
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
.public-bg {
  background: rgba(12, 26, 63, 0.3);
}
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
}
.right-body {
  width: 30%;
  height: 100%;
  float: left;
  /* margin: 0 0.3%; */
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
