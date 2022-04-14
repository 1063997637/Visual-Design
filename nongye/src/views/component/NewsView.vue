<template>
  <div class="model" v-show="showModel">
    <div class="mask"></div>
    <div class="model-dialog">
      <div class="model-header">
        <span>{{ newstitle }}</span>
      </div>
      <div class="model-body">
        <div class="body">{{ newsbody }}</div>
      </div>
      <!-- <div class="model-footer">
        <button class="btn">任意点击关闭</button>
      </div> -->
    </div>
  </div>
</template>


<script>
export default {
  data(){
    return {
    };
  },
  props: {
    //是否展示弹框
    showModel: Boolean,
    newstitle:{
      type:String,
      default:"新闻标题"
    },
    newsbody:{
      type:String,
      default:"新闻内容"
    },
  },
};
</script>

<style>
.mask {
  position: absolute;
  top: 0;
  height: 100%;
  width: 100%;
  /* background-color: rgba(167, 165, 165, 0.486); */
  opacity: 0.5;
  z-index: 9;
  /* border: 1px solid red; */
}
.model-dialog {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  border-radius: 12px;
  width: 600px;
  height: 300px;
  border: 1px solid #f5f5f5;
  overflow: hidden;
  z-index: 10;
}
.model-header {
  position: relative;
  height: 30px;
  padding-left: 10px;
  padding-top: 10px;
  font-size: 20px;
  /* line-height: 50px; */
  background-color: #05d1fc;
  border-bottom: 1px solid rgb(177, 176, 176);
}
.model-body {
  height:90%;
  width: 100%;
  /* line-height: 150px; */
  margin: 0;
  padding: 0;
  /* float: left; */
  font-size: 15px;
  text-align:left;
  /* border: 1px solid red; */
  background-color: #05d1fc;
}
</style>