# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# 农产品产量
class Output_of_agricultural_products(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    粮食产量_万吨_field = models.FloatField(db_column='粮食产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    夏收粮食产量_万吨_field = models.FloatField(db_column='夏收粮食产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    秋粮产量_万吨_field = models.FloatField(db_column='秋粮产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    谷物产量_万吨_field = models.FloatField(db_column='谷物产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    稻谷产量_万吨_field = models.FloatField(db_column='稻谷产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    早稻产量_万吨_field = models.FloatField(db_column='早稻产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    中稻和一季晚稻产量_万吨_field = models.FloatField(db_column='中稻和一季晚稻产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    双季晚稻产量_万吨_field = models.FloatField(db_column='双季晚稻产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    小麦产量_万吨_field = models.FloatField(db_column='小麦产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    冬小麦产量_万吨_field = models.FloatField(db_column='冬小麦产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    春小麦产量_万吨_field = models.FloatField(db_column='春小麦产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    玉米产量_万吨_field = models.FloatField(db_column='玉米产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    谷子产量_万吨_field = models.FloatField(db_column='谷子产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    高粱产量_万吨_field = models.FloatField(db_column='高粱产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    其他谷物产量_万吨_field = models.FloatField(db_column='其他谷物产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    大麦产量_万吨_field = models.FloatField(db_column='大麦产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    豆类产量_万吨_field = models.FloatField(db_column='豆类产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    绿豆产量_万吨_field = models.FloatField(db_column='绿豆产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    红小豆产量_万吨_field = models.FloatField(db_column='红小豆产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    大豆产量_万吨_field = models.FloatField(db_column='大豆产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    薯类产量_万吨_field = models.FloatField(db_column='薯类产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    马铃薯产量_万吨_field = models.FloatField(db_column='马铃薯产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    棉花产量_万吨_field = models.FloatField(db_column='棉花产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    油料产量_万吨_field = models.FloatField(db_column='油料产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    花生产量_万吨_field = models.FloatField(db_column='花生产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    油菜籽产量_万吨_field = models.FloatField(db_column='油菜籽产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    芝麻产量_万吨_field = models.FloatField(db_column='芝麻产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    葵花籽产量_万吨_field = models.FloatField(db_column='葵花籽产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    胡麻籽产量_万吨_field = models.FloatField(db_column='胡麻籽产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    糖料产量_万吨_field = models.FloatField(db_column='糖料产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    麻类产量_万吨_field = models.FloatField(db_column='麻类产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    黄红麻产量_万吨_field = models.FloatField(db_column='黄红麻产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    亚麻产量_万吨_field = models.FloatField(db_column='亚麻产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    大麻产量_万吨_field = models.FloatField(db_column='大麻产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    苎麻产量_万吨_field = models.FloatField(db_column='苎麻产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    甘蔗产量_万吨_field = models.FloatField(db_column='甘蔗产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    甜菜产量_万吨_field = models.FloatField(db_column='甜菜产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    烟叶产量_万吨_field = models.FloatField(db_column='烟叶产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    烤烟产量_万吨_field = models.FloatField(db_column='烤烟产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    蔬菜产量_万吨_field = models.FloatField(db_column='蔬菜产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '主要农作物产品产量_csv'


class Crop_yield_per_unit_area(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    粮食单位面积产量_公斤_公顷_field = models.FloatField(db_column='粮食单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    夏收粮食单位面积产量_公斤_公顷_field = models.FloatField(db_column='夏收粮食单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    秋粮单位面积产量_公斤_公顷_field = models.FloatField(db_column='秋粮单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    谷物单位面积产量_公斤_公顷_field = models.FloatField(db_column='谷物单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    稻谷单位面积产量_公斤_公顷_field = models.FloatField(db_column='稻谷单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    早稻单位面积产量_公斤_公顷_field = models.FloatField(db_column='早稻单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    中稻和一季晚稻单位面积产量_公斤_公顷_field = models.FloatField(db_column='中稻和一季晚稻单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    双季晚稻单位面积产量_公斤_公顷_field = models.FloatField(db_column='双季晚稻单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    小麦单位面积产量_公斤_公顷_field = models.FloatField(db_column='小麦单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    冬小麦单位面积产量_公斤_公顷_field = models.FloatField(db_column='冬小麦单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    春小麦单位面积产量_公斤_公顷_field = models.FloatField(db_column='春小麦单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    玉米单位面积产量_公斤_公顷_field = models.FloatField(db_column='玉米单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    谷子单位面积产量_公斤_公顷_field = models.FloatField(db_column='谷子单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    高粱单位面积产量_公斤_公顷_field = models.FloatField(db_column='高粱单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    其他谷物单位面积产量_公斤_公顷_field = models.FloatField(db_column='其他谷物单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    大麦单位面积产量_公斤_公顷_field = models.FloatField(db_column='大麦单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    豆类单位面积产量_公斤_公顷_field = models.FloatField(db_column='豆类单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    大豆单位面积产量_公斤_公顷_field = models.FloatField(db_column='大豆单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    绿豆单位面积产量_公斤_公顷_field = models.FloatField(db_column='绿豆单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    红小豆单位面积产量_公斤_公顷_field = models.FloatField(db_column='红小豆单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    薯类单位面积产量_公斤_公顷_field = models.FloatField(db_column='薯类单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    马铃薯单位面积产量_公斤_公顷_field = models.FloatField(db_column='马铃薯单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    棉花单位面积产量_公斤_公顷_field = models.FloatField(db_column='棉花单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    油料单位面积产量_公斤_公顷_field = models.FloatField(db_column='油料单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    花生单位面积产量_公斤_公顷_field = models.FloatField(db_column='花生单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    油菜籽单位面积产量_公斤_公顷_field = models.FloatField(db_column='油菜籽单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    芝麻单位面积产量_公斤_公顷_field = models.FloatField(db_column='芝麻单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    胡麻籽单位面积产量_公斤_公顷_field = models.FloatField(db_column='胡麻籽单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    葵花籽单位面积产量_公斤_公顷_field = models.FloatField(db_column='葵花籽单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    麻类单位面积产量_公斤_公顷_field = models.FloatField(db_column='麻类单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    黄红麻单位面积产量_公斤_公顷_field = models.FloatField(db_column='黄红麻单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    大麻单位面积产量_公斤_公顷_field = models.FloatField(db_column='大麻单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    苎麻单位面积产量_公斤_公顷_field = models.FloatField(db_column='苎麻单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    亚麻单位面积产量_公斤_公顷_field = models.FloatField(db_column='亚麻单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    烟叶单位面积产量_公斤_公顷_field = models.FloatField(db_column='烟叶单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    烤烟单位面积产量_公斤_公顷_field = models.FloatField(db_column='烤烟单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    糖料单位面积产量_公斤_公顷_field = models.FloatField(db_column='糖料单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    甘蔗单位面积产量_公斤_公顷_field = models.FloatField(db_column='甘蔗单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    甜菜单位面积产量_公斤_公顷_field = models.FloatField(db_column='甜菜单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    蔬菜单位面积产量_公斤_公顷_field = models.FloatField(db_column='蔬菜单位面积产量(公斤/公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '主要农作物单位面积产量_csv'


class Crop_area(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    农作物总播种面积_千公顷_field = models.FloatField(db_column='农作物总播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    粮食作物播种面积_千公顷_field = models.FloatField(db_column='粮食作物播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    夏收粮食播种面积_千公顷_field = models.FloatField(db_column='夏收粮食播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    秋收粮食播种面积_千公顷_field = models.FloatField(db_column='秋收粮食播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    谷物播种面积_千公顷_field = models.FloatField(db_column='谷物播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    稻谷播种面积_千公顷_field = models.FloatField(db_column='稻谷播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    早稻播种面积_千公顷_field = models.FloatField(db_column='早稻播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    中稻和一季晚稻播种面积_千公顷_field = models.FloatField(db_column='中稻和一季晚稻播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    双季晚稻播种面积_千公顷_field = models.FloatField(db_column='双季晚稻播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    小麦播种面积_千公顷_field = models.FloatField(db_column='小麦播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    冬小麦播种面积_千公顷_field = models.FloatField(db_column='冬小麦播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    春小麦播种面积_千公顷_field = models.FloatField(db_column='春小麦播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    玉米播种面积_千公顷_field = models.FloatField(db_column='玉米播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    谷子播种面积_千公顷_field = models.FloatField(db_column='谷子播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    高粱播种面积_千公顷_field = models.FloatField(db_column='高粱播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    其他谷物播种面积_千公顷_field = models.FloatField(db_column='其他谷物播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    大麦播种面积_千公顷_field = models.FloatField(db_column='大麦播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    豆类播种面积_千公顷_field = models.FloatField(db_column='豆类播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    大豆播种面积_千公顷_field = models.FloatField(db_column='大豆播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    绿豆播种面积_千公顷_field = models.FloatField(db_column='绿豆播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    红小豆播种面积_千公顷_field = models.FloatField(db_column='红小豆播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    薯类播种面积_千公顷_field = models.FloatField(db_column='薯类播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    马铃薯播种面积_千公顷_field = models.FloatField(db_column='马铃薯播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    油料播种面积_千公顷_field = models.FloatField(db_column='油料播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    花生播种面积_千公顷_field = models.FloatField(db_column='花生播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    油菜籽播种面积_千公顷_field = models.FloatField(db_column='油菜籽播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    芝麻播种面积_千公顷_field = models.FloatField(db_column='芝麻播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    葵花籽播种面积_千公顷_field = models.FloatField(db_column='葵花籽播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    胡麻籽播种面积_千公顷_field = models.FloatField(db_column='胡麻籽播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    棉花播种面积_千公顷_field = models.FloatField(db_column='棉花播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    麻类播种面积_千公顷_field = models.FloatField(db_column='麻类播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    黄红麻播种面积_千公顷_field = models.FloatField(db_column='黄红麻播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    亚麻播种面积_千公顷_field = models.FloatField(db_column='亚麻播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    大麻播种面积_千公顷_field = models.FloatField(db_column='大麻播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    苎麻播种面积_千公顷_field = models.FloatField(db_column='苎麻播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    糖料播种面积_千公顷_field = models.FloatField(db_column='糖料播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    甘蔗播种面积_千公顷_field = models.FloatField(db_column='甘蔗播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    甜菜播种面积_千公顷_field = models.FloatField(db_column='甜菜播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    烟叶播种面积_千公顷_field = models.FloatField(db_column='烟叶播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    烤烟播种面积_千公顷_field = models.FloatField(db_column='烤烟播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    蔬菜播种面积_千公顷_field = models.FloatField(db_column='蔬菜播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    药材播种面积_千公顷_field = models.FloatField(db_column='药材播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    其他农作物播种面积_千公顷_field = models.FloatField(db_column='其他农作物播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    青饲料播种面积_千公顷_field = models.FloatField(db_column='青饲料播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '主要农作物播种面积_csv'


class Output_of_forest_products(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    木材产量_万立方米_field = models.FloatField(db_column='木材产量(万立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    橡胶产量_吨_field = models.FloatField(db_column='橡胶产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    松脂产量_吨_field = models.FloatField(db_column='松脂产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    生漆产量_吨_field = models.FloatField(db_column='生漆产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    油桐籽产量_吨_field = models.FloatField(db_column='油桐籽产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    油茶籽产量_吨_field = models.FloatField(db_column='油茶籽产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    乌桕籽产量_吨_field = models.FloatField(db_column='乌桕籽产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    五倍籽产量_吨_field = models.FloatField(db_column='五倍籽产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    棕片产量_吨_field = models.FloatField(db_column='棕片产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    竹笋片产量_吨_field = models.FloatField(db_column='竹笋片产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    紫胶产量_吨_field = models.FloatField(db_column='紫胶产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '主要林产品产量_csv'


class Added_value(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    农林牧渔业增加值_亿元_field = models.FloatField(db_column='农林牧渔业增加值(亿元)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    农业增加值_亿元_field = models.FloatField(db_column='农业增加值(亿元)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    林业增加值_亿元_field = models.FloatField(db_column='林业增加值(亿元)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    牧业增加值_亿元_field = models.FloatField(db_column='牧业增加值(亿元)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    渔业增加值_亿元_field = models.FloatField(db_column='渔业增加值(亿元)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '农林牧渔业增加值_csv'


class Total_output_value_and_index(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    农林牧渔业总产值_亿元_field = models.FloatField(db_column='农林牧渔业总产值(亿元)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    农业总产值_亿元_field = models.FloatField(db_column='农业总产值(亿元)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    林业总产值_亿元_field = models.FloatField(db_column='林业总产值(亿元)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    牧业总产值_亿元_field = models.FloatField(db_column='牧业总产值(亿元)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    渔业总产值_亿元_field = models.FloatField(db_column='渔业总产值(亿元)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    农林牧渔业总产值指数_百分之_field = models.FloatField(db_column='农林牧渔业总产值指数(百分之)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    农业总产值指数_百分之_field = models.FloatField(db_column='农业总产值指数(百分之)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    林业总产值指数_百分之_field = models.FloatField(db_column='林业总产值指数(百分之)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    牧业总产值指数_百分之_field = models.FloatField(db_column='牧业总产值指数(百分之)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    渔业总产值指数_百分之_field = models.FloatField(db_column='渔业总产值指数(百分之)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '农林牧渔业总产值及指数_csv'


class Electricity_consumption(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    有效灌溉面积_千公顷_field = models.FloatField(db_column='有效灌溉面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    农用化肥施用折纯量_万吨_field = models.FloatField(db_column='农用化肥施用折纯量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    农用氮肥施用折纯量_万吨_field = models.FloatField(db_column='农用氮肥施用折纯量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    农用磷肥施用折纯量_万吨_field = models.FloatField(db_column='农用磷肥施用折纯量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    农用钾肥施用折纯量_万吨_field = models.FloatField(db_column='农用钾肥施用折纯量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    农用复合肥施用折纯量_万吨_field = models.FloatField(db_column='农用复合肥施用折纯量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    乡村办水电站个数_个_field = models.FloatField(db_column='乡村办水电站个数(个)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    乡村办水电站装机容量_万千瓦_field = models.FloatField(db_column='乡村办水电站装机容量(万千瓦)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    农村用电量_亿千瓦小时_field = models.FloatField(db_column='农村用电量(亿千瓦小时)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '有效灌溉面积农用化肥施用量农村水电站及用电量_csv'


class Output_of_aquatic_products(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    水产品总产量_万吨_field = models.FloatField(db_column='水产品总产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    捕捞产量_吨_field = models.FloatField(db_column='捕捞产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    养殖产量_吨_field = models.FloatField(db_column='养殖产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    鱼类产量_吨_field = models.FloatField(db_column='鱼类产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    虾蟹类产量_吨_field = models.FloatField(db_column='虾蟹类产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    贝类产量_吨_field = models.FloatField(db_column='贝类产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    藻类产量_吨_field = models.FloatField(db_column='藻类产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    海水产品产量_万吨_field = models.FloatField(db_column='海水产品产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    海洋捕捞产量_吨_field = models.FloatField(db_column='海洋捕捞产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    海水养殖产量_吨_field = models.FloatField(db_column='海水养殖产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    天然生产海水产品产量_万吨_field = models.FloatField(db_column='天然生产海水产品产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    人工养殖海水产品产量_万吨_field = models.FloatField(db_column='人工养殖海水产品产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    鱼类海水产品产量_万吨_field = models.FloatField(db_column='鱼类海水产品产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    虾蟹类海水产品产量_万吨_field = models.FloatField(db_column='虾蟹类海水产品产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    贝类海水产品产量_万吨_field = models.FloatField(db_column='贝类海水产品产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    藻类海水产品产量_万吨_field = models.FloatField(db_column='藻类海水产品产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    淡水产品产量_万吨_field = models.FloatField(db_column='淡水产品产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    淡水捕捞产量_吨_field = models.FloatField(db_column='淡水捕捞产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    淡水养殖产量_吨_field = models.FloatField(db_column='淡水养殖产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    天然生产淡水产品产量_万吨_field = models.FloatField(db_column='天然生产淡水产品产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    人工养殖淡水产品产量_万吨_field = models.FloatField(db_column='人工养殖淡水产品产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    鱼类淡水产品产量_万吨_field = models.FloatField(db_column='鱼类淡水产品产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    虾蟹类淡水产品产量_万吨_field = models.FloatField(db_column='虾蟹类淡水产品产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    贝类淡水产品产量_万吨_field = models.FloatField(db_column='贝类淡水产品产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '水产品产量_csv'


class Livestock_output(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    猪出栏数量_万头_field = models.FloatField(db_column='猪出栏数量(万头)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    牛出栏数量_万头_field = models.FloatField(db_column='牛出栏数量(万头)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    羊出栏数量_万只_field = models.FloatField(db_column='羊出栏数量(万只)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    家禽出栏量_万只_field = models.FloatField(db_column='家禽出栏量(万只)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '牲畜出栏量_csv'


class Livestock_raising(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    大牲畜年底头数_万头_field = models.FloatField(db_column='大牲畜年底头数(万头)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    牛期末数量_万头_field = models.FloatField(db_column='牛期末数量(万头)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    马期末数量_万头_field = models.FloatField(db_column='马期末数量(万头)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    驴期末数量_万头_field = models.FloatField(db_column='驴期末数量(万头)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    骡期末数量_万头_field = models.FloatField(db_column='骡期末数量(万头)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    骆驼期末数量_万头_field = models.FloatField(db_column='骆驼期末数量(万头)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    猪年底头数_万头_field = models.FloatField(db_column='猪年底头数(万头)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    羊年底只数_万头_field = models.FloatField(db_column='羊年底只数(万头)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    山羊期末数量_万头_field = models.FloatField(db_column='山羊期末数量(万头)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    绵羊期末数量_万头_field = models.FloatField(db_column='绵羊期末数量(万头)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '牲畜饲养_csv'


class Output_of_livestock_products(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    肉类产量_万吨_field = models.FloatField(db_column='肉类产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    猪肉产量_万吨_field = models.FloatField(db_column='猪肉产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    牛肉产量_万吨_field = models.FloatField(db_column='牛肉产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    羊肉产量_万吨_field = models.FloatField(db_column='羊肉产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    牛奶产量_万吨_field = models.FloatField(db_column='牛奶产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    绵羊毛产量_吨_field = models.FloatField(db_column='绵羊毛产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    细羊毛产量_吨_field = models.FloatField(db_column='细羊毛产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    半细羊毛产量_吨_field = models.FloatField(db_column='半细羊毛产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    山羊毛产量_吨_field = models.FloatField(db_column='山羊毛产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    羊绒产量_吨_field = models.FloatField(db_column='羊绒产量(吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    禽蛋产量_万吨_field = models.FloatField(db_column='禽蛋产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    蜂蜜产量_万吨_field = models.FloatField(db_column='蜂蜜产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '畜产品产量_csv'


class Tea_and_fruit_yield(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    茶叶产量_万吨_field = models.FloatField(db_column='茶叶产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    红茶产量_万吨_field = models.FloatField(db_column='红茶产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    绿茶产量_万吨_field = models.FloatField(db_column='绿茶产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    水果产量_万吨_field = models.FloatField(db_column='水果产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    香蕉产量_万吨_field = models.FloatField(db_column='香蕉产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    苹果产量_万吨_field = models.FloatField(db_column='苹果产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    柑桔产量_万吨_field = models.FloatField(db_column='柑桔产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    梨产量_万吨_field = models.FloatField(db_column='梨产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    葡萄产量_万吨_field = models.FloatField(db_column='葡萄产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    菠萝产量_万吨_field = models.FloatField(db_column='菠萝产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    红枣产量_万吨_field = models.FloatField(db_column='红枣产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    柿子产量_万吨_field = models.FloatField(db_column='柿子产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    园林水果产量_万吨_field = models.FloatField(db_column='园林水果产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    瓜果类产量_万吨_field = models.FloatField(db_column='瓜果类产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    西瓜产量_万吨_field = models.FloatField(db_column='西瓜产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    甜瓜产量_万吨_field = models.FloatField(db_column='甜瓜产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    草莓产量_万吨_field = models.FloatField(db_column='草莓产量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '茶叶水果产量_csv'


class Nyyw(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    herf = models.TextField(blank=True, null=True)
    daa = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    picherf = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nyyw'
