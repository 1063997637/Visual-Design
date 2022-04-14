<template>
  <div>
    <p>这是测试页面{{ message }}</p>
    <h1>
      接口数据处理测试
      <br />
    </h1>
    <p>
      {{ data }}
    </p>
    <h1>
      静态数据格式确定
      <br />
    </h1>
    <p>
      {{ data2 }}
    </p>
  </div>
</template>

<script>
import axis from "axios";
export default {
  data() {
    return {
      message: "",
      data: [],
      data2: [
        { name: "北京市", value: 25.8 },
        { name: "天津市", value: 13.3 },
        { name: "河北省", value: 146.3 },
        { name: "山西省", value: 115.2 },
        { name: "内蒙古自治区", value: 503.9 },
        { name: "辽宁省", value: 397.1 },
        { name: "吉林省", value: 586.2 },
        { name: "黑龙江省", value: 1419.9 },
        { name: "上海市", value: 58.6 },
        { name: "江苏省", value: 543.4 },
        { name: "浙江省", value: 1026.6 },
        { name: "安徽省", value: 1280.4 },
        { name: "福建省", value: 760.3 },
        { name: "江西省", value: 1685.6 },
        { name: "山东省", value: 375.3 },
        { name: "河南省", value: 408.6 },
        { name: "湖北省", value: 1754.7 },
        { name: "广东省", value: 1626 },
        { name: "湖南省", value: 2118.9 },
        { name: "广西壮族自治区", value: 2114.8 },
        { name: "海南省", value: 263.6 },
        { name: "重庆市", value: 766.9 },
        { name: "四川省", value: 3237.3 },
        { name: "贵州省", value: 1328.6 },
        { name: "云南省", value: 1799.2 },
        { name: "西藏自治区", value: 4597.3 },
        { name: "陕西省", value: 419.6 },
        { name: "甘肃省", value: 408 },
        { name: "青海省", value: 1011.9 },
        { name: "宁夏回族自治区", value: 11 },
        { name: "新疆维吾尔自治区", value: 801 },
      ],
    };
  },
  methods: {
    getdatas() {
      var that = this;
      // var sdata = [];
      axis.get("http://127.0.0.1:8000/shuiziyuan/").then((res) => {
        that.message = res.data;
        for (let i = 0; i < res.data.length; i++) {
          undefined;
          //   var sdata = { name: "", value: "" };
          //   sdata.name = res.data[i].fields.年份;
          //   sdata.value = res.data[i].fields.省份编码;
          var it1 = res.data[i].fields.省份;
          var it2 = res.data[i].fields.水资源总量_亿立方米_field;
          var item = { name: it1, value: it2 };
          that.data.push(item);
          // console.log(that.data2[i].value);
          // console.log(typeof that.data2[i].value);
          // console.log("上面为静态数据，下面是接口获取的");
          // console.log(that.data[i].value);
          // console.log(typeof that.data[i].value);
        }
        console.log(this.data[0].name);
        console.log(this.data[0].value);
        console.log(typeof this.data[0].name);
        console.log(typeof this.data[0].value);

        console.log("上面为接口获取，下为静态");
        console.log(this.data2[0].name);
        console.log(this.data2[0].value);
        console.log(typeof this.data2[0].name);
        console.log(typeof this.data2[0].value);
      });
    },
  },
  mounted() {
    this.getdatas();
  },
};
</script>

<style>
</style>