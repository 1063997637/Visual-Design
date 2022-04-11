"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
     path('index/', views.index ),
    # path('shuiziyuan/',views.shuiziyuan ),
    # path('gongyongshui/',views.gongyongshui ),
    # path('yunshuluxian/',views.yunshuluxian ),
    # path('huoyun/',views.huoyun),
    # path('keyun/',views.keyun),
    # path('senlinziyuan/',views.senlinziyuan),
    # path('zaolinmianji/',views.zaolinmianji),
    # path('yousefeijinshu/',views.yousefeijinshu),
    # path('heisenengyuan/',views.heisenengyuan),
    # path('aa/',views.lsdwmjcl),

    # Output_of_agricultural_products 主要农作物产量
    path('ooap/lscl', views.ooap_lscl),
    path('ooap/xlcl', views.ooap_xlcl),
    path('ooap/qlcl', views.ooap_qlcl),
    path('ooap/dgcl', views.ooap_dgcl),
    path('ooap/xmcl', views.ooap_xmcl),
    path('ooap/ymcl', views.ooap_ymcl),
    path('ooap/gzcl', views.ooap_gzcl),
    path('ooap/glcl', views.ooap_glcl),
    path('ooap/qtgwcl', views.ooap_qtgwcl),
    path('ooap/ldcl', views.ooap_ldcl),
    path('ooap/hxdcl', views.ooap_hxdcl),
    path('ooap/ddcl', views.ooap_ddcl),
    path('ooap/mlscl', views.ooap_mlscl),
    path('ooap/mhcl', views.ooap_mhcl),
    path('ooap/hscl', views.ooap_hscl),
    path('ooap/yczcl', views.ooap_yczcl),
    path('ooap/sccl', views.ooap_sccl),


    # Crop_area  主要农作物播种面积
    path('ca/nzwzmj2020',views.ca_nzwzmj2020),
    path('ca/nzwzmj2019',views.ca_nzwzmj2019),
    path('ca/nzwzmj2018',views.ca_nzwzmj2018),
    path('ca/nzwzmj2017',views.ca_nzwzmj2017),
    path('ca/nzwzmj2016',views.ca_nzwzmj2016),
    path('ca/lsmj', views.ca_lsmj),
    path('ca/xlmj', views.ca_xlmj),
    path('ca/qlmj', views.ca_qlmj),
    path('ca/dgmj', views.ca_dgmj),
    path('ca/xmmj', views.ca_xmmj),
    path('ca/ymmj', views.ca_ymmj),
    path('ca/gzmj', views.ca_gzmj),
    path('ca/glmj', views.ca_glmj),
    path('ca/qtgwmj', views.ca_qtgwmj),
    path('ca/ldmj', views.ca_ldmj),
    path('ca/hxdmj', views.ca_hxdmj),
    path('ca/ddmj', views.ca_ddmj),
    path('ca/mlsmj', views.ca_mlsmj),
    path('ca/mhmj', views.ca_mhmj),
    path('ca/hsmj', views.ca_hsmj),
    path('ca/yczmj', views.ca_yczmj),
    path('ca/scmj', views.ca_scmj),

    path('oofp/mccl', views.oofp_mccl),
    path('oofp/xjcl', views.oofp_xjcl),
    path('oofp/szcl', views.oofp_szcl),
    path('oofp/sqcl', views.oofp_sqcl),
    path('oofp/ytzcl', views.oofp_ytzcl),
    path('oofp/cyzcl', views.oofp_cyzcl),
    path('oofp/wjzcl', views.oofp_wjzcl),
    path('oofp/wbzcl', views.oofp_wbzcl),
    path('oofp/zpcl', views.oofp_zpcl),
    path('oofp/zspcl', views.oofp_zspcl),
    path('oofp/zjcl', views.oofp_zjcl),

    path('ec/yxggmj2016', views.ec_yxggl2016),
    path('ec/yxggmj2017', views.ec_yxggl2017),
    path('ec/yxggmj2018', views.ec_yxggl2018),
    path('ec/yxggmj2019', views.ec_yxggl2019),
    path('ec/yxggmj2020', views.ec_yxggl2020),
    path('ec/nyhf2016', views.ec_nyhfsyzcl2016),
    path('ec/nyhf2017', views.ec_nyhfsyzcl2017),
    path('ec/nyhf2018', views.ec_nyhfsyzcl2018),
    path('ec/nyhf2019', views.ec_nyhfsyzcl2019),
    path('ec/nyhf2020', views.ec_nyhfsyzcl2020),
    path('ec/ncydl2016', views.ec_ncydl2016),
    path('ec/ncydl2017', views.ec_ncydl2017),
    path('ec/ncydl2018', views.ec_ncydl2018),
    path('ec/ncydl2019', views.ec_ncydl2019),
    path('ec/ncydl2020', views.ec_ncydl2020),

    path('ooap1/scpzcl', views.ooap1_scpzcl),
    path('ooap1/blcl', views.ooap1_blcl),
    path('ooap1/yzcl', views.ooap1_yzcl),
    path('ooap1/ylcl', views.ooap1_ylcl),
    path('ooap1/xxlcl', views.ooap1_xxlcl),
    path('ooap1/blcl', views.ooap1_blcl),
    path('ooap1/zlcl', views.ooap1_zlcl),
    path('ooap1/hscpcl', views.ooap1_hscpcl),
    path('ooap1/dscpcl', views.ooap1_dscpcl),

    path('lo/zclsl', views.lo_zclsl),
    path('lo/nclsl', views.lo_nclsl),
    path('lo/yclsl', views.lo_yclsl),
    path('lo/jqcll', views.lo_jqcll),

    path('lr/dscndts', views.lr_dscndts),
    path('lr/nqmsl', views.lr_nqmsl),
    path('lr/mqmsl', views.lr_mqmsl),
    path('lr/lqmsl', views.lr_lqmsl),
    path('lr/luoqmsl', views.lr_luoqmsl),
    path('lr/zndts', views.lr_zndts),
    path('lr/yndzs', views.lr_yndzs),

    path('oolp/rlcl', views.oolp_rlcl),
    path('oolp/zrcl', views.oolp_zrcl),
    path('oolp/nrcl', views.oolp_nrcl),
    path('oolp/yrcl', views.oolp_yrcl),
    path('oolp/nncl', views.oolp_nncl),
    path('oolp/qdcl', views.oolp_qdcl),
    path('oolp/fmcl', views.oolp_fmcl),

    path('tafy/sgcl', views.tafy_sgcl),












]
