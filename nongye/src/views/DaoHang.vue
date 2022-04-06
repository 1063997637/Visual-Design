<template>
  <div
    class="content"
    v-bind:style="{
      backgroundImage: 'url(' + bg + ')',
      backgroundRepeat: 'no-repeat',
      backgroundSize: '100% 100%',
    }"
  >
    <div class="nong">
      <router-link to="/maptest">
        <img src="../img/发芽.png" style="width: 50%; height: 50%" />
      </router-link>
    </div>
    <div class="lin">
      <router-link to="/mapuse">
        <img src="../img/森林.png" style="width: 50%; height: 50%" />
      </router-link>
    </div>
    <div class="mu">
      <router-link to="/maptest">
        <img src="../img/奶牛.png" style="width: 50%; height: 50%" />
      </router-link>
    </div>
    <div class="yu">
      <router-link to="/mapuse">
        <img src="../img/鱼.png" style="width: 50%; height: 50%" />
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      bg: require('../img/bgr.jpg')
  }
}

};
</script>

<style scoped>
/* 定义动画 */

@keyframes move {
  /* 开始状态 */
  0% {
    transform: translateY(0px);
  }
  /* 结束状态 */
  100% {
    transform: translateY(10px);
  }
}
.background {
  height: 100%;
  width: 100%;
  z-index: -1;
}
.content {
  position: absolute;
  height: 98%;
  width: 99%;
}
.content .nong {
  float: left;
  margin-top: 33%;
  width: 25%;
  height: 25%;
  /* 使用动画 */
  animation-name: move;
  animation-duration: 1.5s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
.content .lin {
  float: left;
  width: 25%;
  height: 25%;
  /* 使用动画 */
  animation-name: move;
  animation-duration: 1.5s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
.content .mu {
  float: left;
  margin-top: 15%;
  width: 25%;
  height: 25%;
  /* 使用动画 */
  animation-name: move;
  animation-duration: 1.5s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
.content .yu {
  float: left;
  width: 25%;
  height: 25%;
  /* 使用动画 */
  animation-name: move;
  animation-duration: 1.5s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
</style>