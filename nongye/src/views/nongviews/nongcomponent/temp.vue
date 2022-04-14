<template>
  <div class="content-body">
    <!-- <div class="title">水资源各省分布情况</div> -->
    <div id="main1" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";
export default {
  //数据项:省份，年份，水资源
  //水资源总量,地表水资源量，地下水资源量，地表水与地下水资源重复量(亿立方米)
  //人均水资源量(立方米/人)
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
  methods: {
    initCharts(Dom) {
      var myChart = echarts.init(Dom);
      //配置数据
const colors = ['#FFAE57', '#FF7853', '#EA5151', '#CC3F57', '#9A2555'];
const bgColor = '#2E2733';
const itemStyle = {
  star5: {
    color: colors[0]
  },
  star4: {
    color: colors[1]
  },
  star3: {
    color: colors[2]
  },
  star2: {
    color: colors[3]
  }
};
const data = [
  {
    name: '虚构',
    itemStyle: {
      color: colors[1]
    },
    children: [
      {
        name: '小说',
        children: [
          {
            name: '5☆',
            children: [
              {
                name: '疼'
              },
              {
                name: '慈悲'
              },
              {
                name: '楼下的房客'
              }
            ]
          },
          {
            name: '4☆',
            children: [
              {
                name: '虚无的十字架'
              },
              {
                name: '无声告白'
              },
              {
                name: '童年的终结'
              }
            ]
          },
          {
            name: '3☆',
            children: [
              {
                name: '疯癫老人日记'
              }
            ]
          }
        ]
      },
      {
        name: '其他',
        children: [
          {
            name: '5☆',
            children: [
              {
                name: '纳博科夫短篇小说全集'
              }
            ]
          },
          {
            name: '4☆',
            children: [
              {
                name: '安魂曲'
              },
              {
                name: '人生拼图版'
              }
            ]
          },
          {
            name: '3☆',
            children: [
              {
                name: '比起爱你，我更需要你'
              }
            ]
          }
        ]
      }
    ]
  },
  {
    name: '非虚构',
    itemStyle: {
      color: colors[2]
    },
    children: [
      {
        name: '设计',
        children: [
          {
            name: '5☆',
            children: [
              {
                name: '无界面交互'
              }
            ]
          },
          {
            name: '4☆',
            children: [
              {
                name: '数字绘图的光照与渲染技术'
              },
              {
                name: '日本建筑解剖书'
              }
            ]
          },
          {
            name: '3☆',
            children: [
              {
                name: '奇幻世界艺术\n&RPG地图绘制讲座'
              }
            ]
          }
        ]
      },
      {
        name: '社科',
        children: [
          {
            name: '5☆',
            children: [
              {
                name: '痛点'
              }
            ]
          },
          {
            name: '4☆',
            children: [
              {
                name: '卓有成效的管理者'
              },
              {
                name: '进化'
              },
              {
                name: '后物欲时代的来临'
              }
            ]
          },
          {
            name: '3☆',
            children: [
              {
                name: '疯癫与文明'
              }
            ]
          }
        ]
      },
      {
        name: '心理',
        children: [
          {
            name: '5☆',
            children: [
              {
                name: '我们时代的神经症人格'
              }
            ]
          },
          {
            name: '4☆',
            children: [
              {
                name: '皮格马利翁效应'
              },
              {
                name: '受伤的人'
              }
            ]
          },
          {
            name: '3☆'
          },
          {
            name: '2☆',
            children: [
              {
                name: '迷恋'
              }
            ]
          }
        ]
      },
      {
        name: '居家',
        children: [
          {
            name: '4☆',
            children: [
              {
                name: '把房子住成家'
              },
              {
                name: '只过必要生活'
              },
              {
                name: '北欧简约风格'
              }
            ]
          }
        ]
      },
      {
        name: '绘本',
        children: [
          {
            name: '5☆',
            children: [
              {
                name: '设计诗'
              }
            ]
          },
          {
            name: '4☆',
            children: [
              {
                name: '假如生活糊弄了你'
              },
              {
                name: '博物学家的神秘动物图鉴'
              }
            ]
          },
          {
            name: '3☆',
            children: [
              {
                name: '方向'
              }
            ]
          }
        ]
      },
      {
        name: '哲学',
        children: [
          {
            name: '4☆',
            children: [
              {
                name: '人生的智慧'
              }
            ]
          }
        ]
      },
      {
        name: '技术',
        children: [
          {
            name: '5☆',
            children: [
              {
                name: '代码整洁之道'
              }
            ]
          },
          {
            name: '4☆',
            children: [
              {
                name: 'Three.js 开发指南'
              }
            ]
          }
        ]
      }
    ]
  }
];
for (let j = 0; j < data.length; ++j) {
  let level1 = data[j].children;
  for (let i = 0; i < level1.length; ++i) {
    let block = level1[i].children;
    let bookScore = [];
    let bookScoreId;
    for (let star = 0; star < block.length; ++star) {
      let style = (function (name) {
        switch (name) {
          case '5☆':
            bookScoreId = 0;
            return itemStyle.star5;
          case '4☆':
            bookScoreId = 1;
            return itemStyle.star4;
          case '3☆':
            bookScoreId = 2;
            return itemStyle.star3;
          case '2☆':
            bookScoreId = 3;
            return itemStyle.star2;
        }
      })(block[star].name);
      block[star].label = {
        color: style.color,
        downplay: {
          opacity: 0.5
        }
      };
      if (block[star].children) {
        style = {
          opacity: 1,
          color: style.color
        };
        block[star].children.forEach(function (book) {
          book.value = 1;
          book.itemStyle = style;
          book.label = {
            color: style.color
          };
          let value = 1;
          if (bookScoreId === 0 || bookScoreId === 3) {
            value = 5;
          }
          if (bookScore[bookScoreId]) {
            bookScore[bookScoreId].value += value;
          } else {
            bookScore[bookScoreId] = {
              color: colors[bookScoreId],
              value: value
            };
          }
        });
      }
    }
    level1[i].itemStyle = {
      color: data[j].itemStyle.color
    };
  }
}
var option = {
  backgroundColor: "",
  color: colors,
  series: [
    {
      type: 'sunburst',
      center: ['50%', '48%'],
      data: data,
      sort: function (a, b) {
        if (a.depth === 1) {
          return b.getValue() - a.getValue();
        } else {
          return a.dataIndex - b.dataIndex;
        }
      },
      label: {
        rotate: 'radial',
        color: bgColor
      },
      itemStyle: {
        borderColor: bgColor,
        borderWidth: 2
      },
      levels: [
        {},
        {
          r0: 0,
          r: 40,
          label: {
            rotate: 0
          }
        },
        {
          r0: 40,
          r: 105
        },
        {
          r0: 115,
          r: 140,
          itemStyle: {
            shadowBlur: 2,
            shadowColor: colors[2],
            color: 'transparent'
          },
          label: {
            rotate: 'tangential',
            fontSize: 10,
            color: colors[0]
          }
        },
        {
          r0: 140,
          r: 145,
          itemStyle: {
            shadowBlur: 80,
            shadowColor: colors[0]
          },
          label: {
            position: 'outside',
            textShadowBlur: 5,
            textShadowColor: '#333'
          },
          downplay: {
            label: {
              opacity: 0.5
            }
          }
        }
      ]
    }
  ]
};
      myChart.setOption(option, true);
    },
  },
  mounted() {
    this.initCharts(document.getElementById("main1"));
  },
};
</script>

<style>
.content-body {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  position: relative;
}
</style>