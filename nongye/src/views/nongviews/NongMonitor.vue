<template>
  <div class="whole-body">
    <div class="bnt-view">
      <div class="topbnt_left fl">
        <ul>
          <li><router-link to="/"> 主页 </router-link></li>
          <li><router-link to="/nongguide"> 展览馆 </router-link></li>
        </ul>
      </div>
      <h1 class="tith1 fl">农业基地</h1>
      <div class="fr topbnt_right">
        <ul>
          <li class="active">
            <router-link to="/nongmonitor"> 监测馆 </router-link>
          </li>
          <li><router-link to="/nongview"> 数据馆 </router-link></li>
        </ul>
      </div>
    </div>
    <div class="content">
<price-show/>
    </div>
  </div>
</template>

<script>
import PriceShow from "./nongcomponent/PriceShow.vue";


export default({
      components: {
       PriceShow
      },
});
</script>


<style scoped>
.whole-body {
  background: url("../../img/bg.jpg");
  background-size: 100% 100%;
  width: 100%;
  height: 100%;
  position: fixed;
}
.bnt-view {
  height: 10%;
  width: 100%;
  /* display: inline-block; */
  /* border: 1px solid red; */
}
.fl {
  float: left;
}
.fr {
  float: right;
}
.topbnt_left {
  width: 33%;
  height: 100%;
}
.topbnt_left ul {
  padding-top: 15
PriceShowpx;
  padding-left: 10%;
  width: 100%;
}
.topbnt_left li {
  background: url("../../img/bnt.png") center;
  font-size: 14px;
  line-height: 33px;
  background-repeat: no-repeat;
  width: 18%;
  height: 35px;
  float: left;
  text-align: center;
  margin-left: 15%;
}
.topbnt_left li a {
  text-decoration: none;
  color: #fff;
}
.topbnt_left li.active,
.topbnt_right li.active {
  background: url("../../img/bntactive.png") no-repeat center;
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
.topbnt_right {
  width: 33%;
  height: 100%;
}
.topbnt_right ul {
  padding-top: 15px;
  padding-left: 10%;
  width: 100%;
}
.topbnt_right li {
  background: url("../../img/bnt.png") center;
  font-size: 14px;
  line-height: 33px;
  background-repeat: no-repeat;
  width: 18%;
  height: 35px;
  float: right;
  text-align: center;
  margin-right: 25%;
}
.topbnt_right li a {
  text-decoration: none;
  color: #fff;
}
.content {
  margin-left: 10%;
  width: 80%;
  height: 80%;
  border: 1px solid red;
  background: #fff;
}
    .scroll {
      display: inline-block;
      height: 300px;
      width: 390px;
      margin: 0 25px;
      overflow: hidden;
      position: relative;
    }

    .scroll>div:first-child {
      font-weight: bold;
      color: red;
      text-align: center;
    }

    .scroll>div:last-child {
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