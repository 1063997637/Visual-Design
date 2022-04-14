<template>
  <div class="content-body">
    <!-- <div class="title">水资源各省分布情况</div> -->
    <div id="main" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";
export default {
  data() {
    return {
    };
  },
  props: {
    listdata: {
      type: Array,
      default: function () {
        return [];
      },
    },
  },
  methods: {
    initCharts() {
      var myChart = echarts.init(document.getElementById("main"));
      //配置数据
      var option = {
        title: {
          text: "粮食产量统计图",
          textStyle: {
            color: "#5881c4",
          },
        },
        xAxis: {
          type: "category",
          // data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: "value",
        },
        tooltip: {
          trigger: "item",
        },
        dataZoom: [
          {
            type: "slider",
            show: true,
            xAxisIndex: [0],
            start: 1,
            end: 35,
          },
          {
            type: "inside",
            xAxisIndex: [0],
            start: 1,
            end: 35,
          },
        ],
        series: [
          {
            //   data: [120, 200, 150, 80, 70, 110, 130],
            data: this.listdata,
            type: "bar",
            showBackground: true,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.2)",
            },
            itemStyle: {
              color: "orange",
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
      };
           setTimeout(() => {
        myChart.setOption(option, true);
      }, 1000);
    },
  },
  mounted() {
    this.initCharts();
  },
};
</script>

<style>
.content-body {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  position: relative;
}
</style>