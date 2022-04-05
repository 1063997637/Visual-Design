import json

import json


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import app01.models

from django.http import HttpResponse
from django.core import serializers
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

    # all_water = models.water_resource.objects.filter(年份 = '2020' ) #最近年份
    #
    # all_water_data = [{'省份','水资源总量(亿立方米)','地表水资源量(亿立方米)','地下水资源量(亿立方米)','地表水与地下水资源重复量(亿立方米)','人均水资源量(立方米 / 人)'}]

    # list_dict = all_water.values()
    # print(all_water)
    # for obj in all_water:
    #     print(obj.id,obj.省份 ,obj.人均水资源量_立方米_人_field,obj.地下水资源量_亿立方米_field)
        # print(obj.value)

    # print(list_dict)    #111
    # ret_list = list(list_dict)
    # return HttpResponse(ret_list, safe=False)

    # data = serializers.serialize("json", all_water,ensure_ascii=False)
    # return HttpResponse(data, content_type='application/json; charset=utf-8')

    # return HttpResponse("hunan ziyuan data")

# 供用水情况
def gongyongshui(request):
    year = models.water_supply.objects.values().filter(供水总量_亿立方米_field__isnull=False).first().get('年份')
    # a = models.water_supply.objects.first()
    # print(year)
    gysqk = models.water_supply.objects.filter(年份=year)
    data = serializers.serialize("json", gysqk, ensure_ascii=False)
    return HttpResponse(data, content_type='application/json; charset=utf-8')

# 运输线路长度
def yunshuluxian(request):
    year = models.transportation_route.objects.values().filter(内河航道里程_万公里_field__isnull = False).first().get('年份')
    ysxlcd = models.transportation_route.objects.filter(年份=year)
    data = serializers.serialize("json", ysxlcd, ensure_ascii=False)
    return HttpResponse(data, content_type='application/json; charset=utf-8')


# 货运量
def huoyun(request):
    year = models.freight_transport.objects.values().filter(货运量_万吨_field__isnull=False).first().get('年份')
    hyl = models.freight_transport.objects.filter(年份=year)
    data = serializers.serialize("json", hyl, ensure_ascii=False)
    return HttpResponse(data, content_type='application/json; charset=utf-8')

# 客运量
def keyun(request):
    year = models.passenger_volume.objects.values().filter(客运量_万人_field__isnull=False).first().get('年份')
    kyl = models.passenger_volume.objects.filter(年份=year)
    data = serializers.serialize("json", kyl, ensure_ascii=False)
    return HttpResponse(data, content_type='application/json; charset=utf-8')

# 森林资源
def senlinziyuan(request):
    year = models.forest_resources.objects.values().filter(林业用地面积_万公顷_field__isnull=False).first().get('年份')
    slzy = models.forest_resources.objects.filter(年份=year)
    data = serializers.serialize("json", slzy, ensure_ascii=False)
    return HttpResponse(data, content_type='application/json; charset=utf-8')

# 造林面积

def zaolinmianji(request):
    year = models.afforestation_area.objects.values().filter(造林总面积_千公顷_field__isnull=False).first().get('年份')
    zlmj = models.afforestation_area.objects.filter(年份=year)
    data = serializers.serialize("json", zlmj, ensure_ascii=False)
    return HttpResponse(data, content_type='application/json; charset=utf-8')

# 有色金属非金属
def yousefeijinshu(request):
    year = models.non_ferrous_metals.objects.values().filter(铜矿储量_万吨_field__isnull=False).first().get('年份')
    ysjs = models.non_ferrous_metals.objects.filter(年份=year)
    data = serializers.serialize("json", ysjs, ensure_ascii=False)
    return HttpResponse(data, content_type='application/json; charset=utf-8')



# 黑色金属能源
def heisenengyuan(request):
    year = models.Main_energy_ferrous_metal.objects.values().filter(石油储量_万吨_field__isnull=False).first().get('年份')
    hsjs = models.Main_energy_ferrous_metal.objects.filter(年份=year)
    data = serializers.serialize("json", hsjs, ensure_ascii=False)
    return HttpResponse(data, content_type='application/json; charset=utf-8')







