import json
import time

from django.core import serializers
from django.core.serializers import serialize
from django.forms import model_to_dict
# from django.http import HttpResponse, JsonResponse
# from rest_framework import serializers
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import APIView

# Create your views here.
from app01 import models


# python manage.py runserver 192.168.123.8:8000

def index(request):
    return HttpResponse("Welcome!!")


# 水资源
def shuiziyuan(request):
    year = models.water_resource.objects.values().filter(水资源总量_亿立方米_field__isnull=False).first().get('年份')
    szy = models.water_resource.objects.filter(年份=year)
    data = serializers.serialize("json", szy, ensure_ascii=False)
    return HttpResponse(data, content_type='application/json; charset=utf-8')

# # 供用水情况
# def gongyongshui(request):
#     year = models.water_supply.objects.values().filter(供水总量_亿立方米_field__isnull=False).first().get('年份')
#     # a = models.water_supply.objects.first()
#     # print(year)
#     gysqk = models.water_supply.objects.filter(年份=year)
#     data = serializers.serialize("json", gysqk, ensure_ascii=False)
#     return HttpResponse(data, content_type='application/json; charset=utf-8')



def ooap_lscl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(粮食产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '粮食产量_万吨_field')
    # data = model.filter(年份=year).all()
    # data = serializers.serialize("json", data, ensure_ascii=False)
    data = list(data)

    # print(type(data))

    # json_list = []
    # for good in data:
    #     json_dict = model_to_dict(good)
    #     json_list.append(json_dict)
    #
    # print(json_list)

    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_xlcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(夏收粮食产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '夏收粮食产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    # return HttpResponse(data, content_type='application/json; charset=utf-8')


def ooap_qlcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(秋粮产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '秋粮产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_dgcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(稻谷产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '稻谷产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_xmcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(小麦产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '小麦产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_ymcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(玉米产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '玉米产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_gzcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(谷子产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '谷子产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_glcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(高粱产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '高粱产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_qtgwcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(其他谷物产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '其他谷物产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_ldcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(绿豆产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '绿豆产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_hxdcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(红小豆产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '红小豆产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_ddcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(大豆产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '大豆产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_mlscl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(马铃薯产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '马铃薯产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_mhcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(棉花产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '棉花产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_hscl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(花生产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '花生产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_yczcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(油菜籽产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '油菜籽产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap_sccl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(蔬菜产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '蔬菜产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_nzwzmj2020(request):
    model = models.Crop_area.objects
    # year = model.values().filter(粮食单位面积产量_公斤_公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份='2020').values('省份', '年份', '农作物总播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_nzwzmj2019(request):
    model = models.Crop_area.objects
    # year = model.values().filter(粮食单位面积产量_公斤_公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份='2019').values('省份', '年份', '农作物总播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_nzwzmj2018(request):
    model = models.Crop_area.objects
    # year = model.values().filter(粮食单位面积产量_公斤_公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份='2018').values('省份', '年份', '农作物总播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_nzwzmj2017(request):
    model = models.Crop_area.objects
    # year = model.values().filter(粮食单位面积产量_公斤_公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份='2017').values('省份', '年份', '农作物总播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_nzwzmj2016(request):
    model = models.Crop_area.objects
    # year = model.values().filter(粮食单位面积产量_公斤_公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份='2016').values('省份', '年份', '农作物总播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_lsmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(粮食作物播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '粮食作物播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_xlmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(夏收粮食播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '夏收粮食播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_qlmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(秋收粮食播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '秋收粮食播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_dgmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(稻谷播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '稻谷播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_xmmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(小麦播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '小麦播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_ymmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(玉米播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '玉米播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_gzmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(谷子播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '谷子播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_glmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(高粱播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '高粱播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_qtgwmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(其他谷物播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '其他谷物播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_ldmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(绿豆播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '绿豆播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_hxdmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(红小豆播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '红小豆播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_ddmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(大豆播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '大豆播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_mlsmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(马铃薯播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '马铃薯播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_mhmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(棉花播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '棉花播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_hsmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(花生播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '花生播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_yczmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(油菜籽播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '油菜籽播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ca_scmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(蔬菜播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '蔬菜播种面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oofp_mccl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(木材产量_万立方米_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '木材产量_万立方米_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oofp_xjcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(橡胶产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '橡胶产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oofp_szcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(松脂产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '松脂产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oofp_sqcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(生漆产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '生漆产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oofp_ytzcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(油桐籽产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '油桐籽产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oofp_cyzcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(油茶籽产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '油茶籽产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oofp_wjzcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(乌桕籽产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '乌桕籽产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oofp_wbzcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(五倍籽产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '五倍籽产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oofp_zpcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(棕片产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '棕片产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oofp_zspcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(竹笋片产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '竹笋片产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oofp_zjcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(紫胶产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '紫胶产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_yxggl2016(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(有效灌溉面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=2016).values('省份', '年份', '有效灌溉面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_yxggl2017(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(有效灌溉面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=2017).values('省份', '年份', '有效灌溉面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_yxggl2018(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(有效灌溉面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=2018).values('省份', '年份', '有效灌溉面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_yxggl2019(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(有效灌溉面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=2019).values('省份', '年份', '有效灌溉面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_yxggl2020(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(有效灌溉面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=2020).values('省份', '年份', '有效灌溉面积_千公顷_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_nyhfsyzcl2016(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农用化肥施用折纯量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=2016).values('省份', '年份', '农用化肥施用折纯量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_nyhfsyzcl2017(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农用化肥施用折纯量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=2017).values('省份', '年份', '农用化肥施用折纯量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_nyhfsyzcl2018(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农用化肥施用折纯量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=2018).values('省份', '年份', '农用化肥施用折纯量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_nyhfsyzcl2019(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农用化肥施用折纯量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=2019).values('省份', '年份', '农用化肥施用折纯量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_nyhfsyzcl2020(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农用化肥施用折纯量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=2020).values('省份', '年份', '农用化肥施用折纯量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_ncydl2016(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农村用电量_亿千瓦小时_field__isnull=False).first().get('年份')
    data = model.filter(年份=2016).values('省份', '年份', '农村用电量_亿千瓦小时_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_ncydl2017(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农村用电量_亿千瓦小时_field__isnull=False).first().get('年份')
    data = model.filter(年份=2017).values('省份', '年份', '农村用电量_亿千瓦小时_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_ncydl2018(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农村用电量_亿千瓦小时_field__isnull=False).first().get('年份')
    data = model.filter(年份=2018).values('省份', '年份', '农村用电量_亿千瓦小时_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_ncydl2019(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农村用电量_亿千瓦小时_field__isnull=False).first().get('年份')
    data = model.filter(年份=2019).values('省份', '年份', '农村用电量_亿千瓦小时_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ec_ncydl2020(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农村用电量_亿千瓦小时_field__isnull=False).first().get('年份')
    data = model.filter(年份=2020).values('省份', '年份', '农村用电量_亿千瓦小时_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap1_scpzcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(水产品总产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '水产品总产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap1_blcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(捕捞产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '捕捞产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap1_yzcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(养殖产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '养殖产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap1_ylcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(鱼类产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '鱼类产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap1_xxlcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(虾蟹类产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '虾蟹类产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap1_blcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(贝类产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '贝类产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap1_zlcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(藻类产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '藻类产量_吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap1_hscpcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(海水产品产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '海水产品产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def ooap1_dscpcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(淡水产品产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '淡水产品产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def lo_zclsl(request):
    model = models.Livestock_output.objects
    year = model.values().filter(猪出栏数量_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '猪出栏数量_万头_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def lo_nclsl(request):
    model = models.Livestock_output.objects
    year = model.values().filter(牛出栏数量_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '牛出栏数量_万头_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def lo_yclsl(request):
    model = models.Livestock_output.objects
    year = model.values().filter(羊出栏数量_万只_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '羊出栏数量_万只_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def lo_jqcll(request):
    model = models.Livestock_output.objects
    year = model.values().filter(家禽出栏量_万只_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '家禽出栏量_万只_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def lr_dscndts(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(大牲畜年底头数_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '大牲畜年底头数_万头_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def lr_nqmsl(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(牛期末数量_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '牛期末数量_万头_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def lr_mqmsl(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(马期末数量_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '马期末数量_万头_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def lr_lqmsl(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(驴期末数量_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '驴期末数量_万头_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def lr_luoqmsl(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(骡期末数量_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '骡期末数量_万头_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def lr_zndts(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(猪年底头数_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '猪年底头数_万头_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def lr_yndzs(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(羊年底只数_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '羊年底只数_万头_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oolp_rlcl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(肉类产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '肉类产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oolp_zrcl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(猪肉产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '猪肉产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oolp_nrcl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(牛肉产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '牛肉产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oolp_yrcl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(羊肉产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '羊肉产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oolp_nncl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(牛奶产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '牛奶产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oolp_qdcl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(禽蛋产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '禽蛋产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def oolp_fmcl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(蜂蜜产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '蜂蜜产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def tafy_sgcl(request):
    model = models.Tea_and_fruit_yield.objects
    year = model.values().filter(水果产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '水果产量_万吨_field')
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})



class price(APIView):

    def get(self, request):
        model = models.Price.objects
        id = request.GET.get("id")
        data = model.filter(id=id).values('class_field', 'variety','unit','p20_7','p20_9','p21_1','p21_3','p21_5','p21_7','p21_9','p21_11','p22_1','p22_3','p22_5','yc')
        data = list(data)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})



# 手动爬取  农业要闻 第一页的内容
def spider_nyyw(request):
    nyyw_run()
    return HttpResponse('农业要闻更新成功！！')


def spider_hnnyyw(request):
    hnnyyw_run()
    return HttpResponse('湖南农业要闻更新成功！！')


def nyyw_title(request):
    model = models.Nyyw.objects
    data = model.values('id', 'title', 'date')
    # print(data[0])
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})




class nyyw_body(APIView):

    def get(self, request):
        model = models.Nyyw.objects
        id = request.GET.get("id")
        data = model.filter(id=id).values("title", "daa", "herf", "picherf", "body")
        data = list(data)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def hnnyyw_title(request):
    model = models.Hnnyyw.objects
    data = model.values('id', 'title', 'date')
    # print(data[0])
    data = list(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


class hnnyyw_body(APIView):

    def get(self, request):
        model = models.Hnnyyw.objects
        id = request.GET.get("id")
        data = model.filter(id=id).values("title", "daa", "herf", "picherf", "body")
        data = list(data)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


# 自动爬取 农业要闻第一页的数据
def nyyw_run():
    import re
    import unicodedata

    from bs4 import BeautifulSoup
    import requests

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
        'Connection': 'close'}
    url = 'http://www.agri.cn/V20/ZX/nyyw/'
    res = requests.get(url, headers=headers, verify=False)  # 新闻的网址
    res.encoding = res.apparent_encoding
    # 根据网站的编码方式修改解码方式，因为网页的文字编码方式多种多样有UTF-8 GBK这些解码方式如果不一致容易发生乱码，所以解码方式最好不要统一，而是交给网页自己来决定
    soup = BeautifulSoup(res.text, 'html.parser')

    rates = soup.select('.bj_3-2')
    rates1 = soup.select('.hui_14')

    aa = []
    for data in rates:
        # print(type(data))
        # bb = {}
        temp = re.findall(r'\(.+\)', unicodedata.normalize('NFKC', str(data)), re.S)  # 多行匹配 ， 去除Unicode的空格
        title = re.findall(r'\>(.+)\<', str(temp))
        herf = re.findall((r'\.\/(.+)\"'), str(temp))
        url1 = url + herf[0]
        url2 = url + herf[0].split('/')[0]
        url3 = ""

        # 爬取新闻体
        headers1 = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36',
            'Connection': 'close'
        }
        res1 = requests.get(url1, headers=headers1, verify=False)
        res1.encoding = res1.apparent_encoding
        soup1 = BeautifulSoup(res1.text, 'html.parser')
        res1.close()
        time.sleep(0.05)

        rates2 = soup1.select('.hui_12-12')
        rates3 = soup1.select('.TRS_Editor')

        daa = re.findall(r'\>(.+)\<', unicodedata.normalize('NFKC', str(rates2)))  # date and author
        body = re.findall(r'\[(.+)\]', unicodedata.normalize('NFKC', str(rates3)), re.S)

        picherf = re.findall(r'src\=\"(.+?)\" src\=\"', unicodedata.normalize('NFKC', str(body)))

        for i in picherf:
            url3 = url3 + url2 + "/" + i + " "

        body1 = body[0]
        body1 = body1.replace("\"", "\'")
        body1 = body1.replace("\n", "")
        # print(body1)
        url1 = url1.replace("http://", "")
        url3 = url3.replace("http://", "")
        daa = daa[0].replace(":", "：")
        bb = {'id': 0, 'title': title[0], 'herf': url1, 'date': 0, 'daa': daa, 'body': body1, 'picherf': url3}
        # print(type(body[0]))
        aa.append(bb)

    i = 0
    for data in rates1:
        date = re.findall(r'\((.+)\)', str(data))
        # print(str(date))
        aa[i]['date'] = date[0]
        aa[i]['id'] = i + 1
        # models.Nyyw.objects.bulk_create(aa)
        i += 1

    # 删除 重新创建数据表
    models.Nyyw.objects.all().delete()
    batch = [models.Nyyw(id=row['id'], title=row['title'], herf=row['herf'], date=row['date'], daa=row['daa'],
                         body=row['body'], picherf=row['picherf']) for row in aa]
    models.Nyyw.objects.bulk_create(batch)

    # 更新数据表
    # i = 1
    # for row in aa:
    #     models.Nyyw.objects.filter(id=i).update(title=row['title'], herf=row['herf'], daa=row['daa'], date=row['date'],
    #                                             body=row['body'],
    #                                             picherf=row['picherf'])
    #     i += 1


def hnnyyw_run():
    import json
    import re
    import unicodedata

    from bs4 import BeautifulSoup
    import requests
    from lxml import etree

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36'}
    url = 'http://www.agri.cn/province/hunan/dsxxlb/'  # http://www.agri.cn/V20/ZX/nyyw/
    res = requests.get(url, headers=headers)  # 新闻的网址
    res.encoding = res.apparent_encoding
    # 根据网站的编码方式修改解码方式，因为网页的文字编码方式多种多样有UTF-8 GBK这些解码方式如果不一致容易发生乱码，所以解码方式最好不要统一，而是交给网页自己来决定
    soup = BeautifulSoup(res.text, 'html.parser')

    rates = soup.select('.lb_m12 li')
    rates1 = soup.select('li')
    # bJson = json.dumps(rates, ensure_ascii=False)

    aa = []
    p = 0
    for data in rates:
        # print(type(data))
        # bb = {}
        # temp = re.findall(r'li><.+</li>', unicodedata.normalize('NFKC', str(data)), re.S)  # 多行匹配 ， 去除Unicode的空格
        title = re.findall(r'title\=\"(.+)\"', unicodedata.normalize('NFKC', str(data)), re.S)
        herf = re.findall((r'href\=\"\.\/(.+)\" title'), unicodedata.normalize('NFKC', str(data)), re.S)
        date = re.findall((r'span\>\((.+)\)'), unicodedata.normalize('NFKC', str(data)), re.S)
        url1 = url + herf[0]  # 新闻的url

        url3 = ""
        # print(url1)
        # 爬取新闻体
        headers1 = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36'}
        res1 = requests.get(url1, headers=headers1)
        res1.encoding = res1.apparent_encoding
        soup1 = BeautifulSoup(res1.text, 'html.parser')

        rates2 = soup1.select('.nr_m12')
        rates3 = soup1.select('.nr_m16')

        daahtml = soup1.select('.nr_m15')
        daa = re.findall(r'\<span\>(.+)\<\/span', unicodedata.normalize('NFKC', str(daahtml)))  # date and author

        daa[0] = daa[0].replace('</span><span>', ' ')
        picherf = re.findall(r'src\=\"(.+?)\" src\=\"', unicodedata.normalize('NFKC', str()))
        for i in picherf:
            url3 = url3 + url1 + "/" + i + " "
        body1 = str(rates3[0])
        # print(body1)
        daa = daa[0].replace(":", "：")
        # url1 = url1.replace("//", "/")
        # print(date[0])
        p = p + 1
        bb = {'id': p, 'title': title[0], 'herf': url1, 'date': date[0], 'daa': daa, 'body': body1, 'picherf': url3}
        # print(type(body[0]))
        aa.append(bb)
        # print(date)
    # print(aa[2]["id"])
    models.Hnnyyw.objects.all().delete()
    batch = [models.Hnnyyw(id=row['id'], title=row['title'], herf=row['herf'], date=row['date'], daa=row['daa'],
                           body=row['body'], picherf=row['picherf']) for row in aa]
    models.Hnnyyw.objects.bulk_create(batch)
