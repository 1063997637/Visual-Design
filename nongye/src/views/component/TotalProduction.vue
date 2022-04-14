<template>
  <div class="content-body">
    <div id="main" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";
export default {
  data() {
    return {
      totaldata: [{}],
      proname:[
          "稻谷","小麦","玉米","谷子","高粱","其他谷物","绿豆","红小豆","大豆",
          "马铃薯","棉花","花生","油菜籽","蔬菜"
      ],
      staticdata: [],
    };
  },
  props: {
    xvalue: {
      type: Array,
      default: function () {
        return [];
      },
    },
    yvalue: {
      type: Array,
      default: function () {
        return [];
      },
    },
  },
  methods: {
    setdata(){
      for(var i=0;i<this.proname.length;i++){
          this.staticdata.push(Math.round(Math.random()*200));
      }
    },
    initCharts(Dom) {
      var myChart = echarts.init(Dom);
      myChart.showLoading();
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
          // data:this.xvalue,
          data:this.proname,
        },
        yAxis: {
          name:"产量(万吨)",
          type: "value",
        },
        tooltip: {
          trigger: "item",
          formatter: "{b}: {c}万吨" // 这里是鼠标移上去的显示数据
        },
        dataZoom: [
          {
            type: "slider",
            show: true,
            xAxisIndex: [0],
            start: 10,
            end: 50,
          },
          {
            type: "inside",
            xAxisIndex: [0],
            start: 10,
            end: 50,
          },
        ],
        series: [
          {
            //   data: [120, 200, 150, 80, 70, 110, 130],
            data: this.staticdata,
            // data:this.yvalue,
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
        myChart.hideLoading();
      }, 1000);
    },
  },
  mounted() {
    this.setdata();
    this.initCharts(document.getElementById("main"));
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