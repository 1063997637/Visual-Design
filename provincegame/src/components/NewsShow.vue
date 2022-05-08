<template>
  <div class="scroll">
    <div>近日农业看点</div>
    <vue3-seamless-scroll
      :list="this.onlinenews"
      :step="0.5"
      :hover="true"
      v-if="this.onlinenews.length > 0"
    >
      <div class="item" v-for="(item, index) in this.onlinenews" :key="index">
        <span :data-obj="JSON.stringify(item)" @click="handleButton">
        <!-- <span> -->
          {{item.id}}.{{ item.title }}
        </span>
        <span>{{ item.date }}</span>
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
      newsurl: "http://172.17.12.75:8000/hnnyyw/title",
      onlinenews: [],
    };
  },
  components: {
    Vue3SeamlessScroll,
  },
  methods: {
    getnewstitle() {
      axis.get(this.newsurl).then((res) => {
        // console.log(res);
        for (let i = 0; i < res.data.length; i++) {
          this.onlinenews.push({
            id:res.data[i].id,
            title: res.data[i].title,
            date: res.data[i].date,
          });
        }
        // console.log(this.onlinenews);
      });
    },
    handleButton(e) {
      let InfoAnync = JSON.parse(e.target.dataset.obj);
      console.log(InfoAnync.id);
      // location.href = "/NewsView"; //测试效果
    },
  },
  mounted() {
    this.getnewstitle();
    console.log(this.onlinenews);
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