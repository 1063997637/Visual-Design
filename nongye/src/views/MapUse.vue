<template>
  <div class="content-body">
    <!-- <div class="title">水资源各省分布情况</div> -->
    <div id="main" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import * as chinaMap from "./china.json";
export default {
  //数据项:省份，年份，水资源
  //水资源总量,地表水资源量，地下水资源量，地表水与地下水资源重复量(亿立方米)
  //人均水资源量(立方米/人)
  data() {
    return {};
  },
  methods: {
    initCharts() {
      var myChart = echarts.init(document.getElementById("main"));
      // 注册地图
      echarts.registerMap("china", chinaMap);

      //配置数据
      var option = {
        // title: {
        //   text: "水资源各省分布情况",
        //   textStyle: {
        //     color: "red"
        //   }
        // },
        series: [
          {
            type: "map",
            map: "china",
            label: {
              //文字样式
              show: true, //选择标签是否展示,此处为省份名称
              fontSize: 10,
              fontStyle: "italic",
              color: "red",
            },
            itemStyle: {
              //区域样式
              borderColor: "blue",
              areaColor: "yellow",
            },
            // scaleLimit: {
            //   min: 0.5,
            //   max: 2.0,
            // },
            emphasis: {
              itemStyle: {
                //高亮区域样式
                borderColor: "blue",
                areaColor: "#ccc",
              },
            },
            //data用于结合visualMap筛选判断
            data: [
              { name: "湖南省", value: 1000 },
              { name: "湖北省", value: 2000 },
            ],
          },
        ],
        visualMap: {
          min: 800,
          max: 5000,
          text: ["High", "Low"],
          bottom: 100,
          left: 200,
          realtime: false,
          calculable: true,
          inRange: {
            color: ["lightskyblue", "yellow", "orangered"],
          },
        },
      };
      myChart.setOption(option);
    },
  },
  mounted() {
    this.initCharts();
  },
};
</script>

<style>
.content-body {
  width: 99%;
  height: 93%;
  background: #0d325f;
  background-size: 100% 100%;
  position: absolute;
}
.title {
  color: #ffffff;
  font-weight: bold;
  font-size: 24px;
  letter-spacing: 2px;
  padding: 0 20px;
  position: relative;
  left: 40%;
}
</style>