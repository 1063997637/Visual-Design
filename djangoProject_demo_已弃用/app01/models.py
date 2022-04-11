# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class non_ferrous_metals(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    铜矿储量_万吨_field = models.FloatField(db_column='铜矿储量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    铅矿储量_万吨_field = models.FloatField(db_column='铅矿储量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    锌矿储量_万吨_field = models.FloatField(db_column='锌矿储量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    铝土矿储量_万吨_field = models.FloatField(db_column='铝土矿储量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    菱镁矿储量_万吨_field = models.FloatField(db_column='菱镁矿储量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    硫铁矿储量_万吨_field = models.FloatField(db_column='硫铁矿储量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    磷矿储量_亿吨_field = models.FloatField(db_column='磷矿储量(亿吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    高岭土储量_万吨_field = models.FloatField(db_column='高岭土储量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '主要有色金属_非金属矿产基础储量_csv'


class Main_energy_ferrous_metal(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    石油储量_万吨_field = models.FloatField(db_column='石油储量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    天然气储量_亿立方米_field = models.FloatField(db_column='天然气储量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    煤炭储量_亿吨_field = models.FloatField(db_column='煤炭储量(亿吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    铁矿储量_亿吨_field = models.FloatField(db_column='铁矿储量(亿吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    锰矿储量_万吨_field = models.FloatField(db_column='锰矿储量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    铬矿储量_万吨_field = models.FloatField(db_column='铬矿储量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    钒矿储量_万吨_field = models.FloatField(db_column='钒矿储量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    原生钛铁矿储量_万吨_field = models.FloatField(db_column='原生钛铁矿储量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '主要能源_黑色金属矿产基础储量_csv'


class water_supply(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    供水总量_亿立方米_field = models.FloatField(db_column='供水总量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    地表水供水总量_亿立方米_field = models.FloatField(db_column='地表水供水总量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    地下水供水总量_亿立方米_field = models.FloatField(db_column='地下水供水总量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    其他供水总量_亿立方米_field = models.FloatField(db_column='其他供水总量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    用水总量_亿立方米_field = models.FloatField(db_column='用水总量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    农业用水总量_亿立方米_field = models.FloatField(db_column='农业用水总量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    工业用水总量_亿立方米_field = models.FloatField(db_column='工业用水总量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    生活用水总量_亿立方米_field = models.FloatField(db_column='生活用水总量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    生态用水总量_亿立方米_field = models.FloatField(db_column='生态用水总量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    人均用水量_立方米_人_field = models.FloatField(db_column='人均用水量(立方米/人)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '供水用水情况_csv'


class passenger_volume(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    客运量_万人_field = models.FloatField(db_column='客运量(万人)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    铁路客运量_万人_field = models.FloatField(db_column='铁路客运量(万人)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    国家铁路客运量_万人_field = models.CharField(db_column='国家铁路客运量(万人)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    地方铁路客运量_万人_field = models.CharField(db_column='地方铁路客运量(万人)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    合资铁路客运量_万人_field = models.CharField(db_column='合资铁路客运量(万人)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    公路客运量_万人_field = models.FloatField(db_column='公路客运量(万人)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    水运客运量_万人_field = models.FloatField(db_column='水运客运量(万人)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '客运量_csv'


class forest_resources(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    林业用地面积_万公顷_field = models.FloatField(db_column='林业用地面积(万公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    森林面积_万公顷_field = models.FloatField(db_column='森林面积(万公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    人工林面积_万公顷_field = models.FloatField(db_column='人工林面积(万公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    森林覆盖率_field = models.FloatField(db_column='森林覆盖率(百分之)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    活立木总蓄积量_亿立方米_field = models.FloatField(db_column='活立木总蓄积量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    森林蓄积量_亿立方米_field = models.FloatField(db_column='森林蓄积量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '森林资源_csv'


class water_resource(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    水资源总量_亿立方米_field = models.FloatField(db_column='水资源总量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    地表水资源量_亿立方米_field = models.FloatField(db_column='地表水资源量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    地下水资源量_亿立方米_field = models.FloatField(db_column='地下水资源量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    地表水与地下水资源重复量_亿立方米_field = models.FloatField(db_column='地表水与地下水资源重复量(亿立方米)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    人均水资源量_立方米_人_field = models.FloatField(db_column='人均水资源量(立方米/人)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '水资源_csv'


class freight_transport(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    货运量_万吨_field = models.FloatField(db_column='货运量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    铁路货运量_万吨_field = models.FloatField(db_column='铁路货运量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    国家铁路货运量_万吨_field = models.CharField(db_column='国家铁路货运量(万吨)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    地方铁路货运量_万吨_field = models.CharField(db_column='地方铁路货运量(万吨)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    合资铁路货运量_万吨_field = models.CharField(db_column='合资铁路货运量(万吨)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    公路货运量_万吨_field = models.FloatField(db_column='公路货运量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    水运货运量_万吨_field = models.FloatField(db_column='水运货运量(万吨)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '货运量_csv'


class transportation_route(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    铁路营业里程_万公里_field = models.FloatField(db_column='铁路营业里程(万公里)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    内河航道里程_万公里_field = models.FloatField(db_column='内河航道里程(万公里)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    公路里程_万公里_field = models.FloatField(db_column='公路里程(万公里)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    等级公路里程_万公里_field = models.FloatField(db_column='等级公路里程(万公里)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    高速等级公路里程_万公里_field = models.FloatField(db_column='高速等级公路里程(万公里)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    一级等级公路里程_万公里_field = models.FloatField(db_column='一级等级公路里程(万公里)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    二级等级公路里程_万公里_field = models.FloatField(db_column='二级等级公路里程(万公里)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    等外公路公路里程_万公里_field = models.FloatField(db_column='等外公路公路里程(万公里)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '运输线路长度_csv'


class afforestation_area(models.Model):
    省份编码 = models.IntegerField(blank=True, null=True)
    省份 = models.CharField(max_length=8, blank=True, null=True)
    年份 = models.IntegerField(blank=True, null=True)
    造林总面积_千公顷_field = models.FloatField(db_column='造林总面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    当年人工造林面积_千公顷_field = models.FloatField(db_column='当年人工造林面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    当年飞机播种面积_千公顷_field = models.FloatField(db_column='当年飞机播种面积(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    封山育林_千公顷_field = models.FloatField(db_column='封山育林(千公顷)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    用材林当年造林面积_千公顷_field = models.CharField(db_column='用材林当年造林面积(千公顷)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    经济林当年造林面积_千公顷_field = models.CharField(db_column='经济林当年造林面积(千公顷)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    防护林当年造林面积_千公顷_field = models.CharField(db_column='防护林当年造林面积(千公顷)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    薪炭林当年造林面积_千公顷_field = models.CharField(db_column='薪炭林当年造林面积(千公顷)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    特种用林当年造林面积_千公顷_field = models.CharField(db_column='特种用林当年造林面积(千公顷)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '造林面积_csv'
