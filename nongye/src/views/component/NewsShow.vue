<template>
  <div class="scroll">
    <div>今日农业看点</div>
    <vue3-seamless-scroll :list="localnews" :step="0.5" :hover="true">
      <div class="item" v-for="(item, index) in localnews" :key="index">
        <span :data-obj="JSON.stringify(item)" @click="handleButton">{{
          item.title
        }}</span>
        <span>{{ item.id }}</span>
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
      list: [
        {
          title: "Vue3.0 无缝滚动组件展示数据第1条",
          date: "aaaaaa",
        },
        {
          title: "Vue3.0 无缝滚动组件展示数据第2条",
          date: "什么什么什么什么",
        },
        {
          title: "Vue3.0 无缝滚动组件展示数据第3条",
          date: "什么什么什么什么",
        },
        {
          title: "Vue3.0 无缝滚动组件展示数据第4条",
          date: Date.now(),
        },
        {
          title: "Vue3.0 无缝滚动组件展示数据第5条",
          date: Date.now(),
        },
        {
          title: "Vue3.0 无缝滚动组件展示数据第6条",
          date: Date.now(),
        },
        {
          title: "Vue3.0 无缝滚动组件展示数据第7条",
          date: Date.now(),
        },
        {
          title: "Vue3.0 无缝滚动组件展示数据第8条",
          date: Date.now(),
        },
        {
          title: "Vue3.0 无缝滚动组件展示数据第9条",
          date: Date.now(),
        },
      ],
      onlinenews: [],
      localnews: [
        { id: 1, title: "2022年大学生志愿服务西部计划启动" },
        { id: 2, title: "农业经营主体信贷直通车授信金额已达205.77亿元" },
        {
          id: 3,
          title: "三部门:2025年,在具备条件的地区基本实现村村通快递",
        },
        {
          id: 4,
          title: "第八届中国国际“互联网+”大学生创新创业大赛启动",
        },
        {
          id: 5,
          title: "“中国减贫事业取得非凡成就”",
        },
        {
          id: 6,
          title: "城乡残疾人就业规模达881.6万人",
        },
        {
          id: 7,
          title: "全国农业社会化服务典型开始征集",
        },
        {
          id: 8,
          title:
            "习近平:解放思想开拓创新团结奋斗攻坚克难 加快建设具有世界影响力的中...",
        },
        {
          id: 9,
          title: "李克强主持召开国务院常务会议",
        },
        {
          id: 10,
          title: " 国家级制种基地增加到216个“十四五”末供种保障能力将提高到80%",
        },
        {
          id: 11,
          title: " 农业农村部印发《国家级农作物种质资源库(圃)管理规范》",
        },
        {
          id: 12,
          title:
            " 重拳整治违法活动 切实维护渔业秩序    ——农业农村部有关部门负责人...",
        },
        {
          id: 13,
          title: "重拳整治违法活动 切实维护渔业秩序",
        },
        {
          id: 14,
          title:
            "农业农村部召开部领导专题会强调积极应对疫情影响 维护农业生产流通秩...",
        },
        {
          id: 15,
          title: "商务部多措并举促进货运物流畅通保障市场供应",
        },
      ],
    };
  },
  components: {
    Vue3SeamlessScroll,
  },
  methods: {
    getnewstitle() {
      axis.get("http://43.138.199.177:8000/nyyw/title").then((res) => {
        console.log(res.data);
        res.replace
        JSON.parse()
        for (let i = 0; i < res.data.length; i++) {
          var it1 = res.data[i].id;
          var it2 = res.data[i].title;
          var it3 = res.data[i].date;
          var item = { name: it1, value: it2 ,date:it3};
          that.propProvince.push(item);
        }
      });
    },
    handleButton(e) {
      let InfoAnync = JSON.parse(e.target.dataset.obj);
      console.log(InfoAnync);
      // location.href = "/NewsView"; //测试效果
    },
  },
  mounted() {
    this.getnewstitle();
    // setInterval(() => {
    //   this.list.push({
    //     title: "我是新增的一条数据",
    //     date: Date.now(),
    //   });
    // }, 10000);
  },
});
</script>



<style scoped>
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

.scroll > div:first-child {
  font-weight: bold;
  color: darkcyan;
  text-align: center;
}

.scroll > div:last-child {
  margin-top: 15px;
  height: 260px;
  overflow: hidden;
}

.scroll .item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 3px 0;
  cursor: pointer;
}
.scroll .item span {
  color: darkcyan;
  /* font-size: 17px; */
}
</style>