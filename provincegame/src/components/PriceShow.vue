<template>
  <div class="scroll">
    <div class="tab">
      <span>名称</span>
      <span>比上季度价格涨幅(元)</span>
      <span>预测未来价格(元/斤)</span>
      <span>种植推荐</span>
    </div>
    <vue3-seamless-scroll :list="pricedata" :step="0.5" :hover="true">
      <div class="item" v-for="(item, index) in pricedata" :key="index">
        <span>{{ item.name }}</span>
        <span>{{ item.pricechange }}</span>
        <span>{{ item.pricepredict }}</span>
        <span>{{ item.recommend }}</span>
      </div>
    </vue3-seamless-scroll>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { Vue3SeamlessScroll } from "vue3-seamless-scroll";
import axis from "axios";
export default defineComponent({
  data() {
    return {
      pricedata: [],
      monipricedata:[
        {
          name:"花生",
          pricechange:-0.56,
          pricepredict:1.47,
          recommend:"不推荐"
        },
        {
          name:"花生",
          pricechange:-0.56,
          pricepredict:1.47,
          recommend:"不推荐"
        },
        {
          name:"花生",
          pricechange:-0.56,
          pricepredict:1.47,
          recommend:"不推荐"
        },
        {
          name:"花生",
          pricechange:-0.56,
          pricepredict:1.47,
          recommend:"不推荐"
        },
        {
          name:"花生",
          pricechange:-0.56,
          pricepredict:1.47,
          recommend:"不推荐"
        },
        
      ],
      // 110000, 120000, 340000, 140000, 130000, 210000, 220000,440000,330000,310000,
      //   430000, 420000,
    };
  },
  components: {
    Vue3SeamlessScroll,
  },
  methods: {
    getpricedata() {
      var that = this;
      for (let i = 4; i < 15; i++) {
        var url = "http://172.17.12.75:8000/price?id=" + i;
        axis.get(url).then((res) => {
          // console.log(res.data[0].yc);
          var na = res.data[0].variety;
          var pc = parseFloat(res.data[0].p22_5-res.data[0].p22_3).toFixed(3);
          var prep = res.data[0].yc;
          var rc = pc>0?"推荐":"不推荐";
          that.pricedata.push({
            name: na,
            pricechange: pc,
            pricepredict: prep,
            recommend: rc,
          });
        });
      }
    },
  },
  mounted() {
    this.getpricedata();
    console.log(this.pricedata);
  },
});
</script>



<style scoped>
.scroll .tab {
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 3px 25px;
}
.scroll {
  /* background: #fff; */
  display: inline-block;
  height: 100%;
  width: 100%;
  /* margin-top:5%;
  margin-left: 1%; */
  overflow: hidden;
  position: relative;
}

/* .scroll > div:first-child {
  font-weight: bold;
  color: darkcyan;
  text-align: center;
} */

.scroll > div:last-child {
  margin-top: 15px;
  height: 100%;
  overflow: hidden;
}

.scroll .item {
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 3px 0px;
}
.scroll .item span {
  color: orange;
  /* font-size: 17px; */
}
</style>