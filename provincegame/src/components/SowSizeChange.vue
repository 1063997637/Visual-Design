<template>
  <div class="content-body">
    <div id="main3" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";
export default {
  data() {
    return {};
  },
  methods: {
    initCharts() {
      var myChart = echarts.init(document.getElementById("main3"));
      //配置数据
      var option = {
        title: {
          text: "播种面积变化趋势",
          textStyle: {
            color: "#5881c4",
          },
        },
        tooltip: {
          trigger: "axis",
          // formatter: "{b}: {c}公顷" // 这里是鼠标移上去的显示数据

        },
        legend: {
          left:"18%",
          top:"15%",
          data: ["小麦", "玉米", "大豆", "马铃薯", "油麦菜"],
          textStyle: {
            color: "#5881c4",
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: {
          name:"年份",
          type: "category",
          boundaryGap: false,
          data: ["2015","2016", "2017", "2018", "2019", "2020", "2021"],
        },
        yAxis: {
          name:"面积(公顷)",
          type: "value",
        },
        series: [
          {
            name: "小麦",
            type: "line",
            stack: "Total",
            data: [120, 132, 101, 134, 90, 230, 210],
          },
          {
            name: "玉米",
            type: "line",
            stack: "Total",
            data: [220, 182, 191, 234, 290, 330, 310],
          },
          {
            name: "大豆",
            type: "line",
            stack: "Total",
            data: [150, 232, 201, 154, 190, 330, 410],
          },
          {
            name: "马铃薯",
            type: "line",
            stack: "Total",
            data: [320, 332, 301, 334, 390, 330, 320],
          },
          {
            name: "油麦菜",
            type: "line",
            stack: "Total",
            data: [820, 932, 901, 934, 1290, 1330, 1320],
          },
        ],
      };
      myChart.setOption(option, true);
    },
  },
  mounted() {
    this.initCharts();
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