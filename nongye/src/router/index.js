import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'homepage',
    component: () => import('../views/HomePage.vue')
  },
  {
    path: '/mapuse',
    name: 'mapuse',
    component: () => import('../views/MapUse.vue')
  },
  {
    path: '/maptest',
    name: 'maptest',
    component: () => import('../views/MapTest.vue')
  },
  {
    path: '/apitest',
    name: 'apitest',
    component: () => import('../views/ApiTest.vue')
  },
  {
    path: '/viewtest',
    name: 'viewtest',
    component: () => import('../views/ViewTest.vue')
  },
  {
    path: '/nongguide',
    name: 'nongguide',
    component: () => import('../views/nongviews/NongGuide.vue')
  },
  {
    path: '/nongview',
    name: 'nongview',
    component: () => import('../views/nongviews/NongView.vue')
  },
  {
    path: '/nongmonitor',
    name: 'nongmonitor',
    component: () => import('../views/nongviews/NongMonitor.vue')
  },
  //省份router
  {
    path: '/anhui',
    name: 'anhui',
    component: () => import('../views/province/AnHui.vue')
  },
  {
    path: '/beijing',
    name: 'beijing',
    component: () => import('../views/province/BeiJing.vue')
  },
  {
    path: '/chongqing',
    name: 'chongqing',
    component: () => import('../views/province/ChongQing.vue')
  },
  {
    path: '/fujian',
    name: 'fujian',
    component: () => import('../views/province/FuJian.vue')
  },
  {
    path: '/gansu',
    name: 'gansu',
    component: () => import('../views/province/GanSu.vue')
  },
  {
    path: '/guangdong',
    name: 'guangdong',
    component: () => import('../views/province/GuangDong.vue')
  },
  {
    path: '/guangxi',
    name: 'guangxi',
    component: () => import('../views/province/GuangXi.vue')
  },
  {
    path: '/guizhou',
    name: 'guizhou',
    component: () => import('../views/province/GuiZhou.vue')
  },
  {
    path: '/hainan',
    name: 'hainan',
    component: () => import('../views/province/HaiNan.vue')
  },
  {
    path: '/hebei',
    name: 'hebei',
    component: () => import('../views/province/HeBei.vue')
  },
  {
    path: '/heilongjing',
    name: 'heilongjiang',
    component: () => import('../views/province/HeiLongJiang.vue')
  },
  {
    path: '/henan',
    name: 'hunan',
    component: () => import('../views/province/HeNan.vue')
  },
  {
    path: '/hubei',
    name: 'hubei',
    component: () => import('../views/province/HuBei.vue')
  },
  {
    path: '/hunan',
    name: 'hunan',
    component: () => import('../views/province/HuNan.vue')
  },
  {
    path: '/jiangsu',
    name: 'jiangsu',
    component: () => import('../views/province/JiangSu.vue')
  },
  {
    path: '/jiangxi',
    name: 'jiangxi',
    component: () => import('../views/province/JiangXi.vue')
  },
  {
    path: '/jilin',
    name: 'jilin',
    component: () => import('../views/province/JiLin.vue')
  },
  {
    path: '/liaoning',
    name: 'liaoning',
    component: () => import('../views/province/LiaoNing.vue')
  },
  {
    path: '/neimeng',
    name: 'neimeng',
    component: () => import('../views/province/NeiMeng.vue')
  },
  {
    path: '/ningxia',
    name: 'ningxia',
    component: () => import('../views/province/NingXia.vue')
  },
  {
    path: '/qinghai',
    name: 'qinghai',
    component: () => import('../views/province/QingHai.vue')
  },
  {
    path: '/shandong',
    name: 'shandong',
    component: () => import('../views/province/ShanDong.vue')
  },
  {
    path: '/shanghai',
    name: 'shanghai',
    component: () => import('../views/province/ShangHai.vue')
  },
  {
    path: '/shanxi',
    name: 'shanxi',
    component: () => import('../views/province/ShanXi.vue')
  },
  {
    path: '/sichuan',
    name: 'sichuan',
    component: () => import('../views/province/SiChuan.vue')
  },
  {
    path: '/tianjin',
    name: 'tianjin',
    component: () => import('../views/province/TianJin.vue')
  },
  {
    path: '/xian',
    name: 'xian',
    component: () => import('../views/province/XiAn.vue')
  },
  {
    path: '/xinjiang',
    name: 'xinjiang',
    component: () => import('../views/province/XinJiang.vue')
  },
  {
    path: '/xizang',
    name: 'xizang',
    component: () => import('../views/province/XiZang.vue')
  },
  {
    path: '/yunnan',
    name: 'yunnan',
    component: () => import('../views/province/YunNan.vue')
  },
  {
    path: '/zhejiang',
    name: 'zhejiang',
    component: () => import('../views/province/ZheJiang.vue')
  },
  //end
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
