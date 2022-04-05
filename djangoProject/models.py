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


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ͭ����_���_field = models.FloatField(db_column='ͭ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Ǧ����_���_field = models.FloatField(db_column='Ǧ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    п����_���_field = models.FloatField(db_column='п����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��������_���_field = models.FloatField(db_column='��������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��þ����_���_field = models.FloatField(db_column='��þ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��������_���_field = models.FloatField(db_column='��������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �׿���_�ڶ�_field = models.FloatField(db_column='�׿���(�ڶ�)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ����������_���_field = models.FloatField(db_column='����������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '��Ҫ��ɫ����_�ǽ��������������_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ʯ�ʹ���_���_field = models.FloatField(db_column='ʯ�ʹ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��Ȼ������_��������_field = models.FloatField(db_column='��Ȼ������(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ú̿����_�ڶ�_field = models.FloatField(db_column='ú̿����(�ڶ�)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������_�ڶ�_field = models.FloatField(db_column='������(�ڶ�)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �̿���_���_field = models.FloatField(db_column='�̿���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������_���_field = models.FloatField(db_column='������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������_���_field = models.FloatField(db_column='������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ԭ����������_���_field = models.FloatField(db_column='ԭ����������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '��Ҫ��Դ_��ɫ���������������_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ��ˮ����_��������_field = models.FloatField(db_column='��ˮ����(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ر�ˮ��ˮ����_��������_field = models.FloatField(db_column='�ر�ˮ��ˮ����(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ����ˮ��ˮ����_��������_field = models.FloatField(db_column='����ˮ��ˮ����(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������ˮ����_��������_field = models.FloatField(db_column='������ˮ����(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ˮ����_��������_field = models.FloatField(db_column='��ˮ����(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ũҵ��ˮ����_��������_field = models.FloatField(db_column='ũҵ��ˮ����(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ҵ��ˮ����_��������_field = models.FloatField(db_column='��ҵ��ˮ����(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������ˮ����_��������_field = models.FloatField(db_column='������ˮ����(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��̬��ˮ����_��������_field = models.FloatField(db_column='��̬��ˮ����(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �˾���ˮ��_������_��_field = models.FloatField(db_column='�˾���ˮ��(������/��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '��ˮ��ˮ���_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ������_����_field = models.FloatField(db_column='������(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��·������_����_field = models.FloatField(db_column='��·������(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������·������_����_field = models.CharField(db_column='������·������(����)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ط���·������_����_field = models.CharField(db_column='�ط���·������(����)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������·������_����_field = models.CharField(db_column='������·������(����)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��·������_����_field = models.FloatField(db_column='��·������(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ˮ�˿�����_����_field = models.FloatField(db_column='ˮ�˿�����(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '������_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ��ҵ�õ����_����_field = models.FloatField(db_column='��ҵ�õ����(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ɭ�����_����_field = models.FloatField(db_column='ɭ�����(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �˹������_����_field = models.FloatField(db_column='�˹������(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ɭ�ָ�����_field = models.FloatField(db_column='ɭ�ָ�����(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ����ľ�������_��������_field = models.FloatField(db_column='����ľ�������(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ɭ�������_��������_field = models.FloatField(db_column='ɭ�������(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'ɭ����Դ_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ˮ��Դ����_��������_field = models.FloatField(db_column='ˮ��Դ����(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ر�ˮ��Դ��_��������_field = models.FloatField(db_column='�ر�ˮ��Դ��(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ����ˮ��Դ��_��������_field = models.FloatField(db_column='����ˮ��Դ��(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ر�ˮ�����ˮ��Դ�ظ���_��������_field = models.FloatField(db_column='�ر�ˮ�����ˮ��Դ�ظ���(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �˾�ˮ��Դ��_������_��_field = models.FloatField(db_column='�˾�ˮ��Դ��(������/��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'ˮ��Դ_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ������_���_field = models.FloatField(db_column='������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��·������_���_field = models.FloatField(db_column='��·������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������·������_���_field = models.CharField(db_column='������·������(���)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ط���·������_���_field = models.CharField(db_column='�ط���·������(���)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������·������_���_field = models.CharField(db_column='������·������(���)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��·������_���_field = models.FloatField(db_column='��·������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ˮ�˻�����_���_field = models.FloatField(db_column='ˮ�˻�����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '������_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ��·Ӫҵ���_����_field = models.FloatField(db_column='��·Ӫҵ���(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ںӺ������_����_field = models.FloatField(db_column='�ںӺ������(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��·���_����_field = models.FloatField(db_column='��·���(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ȼ���·���_����_field = models.FloatField(db_column='�ȼ���·���(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ٵȼ���·���_����_field = models.FloatField(db_column='���ٵȼ���·���(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    һ���ȼ���·���_����_field = models.FloatField(db_column='һ���ȼ���·���(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����ȼ���·���_����_field = models.FloatField(db_column='�����ȼ���·���(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���⹫·��·���_����_field = models.FloatField(db_column='���⹫·��·���(����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '������·����_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ���������_ǧ����_field = models.FloatField(db_column='���������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����˹��������_ǧ����_field = models.FloatField(db_column='�����˹��������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ����ɻ��������_ǧ����_field = models.FloatField(db_column='����ɻ��������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ɽ����_ǧ����_field = models.FloatField(db_column='��ɽ����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ò��ֵ����������_ǧ����_field = models.CharField(db_column='�ò��ֵ����������(ǧ����)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����ֵ����������_ǧ����_field = models.CharField(db_column='�����ֵ����������(ǧ����)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����ֵ����������_ǧ����_field = models.CharField(db_column='�����ֵ����������(ǧ����)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    н̿�ֵ����������_ǧ����_field = models.CharField(db_column='н̿�ֵ����������(ǧ����)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������ֵ����������_ǧ����_field = models.CharField(db_column='�������ֵ����������(ǧ����)', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '�������_csv'
