<template>
  <div class="content-body">
    <!-- <div class="title">水资源各省分布情况</div> -->
    <div id="muye" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";
export default {
  // name:"ToltalPro",
  data() {
    return {
      totaldata: [{}],
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
    initCharts(Dom) {
      var myChart = echarts.init(Dom);
      //配置数据
      var option = {
        title: {
          text: "牧业",
          textStyle: {
            color: "#5881c4",
          },
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
          
        },
        legend: {
          textStyle: {
            color: "orange",
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: {
          name: "产量(万吨)",
          type: "value",
          boundaryGap: [0, 0.01],
        },
        yAxis: {
          type: "category",
          data: ["猪", "牛", "羊", "牛奶", "鸡蛋", "蜂蜜"],
        },
        series: [
          {
            name: "出栏量",
            type: "bar",
            data: [218203, 232489, 219034, 0, 0, 0],
          },
          {
            name: "产品产量",
            type: "bar",
            data: [111325, 131438, 111000, 121594, 134141, 681807],
          },
        ],
      };
      myChart.setOption(option, true);
    },
  },
  mounted() {
    this.initCharts(document.getElementById("muye"));
  },
};
</script>

<style scoped>
.content-body {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  position: relative;
}
</style>