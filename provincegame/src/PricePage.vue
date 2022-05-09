<template>
  <div class="whole-body">
    <div class="title">
      <div class="left"><router-link to="/">实时信息</router-link></div>
      <div class="right">
        <router-link to="/pricepage">价格分析</router-link>
      </div>
    </div>
    <div class="left-body">
      <!-- <router-link to="/testpage"><h1>跳转</h1></router-link> -->
      <!-- 左边放产量？ -->
      <div class="left-top">
        <total-production />
        <span class="border_bg_leftTop"></span>
        <span class="border_bg_rightBottom"></span>
      </div>
      <div class="left-bottom">
        <sow-size />
      </div>
    </div>
    <div class="right-body">
      <div class="priceshow"><priceshow /></div>
      <div class="recommend"><price-changeshow /></div>
      <div class="right-bottom"><sow-size-change /></div>
    </div>
  </div>
</template>

<script>
import priceshow from "./components/PriceShow.vue";
// import axis from "axios";
import TotalProduction from "./components/TotalProduction.vue";
import SowSize from "./components/SowSize.vue";
import SowSizeChange from "./components/SowSizeChange.vue";
import PriceChangeshow from "./components/PriceChangeshow.vue";
export default {
  components: {
    priceshow,
    TotalProduction,
    SowSize,
    SowSizeChange,
    PriceChangeshow,
  },
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
  methods: {},
  mounted() {},
};
</script>

<style scoped>
.whole-body {
  background: #FFEFD5;
  /* background-size: 200% 100%; */
  width: 100%;
  height: 100%;
  position: relative;
  /* border: 1px solid #05d1fc; */
}
.whole-body .title {
  /* color: #ffffff; */
  /* margin: 0; */
  height: 5%;
  width: 100%;
  /* text-align: center; */
  /* border: 1px solid red; */

  /* position: relative; */
}
.title .left {
  width: 49%;
  height: 100%;
  float: left;
  text-align: center;

  /* border: 1px solid red; */
}
.title .right {
  width: 50%;
  height: 100%;
  float: left;
  /* border: 1px solid green; */

  position: relative;
}
.left-body {
  float: left;
  width: 33%;
  height: 90%;
  /* border: 1px solid red; */
}
.left-body .left-top {
  float: left;
  width: 100%;
  height: 50%;
  border: 1px solid #05d1fc;

}
.left-body .left-bottom {
  float: left;
  width: 100%;
  height: 50%;
  border: 1px solid #05d1fc;

}
.right-body {
  float: right;
  /* border: 1px solid red; */
  width: 65%;
  height: 90%;
}
.right-body .priceshow {
  float: right;
  /* border: 1px solid red; */
  width: 100%;
  height: 40%;
  border: 1px solid #05d1fc;

}
.right-body .recommend {
  float: right;
  /* border: 1px solid red; */
  width: 100%;
  height: 30%;
  border: 1px solid #05d1fc;

}
.right-body .right-bottom {
  float: right;
  /* border: 1px solid red; */
  width: 100%;
  height: 30%;
  border: 1px solid #05d1fc;

}
</style>