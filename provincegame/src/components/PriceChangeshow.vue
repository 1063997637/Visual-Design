<template>
  <div class="content-body">
    <div id="main4" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
import axis from "axios";
import * as echarts from "echarts";
export default {
  data() {
    return {
      pricedata: [],
      staticdata: [
        [2.3, 2.45, 2.2, 1.35, 1.35, 1.9, 1.9, 2.75, 1.75, 1.9, 2.2, 1.9728],
        [3.4, 3, 3.25, 2.25, 2.25, 3.25, 4.25, 4.25, 3.75, 1.25, 2.8, 2.983],
        [2.25, 3.25, 3.15, 2.65, 2.15, 1.85, 1.85, 3.5, 2.05, 2, 1.6, 1.9526],
        [1.6, 1.07, 1.17, 1.22, 1.05, 0.7, 0.8, 1.4, 1.18, 1.13, 1.1, 1.0176],
        [4, 6, 2.5, 2.75, 3.5, 4.25, 4.6, 4.25, 3.25, 2.5, 3.5, 3.31],
        [0.95, 1.24, 0.8, 0.85, 0.9, 0.7, 0.95, 0.9, 0.95, 1.55, 1, 1.09],
        [1.35, 2, 2.05, 1.5, 1.2, 0.9, 1.25, 2, 1.6, 2.4, 1.75, 1.783],
        [2, 2.85, 4.75, 3.5, 2.6, 2.25, 2.25, 3.9, 5, 6.3, 3.25, 4.554],
        [3.25, 2.5, 3.35, 3.25, 3.75, 3.15, 2.5, 2.6, 2.75, 2.75, 2.75, 2.763],
        [1.75, 2.4, 3.8, 1.15, 1.35, 1, 1.55, 2.65, 2.17, 3.22, 1.6, 2.134],
        [1.85, 1.45, 1.6, 1.8, 1.25, 1.45, 1.9, 2.1, 3.52, 3.15, 1.5, 2.541],
      ],
    };
  },
  methods: {
    initCharts() {
      var myChart = echarts.init(document.getElementById("main4"));
      myChart.showLoading();
      //配置数据
      var option = {
        title: {
          left: "center",
          text: "种植物价格变化趋势",
          textStyle: {
            color: "#5881c4",
          },
        },
        tooltip: {
          trigger: "axis",
          // formatter: "{b}: {c}公顷" // 这里是鼠标移上去的显示数据
        },
        legend: {
          selectedMode: "single",
          left: "18%",
          top: "15%",
          data: [
            "胡萝卜",
            "大白菜",
            "芹菜",
            "菠菜",
            "大蒜",
            "花椰菜",
            "茄子",
            "青辣椒",
            "莲藕",
            "黄瓜",
            "豆角",
          ],
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
          name: "年月",
          type: "category",
          boundaryGap: false,
          data: [
            "20年7月",
            "20年9月",
            "21年1月",
            "21年3月",
            "21年5月",
            "21年7月",
            "21年9月",
            "21年11月",
            "22年1月",
            "22年3月",
            "22年5月",
            "价格预测值",
          ],
        },
        yAxis: {
          name: "价格(元/斤)",
          type: "value",
        },
        series: [
          {
            name: "胡萝卜",
            type: "line",
            stack: "Total",
            data: this.staticdata[0],
          },
          {
            name: "大白菜",
            type: "line",
            stack: "Total",
            data: this.staticdata[1],
          },
          {
            name: "芹菜",
            type: "line",
            stack: "Total",
            data: this.staticdata[2],
          },
          {
            name: "菠菜",
            type: "line",
            stack: "Total",
            data: this.staticdata[3],
          },
          {
            name: "大蒜",
            type: "line",
            stack: "Total",
            data: this.staticdata[4],
          },
          {
            name: "花椰菜",
            type: "line",
            stack: "Total",
            data: this.staticdata[5],
          },
          {
            name: "茄子",
            type: "line",
            stack: "Total",
            data: this.staticdata[6],
          },
          {
            name: "青辣椒",
            type: "line",
            stack: "Total",
            data: this.staticdata[7],
          },
          {
            name: "莲藕",
            type: "line",
            stack: "Total",
            data: this.staticdata[8],
          },
          {
            name: "黄瓜",
            type: "line",
            stack: "Total",
            data: this.staticdata[9],
          },
          {
            name: "豆角",
            type: "line",
            stack: "Total",
            data: this.staticdata[10],
          },
        ],
      };
      myChart.setOption(option, true);
      myChart.hideLoading();
      
      var i=0;
      setInterval(function () {
        myChart.dispatchAction({
          type: "legendToggleSelect",
          name: option.legend.data[++i % option.legend.data.length],
        });
      }, 1500);
    },
    getpricedata() {
      var that = this;
      for (let i = 4; i < 15; i++) {
        var url = "http://172.17.12.75:8000/price?id=" + i;
        axis.get(url).then((res) => {
          var p20_7 = res.data[0].p20_7;
          var p20_9 = res.data[0].p20_9;
          var p21_1 = res.data[0].p21_1;
          var p21_3 = res.data[0].p21_3;
          var p21_5 = res.data[0].p21_5;
          var p21_7 = res.data[0].p21_7;
          var p21_9 = res.data[0].p21_9;
          var p21_11 = res.data[0].p21_11;
          var p22_1 = res.data[0].p22_1;
          var p22_3 = res.data[0].p22_3;
          var p22_5 = res.data[0].p22_5;
          var yc = res.data[0].yc;
          that.pricedata.push([
            p20_7,
            p20_9,
            p21_1,
            p21_3,
            p21_5,
            p21_7,
            p21_9,
            p21_11,
            p22_1,
            p22_3,
            p22_5,
            yc,
          ]);
        });
      }
    },
  },
  mounted() {
    this.initCharts();
    this.getpricedata();
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