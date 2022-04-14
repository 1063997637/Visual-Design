<template>
  <div class="content-body">
    <!-- <div class="title">水资源各省分布情况</div> -->
    <div id="main" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import * as chinaMap from "./china.json";
import axis from "axios";
export default {
  //数据项:省份，年份，水资源
  //水资源总量,地表水资源量，地下水资源量，地表水与地下水资源重复量(亿立方米)
  //人均水资源量(立方米/人)
  data() {
    return {
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
  props: {
    propProvince: {
      type: Array,
      default: function () {
        return [];
      },
    },
  },
  methods: {
    getdatas() {
      var that = this;
      axis.get("http://127.0.0.1:8000/shuiziyuan/").then((res) => {
        that.message = res.data;
        for (let i = 0; i < res.data.length; i++) {
          var it1 = res.data[i].fields.省份;
          var it2 = res.data[i].fields.水资源总量_亿立方米_field;
          var item = { name: it1, value: it2 };
          that.propProvince.push(item);
        }
      });
    },
    initCharts(Dom, data) {
      var myChart = echarts.init(Dom);
      myChart.showLoading();
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
        legend: {
          bottom: 5,
          data: ["水资源总量", "矿产资源总量"],
          itemGap: 20,
          textStyle: {
            color: "#fff",
            fontSize: 14,
          },
          selectedMode: "single",
        },
        tooltip: {
          trigger: "item",
        },
        series: [
          {
            name: "水资源总量",
            data: data,
            // data: [
            //   { name: "湖南省", value: 1000 },
            //   { name: "湖北省", value: 1100 },
            //   { name: "北京市", value: 1200 },
            //   { name: "天津市", value: 1300 },
            //   { name: "山西省", value: 1400 },
            //   { name: "内蒙古自治区", value: 1500 },
            //   { name: "辽宁省", value: 1600 },
            //   { name: "吉林省", value: 1700 },
            //   { name: "黑龙江省", value: 1800 },
            //   { name: "上海市", value: 1900 },
            //   { name: "江苏省", value: 2000 },
            //   { name: "浙江省", value: 2100 },
            //   { name: "安徽省", value: 2300 },
            //   { name: "福建省", value: 2500 },
            //   { name: "江西省", value: 2600 },
            //   { name: "山东省", value: 2800 },
            //   { name: "河南省", value: 2690 },
            //   { name: "广东省", value: 2900 },
            //   { name: "广西壮族自治区", value: 2952 },
            //   { name: "海南省", value: 2999 },
            //   { name: "贵州省", value: 3050 },
            //   { name: "四川省", value: 3060 },
            //   { name: "重庆市", value: 3200 },
            //   { name: "西藏自治区", value: 3300 },
            //   { name: "陕西省", value: 3500 },
            //   { name: "甘肃省", value: 3600 },
            //   { name: "青海省", value: 3700 },
            //   { name: "宁夏回族自治区", value: 3800 },
            //   { name: "新疆维吾尔自治区", value: 3900 },
            // ],
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
          {
            name: "矿产资源总量",
            data: this.staticdata,
            // data: [
            //   { name: "湖南省", value: 1000 },
            //   { name: "湖北省", value: 1100 },
            //   { name: "北京市", value: 1200 },
            //   { name: "天津市", value: 1300 },
            //   { name: "山西省", value: 1400 },
            //   { name: "内蒙古自治区", value: 1500 },
            //   { name: "辽宁省", value: 1600 },
            //   { name: "吉林省", value: 1700 },
            //   { name: "黑龙江省", value: 1800 },
            //   { name: "上海市", value: 1900 },
            //   { name: "江苏省", value: 2000 },
            //   { name: "浙江省", value: 2100 },
            //   { name: "安徽省", value: 2300 },
            //   { name: "福建省", value: 2500 },
            //   { name: "江西省", value: 2600 },
            //   { name: "山东省", value: 2800 },
            //   { name: "河南省", value: 2690 },
            //   { name: "广东省", value: 2900 },
            //   { name: "广西壮族自治区", value: 2952 },
            //   { name: "海南省", value: 2999 },
            //   { name: "贵州省", value: 3050 },
            //   { name: "四川省", value: 3060 },
            //   { name: "重庆市", value: 3200 },
            //   { name: "西藏自治区", value: 3300 },
            //   { name: "陕西省", value: 3500 },
            //   { name: "甘肃省", value: 3600 },
            //   { name: "青海省", value: 3700 },
            //   { name: "宁夏回族自治区", value: 3800 },
            //   { name: "新疆维吾尔自治区", value: 3900 },
            // ],
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
            color: ["orangered", "yellow", "lightskyblue"],
          },
        },
      };
      setTimeout(() => {
        myChart.setOption(option, true);
        myChart.hideLoading();
      }, 1000);
      myChart.on('click', function (params) {
        if(params.data.name == '湖北省'){
			location.href='/viewtest';//测试效果
      <router-link to="/viewtest">
      </router-link>
			}
        });
    },
  },
  mounted() {
    this.getdatas();
    this.initCharts(document.getElementById("main"), this.propProvince);
  },
};
</script>

<style>
.content-body {
  width: 100%;
  height: 100%;
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