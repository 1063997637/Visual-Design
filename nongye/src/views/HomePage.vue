<template>
  <div class="content-body">
    <h1 class="title">农业帮</h1>
    <div class="leftmap">
      <div id="Home" style="width: 100%; height: 100%"></div>
      <span class="border_bg_leftTop"></span>
      <span class="border_bg_rightTop"></span>
      <span class="border_bg_leftBottom"></span>
      <span class="border_bg_rightBottom"></span>
    </div>
    <div class="right-top">
      <weather-show />
      <!-- <time-view /> -->
      <span class="border_bg_leftTop"></span>
      <span class="border_bg_rightTop"></span>
      <span class="border_bg_leftBottom"></span>
      <span class="border_bg_rightBottom"></span>
    </div>
    <div class="righttest">
      <news-show @click="show" /><news-view
        :showModel="this.showModel"
        :newstitle="newsti"
        :newsbody="newsbo"
        @click="showModel = false"
      />
      <span class="border_bg_leftTop"></span>
      <span class="border_bg_rightTop"></span>
      <span class="border_bg_leftBottom"></span>
      <span class="border_bg_rightBottom"></span>
    </div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import * as chinaMap from "./china.json";
import NewsShow from "./component/NewsShow.vue";
import NewsView from "./component/NewsView.vue"; //弹窗
// import TimeView from "./component/TimeView.vue";
import WeatherShow from "./component/WeatherShow.vue";
export default {
  components: { NewsShow, NewsView, WeatherShow },
  data() {
    return {
      newsti: "中国减贫事业取得非凡成就",
      newsbo:
        "近日,财政部、国务院发展研究中心与世界银行共同发布《中国减贫四十年:驱动力量、借鉴意义和未来政策方向》报告。报告梳理了中国减贫的主要成就,总结了中国减贫经验对其他发展中国家的借鉴意义。世界银行中国局局长芮泽接受本报记者专访时表示,按照世界银行每人每天1.9美元的全球绝对贫困标准衡量,中国在1981年至2018年间减少的贫困人口数量占到同期全球减贫人数的近75%,“中国减贫事业取得非凡成就。“中国的减贫故事是一个有关经济增长和转型的故事,改革开放是中国减贫故事的开端。”芮泽表示,保持经济持续快速增长是中国解决贫困问题的主要驱动力,高储蓄和高投资率、大量基础设施投资、健全的宏观经济政策、良好的治理等为中国减贫提供了支持。此外,中国实行有针对性的精准扶贫政策,各部门协调一致推进减贫工作。“在我看来,中国的减贫故事是一个非常有说服力的发展故事。”近几年,芮泽经常到中国农村地区访问,与当地扶贫工作组沟通交流。“我曾到访一个中国的少数民族村庄,那里有一位来自大城市的年轻工程师,已经在当地工作了3年。为更好与群众交流、开展减贫工作,他努力学会了当地方言。”这令芮泽印象深刻。",
      staticdata: [
        { name: "湖南省", value: 10000 },
        { name: "云南省", value: 13000 },
        { name: "湖北省", value: 11000 },
        { name: "北京市", value: 12000 },
        { name: "天津市", value: 13000 },
        { name: "山西省", value: 14000 },
        { name: "内蒙古自治区", value: 15000 },
        { name: "辽宁省", value: 16000 },
        { name: "吉林省", value: 17000 },
        { name: "黑龙江省", value: 18000 },
        { name: "上海市", value: 19000 },
        { name: "江苏省", value: 20000 },
        { name: "浙江省", value: 21000 },
        { name: "安徽省", value: 23000 },
        { name: "福建省", value: 25000 },
        { name: "江西省", value: 26000 },
        { name: "山东省", value: 28000 },
        { name: "河南省", value: 26900 },
        { name: "广东省", value: 29000 },
        { name: "广西壮族自治区", value: 29502 },
        { name: "海南省", value: 29990 },
        { name: "贵州省", value: 30500 },
        { name: "四川省", value: 30600 },
        { name: "重庆市", value: 32000 },
        { name: "西藏自治区", value: 33000 },
        { name: "陕西省", value: 35000 },
        { name: "甘肃省", value: 36000 },
        { name: "青海省", value: 37000 },
        { name: "河北省", value: 38100 },

        { name: "宁夏回族自治区", value: 38000 },
        { name: "新疆维吾尔自治区", value: 39000 },
      ],
      showModel: false,
    };
  },
  methods: {
    show() {
      this.showModel = true;
      console.log(this.showModel);
    },
    initCharts(Dom) {
      var myChart = echarts.init(Dom);
      console.log("开始加载");
      myChart.showLoading();
      // 注册地图
      echarts.registerMap("china", chinaMap);
      //配置数据
      var option = {
        title: {
          left: "center",
          text: "中国地图",
          textStyle: {
            color: "#5881c4",
          },
        },
        tooltip: {
          trigger: "item",
        },
        series: [
          {
            name: "粮食总产量(万吨)",
            data: this.staticdata,
            type: "map",
            map: "china",
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
          textStyle: {
            color: "#5881c4",
          },
          label: {
            show: true,
          },
          min: 10000,
          max: 50000,
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
      myChart.setOption(option, true);
      myChart.hideLoading();
      myChart.on("click", function (params) {
        if (params.data.name == "安徽省") {
          location.href = "/anhui"; //测试效果
        }
        if (params.data.name == "北京省") {
          location.href = "/beijing"; //测试效果
        }
        if (params.data.name == "重庆市") {
          location.href = "/chongqing"; //测试效果
        }
        if (params.data.name == "福建省") {
          location.href = "/fujian"; //测试效果
        }
        if (params.data.name == "甘肃省") {
          location.href = "/gansu"; //测试效果
        }
        if (params.data.name == "广东省") {
          location.href = "/guangdong"; //测试效果
        }
        if (params.data.name == "广西省") {
          location.href = "/guangxi"; //测试效果
        }
        if (params.data.name == "贵州省") {
          location.href = "/guizhou"; //测试效果
        }
        if (params.data.name == "海南省") {
          location.href = "/hainan"; //测试效果
        }
        if (params.data.name == "河北省") {
          location.href = "/hebei"; //测试效果
        }
        if (params.data.name == "黑龙江省") {
          location.href = "/heilongjiang"; //测试效果
        }
        if (params.data.name == "河南省") {
          location.href = "/henan"; //测试效果
        }
        if (params.data.name == "湖北省") {
          location.href = "/hubei"; //测试效果
        }
        if (params.data.name == "湖南省") {
          location.href = "/hunan"; //测试效果
        }
        if (params.data.name == "江苏省") {
          location.href = "/jiangsu"; //测试效果
        }
        if (params.data.name == "江西省") {
          location.href = "/jiangxi"; //测试效果
        }
        if (params.data.name == "吉林省") {
          location.href = "/jilin"; //测试效果
        }
        if (params.data.name == "辽宁省") {
          location.href = "/liaoning"; //测试效果
        }
        if (params.data.name == "内蒙古自治区") {
          location.href = "/neimeng"; //测试效果
        }
        if (params.data.name == "宁夏回族自治区") {
          location.href = "/anhui"; //测试效果
        }
        if (params.data.name == "青海省") {
          location.href = "/qinghai"; //测试效果
        }
        if (params.data.name == "山东省") {
          location.href = "/shandong"; //测试效果
        }
        if (params.data.name == "上海市") {
          location.href = "/shanghai"; //测试效果
        }
        if (params.data.name == "山西省") {
          location.href = "/shanxi"; //测试效果
        }
        if (params.data.name == "四川省") {
          location.href = "/sichuan"; //测试效果
        }
        if (params.data.name == "天津市") {
          location.href = "/tianjin"; //测试效果
        }
        if (params.data.name == "陕西省") {
          location.href = "/xian"; //测试效果
        }
        if (params.data.name == "新疆维吾尔族自治区") {
          location.href = "/xinjiang"; //测试效果
        }
        if (params.data.name == "西藏自治区") {
          location.href = "/xizang"; //测试效果
        }
        if (params.data.name == "云南省") {
          location.href = "/yunnan"; //测试效果
        }
        if (params.data.name == "浙江省") {
          location.href = "/zhejiang"; //测试效果
        }
      });
    },
  },
  mounted() {
    this.initCharts(document.getElementById("Home"));
  },
};
</script>

<style scoped>
.content-body {
  background: url("../img/bg2.jpg");
  width: 100%;
  height: 100%;
  background-size: 100% 100%;
  position: absolute;
  /* border: 1px solid red; */
}
.content-body .title {
  color: #ffffff;
  position: relative;
  margin: 0;
  margin-top: 0.5%;
  height: 3%;
  width: 100%;
  /* padding-top: 10%; */
  letter-spacing: 8px;
  text-align: center;
  font-size: 30px;
  /* border: 1px solid red; */

  position: relative;
}
.content-body .leftmap {
  top: 3.5%;
  left: 1.5%;
  width: 50%;
  height: 90%;
  float: left;
  position: relative;
  border: 1px solid #05d1fc;

  /* border: 1px solid red; */
}
.content-body .righttest {
  position: relative;
  top: 13%;
  left: 2%;
  width: 46.5%;
  height: 50%;
  float: left;
  border: 1px solid #05d1fc;
}
.border_bg_leftTop {
  position: absolute;
  /* left:-5rem; */
  top: -1.1rem;
  width: 5rem;
  height: 1rem;
  display: block;
  background: url("../img/title_left_bg.png");
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
  background: url(../img/border_bg.jpg) no-repeat;
  background-size: 100% 100%;
}
.border_bg_leftBottom {
  position: absolute;
  left: -0.1rem;
  bottom: -0.1rem;
  width: 1.5rem;
  height: 1.5rem;
  display: block;
  background: url(../img/border_bg.jpg) no-repeat;
  background-size: 100% 100%;
}
.border_bg_rightBottom {
  position: absolute;
  right: -0.2rem;
  bottom: -0.2rem;
  width: 1.5rem;
  height: 1.5rem;
  display: block;
  background: url(../img/title_right_bg.png) no-repeat;
  background-size: 100% 100%;
}
.content-body .right-top {
  margin: 0;
  position: relative;
  top: 8%;
  left: 2%;
  width: 46.5%;
  height: 30%;
  float: left;
  border: 1px solid #05d1fc;
}
.fl {
  float: left;
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
</style>