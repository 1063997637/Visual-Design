<template>
  <div class="content-body">
    <!-- <div class="title">水资源各省分布情况</div> -->
    <div id="linye" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
// import axis from "axios";
import * as echarts from "echarts";
export default {
  // name:"ToltalPro",
  data() {
    return {
      urllist:["ymmj","gzmj","ldmj","hxdmj","ddmj","mlsmj","mhmj","yczmj","scmj"],
      totaldata: [{}],
    };
  },
  methods: {
    initCharts(Dom) {
      var myChart = echarts.init(Dom);
      //配置数据
      var option = {
        title: {
          text: "作物种植面积占比",
          textStyle: {
            color: "#5881c4",
          },
        },
        tooltip: {
          trigger: "item",
          formatter: "{b}: {c}公顷 {d}%" // 这里是鼠标移上去的显示数据
        },
        legend: {
          top: "bottom",
          textStyle: {
            color: "orange",
          },
        },
        series: [
          {
            name: "Nightingale Chart",
            type: "pie",
            radius: [20, 110],
            center: ["50%", "40%"],
            roseType: "area",
            itemStyle: {
              borderRadius: 8,
            },
            data: [
              { value: 384.38, name: "玉米" },
              { value: 0, name: "谷子" },
              { value: 11.6, name: "绿豆" },
              { value: 1.22, name: "红小豆" },
              { value: 114.66, name: "大豆" },
              { value: 69.86, name: "马铃薯" },
              { value: 59.47, name: "棉花" },
              { value: 1326.45, name: "油菜籽" },
              { value: 1355.03, name: "蔬菜" },
            ],
          },
        ],
      };
      myChart.setOption(option, true);
    },
    // getsizedata(){
    //   console.log("面积");
    //         // var that = this;
    //   for (let i = 0; i < 9; i++) {
    //     var url = "http://172.17.12.75:8000/ca/" + this.urllist[i];
    //     axis.get(url).then((res) => {
            
    //     });
    //   }
    // }
  },
  mounted() {
    this.initCharts(document.getElementById("linye"));
    // this.getsizedata();
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