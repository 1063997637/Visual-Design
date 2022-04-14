<template>
  <div class="scroll">
    <div>默认配置</div>
    <vue3-seamless-scroll :list="list">
      <div class="item" v-for="(item, index) in list" :key="index">
        <span>{{ item.title }}</span>
        <span>{{ item.date }}</span>
      </div>
    </vue3-seamless-scroll>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { Vue3SeamlessScroll } from "vue3-seamless-scroll";
export default defineComponent({
  components: {
    Vue3SeamlessScroll,
  },
  setup() {
    const list = [
      {
        title: "Vue3.0 无缝滚动组件展示数据第1条",
        date: Date.now(),
      },
      {
        title: "Vue3.0 无缝滚动组件展示数据第2条",
        date: Date.now(),
      },
      {
        title: "Vue3.0 无缝滚动组件展示数据第3条",
        date: Date.now(),
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
    ];
    return { list };
  },
  mounted() {
    setInterval(() => {
      console.log("add!!!!!!!!!");
      this.list.push({
        title: "我是新增的''一条数据",
        date: Date.now(),
      });
    }, 2000);
  },
});
</script>



<style>
.scroll {
  display: inline-block;
  height: 300px;
  width: 390px;
  margin: 0 25px;
  overflow: hidden;
  position: relative;
}

.scroll > div:first-child {
  font-weight: bold;
  color: red;
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
</style>