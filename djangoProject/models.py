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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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


class Hnnyyw(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    herf = models.TextField(blank=True, null=True)
    daa = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    picherf = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hnnyyw'


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


class Price(models.Model):
    id = models.IntegerField(primary_key=True)
    class_field = models.CharField(db_column='class', max_length=100)  # Field renamed because it was a Python reserved word.
    variety = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    p22_5 = models.FloatField(db_column='p22-5', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p22_3 = models.FloatField(db_column='p22-3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p22_1 = models.FloatField(db_column='p22-1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p21_11 = models.FloatField(db_column='p21-11', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p21_9 = models.FloatField(db_column='p21-9', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p21_7 = models.FloatField(db_column='p21-7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p21_5 = models.FloatField(db_column='p21-5', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p21_3 = models.FloatField(db_column='p21-3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p21_1 = models.FloatField(db_column='p21-1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p20_11 = models.FloatField(db_column='p20-11', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p20_9 = models.FloatField(db_column='p20-9', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p20_7 = models.FloatField(db_column='p20-7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    yc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ��ʳ����_���_field = models.FloatField(db_column='��ʳ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������ʳ����_���_field = models.FloatField(db_column='������ʳ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��������_���_field = models.FloatField(db_column='��������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_���_field = models.FloatField(db_column='�������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���Ȳ���_���_field = models.FloatField(db_column='���Ȳ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �絾����_���_field = models.FloatField(db_column='�絾����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �е���һ��������_���_field = models.FloatField(db_column='�е���һ��������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ˫��������_���_field = models.FloatField(db_column='˫��������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    С�����_���_field = models.FloatField(db_column='С�����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��С�����_���_field = models.FloatField(db_column='��С�����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��С�����_���_field = models.FloatField(db_column='��С�����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ײ���_���_field = models.FloatField(db_column='���ײ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���Ӳ���_���_field = models.FloatField(db_column='���Ӳ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��������_���_field = models.FloatField(db_column='��������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����������_���_field = models.FloatField(db_column='�����������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_���_field = models.FloatField(db_column='�������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_���_field = models.FloatField(db_column='�������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �̶�����_���_field = models.FloatField(db_column='�̶�����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��С������_���_field = models.FloatField(db_column='��С������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �󶹲���_���_field = models.FloatField(db_column='�󶹲���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_���_field = models.FloatField(db_column='�������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���������_���_field = models.FloatField(db_column='���������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �޻�����_���_field = models.FloatField(db_column='�޻�����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ϲ���_���_field = models.FloatField(db_column='���ϲ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��������_���_field = models.FloatField(db_column='��������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �Ͳ��Ѳ���_���_field = models.FloatField(db_column='�Ͳ��Ѳ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ֥�����_���_field = models.FloatField(db_column='֥�����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����Ѳ���_���_field = models.FloatField(db_column='�����Ѳ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����Ѳ���_���_field = models.FloatField(db_column='�����Ѳ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ϲ���_���_field = models.FloatField(db_column='���ϲ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_���_field = models.FloatField(db_column='�������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ƺ������_���_field = models.FloatField(db_column='�ƺ������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_���_field = models.FloatField(db_column='�������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_���_field = models.FloatField(db_column='�������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_���_field = models.FloatField(db_column='�������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_���_field = models.FloatField(db_column='�������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��˲���_���_field = models.FloatField(db_column='��˲���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��Ҷ����_���_field = models.FloatField(db_column='��Ҷ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���̲���_���_field = models.FloatField(db_column='���̲���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �߲˲���_���_field = models.FloatField(db_column='�߲˲���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '��Ҫũ�����Ʒ����_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ��ʳ��λ�������_����_����_field = models.FloatField(db_column='��ʳ��λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������ʳ��λ�������_����_����_field = models.FloatField(db_column='������ʳ��λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������λ�������_����_����_field = models.FloatField(db_column='������λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ﵥλ�������_����_����_field = models.FloatField(db_column='���ﵥλ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ȵ�λ�������_����_����_field = models.FloatField(db_column='���ȵ�λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �絾��λ�������_����_����_field = models.FloatField(db_column='�絾��λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �е���һ������λ�������_����_����_field = models.FloatField(db_column='�е���һ������λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ˫������λ�������_����_����_field = models.FloatField(db_column='˫������λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    С��λ�������_����_����_field = models.FloatField(db_column='С��λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��С��λ�������_����_����_field = models.FloatField(db_column='��С��λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��С��λ�������_����_����_field = models.FloatField(db_column='��С��λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���׵�λ�������_����_����_field = models.FloatField(db_column='���׵�λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ӵ�λ�������_����_����_field = models.FloatField(db_column='���ӵ�λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������λ�������_����_����_field = models.FloatField(db_column='������λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������ﵥλ�������_����_����_field = models.FloatField(db_column='�������ﵥλ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ����λ�������_����_����_field = models.FloatField(db_column='����λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���൥λ�������_����_����_field = models.FloatField(db_column='���൥λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �󶹵�λ�������_����_����_field = models.FloatField(db_column='�󶹵�λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �̶���λ�������_����_����_field = models.FloatField(db_column='�̶���λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��С����λ�������_����_����_field = models.FloatField(db_column='��С����λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���൥λ�������_����_����_field = models.FloatField(db_column='���൥λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������λ�������_����_����_field = models.FloatField(db_column='������λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �޻���λ�������_����_����_field = models.FloatField(db_column='�޻���λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ϵ�λ�������_����_����_field = models.FloatField(db_column='���ϵ�λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������λ�������_����_����_field = models.FloatField(db_column='������λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �Ͳ��ѵ�λ�������_����_����_field = models.FloatField(db_column='�Ͳ��ѵ�λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ֥�鵥λ�������_����_����_field = models.FloatField(db_column='֥�鵥λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����ѵ�λ�������_����_����_field = models.FloatField(db_column='�����ѵ�λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����ѵ�λ�������_����_����_field = models.FloatField(db_column='�����ѵ�λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���൥λ�������_����_����_field = models.FloatField(db_column='���൥λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ƺ��鵥λ�������_����_����_field = models.FloatField(db_column='�ƺ��鵥λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���鵥λ�������_����_����_field = models.FloatField(db_column='���鵥λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���鵥λ�������_����_����_field = models.FloatField(db_column='���鵥λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���鵥λ�������_����_����_field = models.FloatField(db_column='���鵥λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��Ҷ��λ�������_����_����_field = models.FloatField(db_column='��Ҷ��λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���̵�λ�������_����_����_field = models.FloatField(db_column='���̵�λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ϵ�λ�������_����_����_field = models.FloatField(db_column='���ϵ�λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ᵥλ�������_����_����_field = models.FloatField(db_column='���ᵥλ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��˵�λ�������_����_����_field = models.FloatField(db_column='��˵�λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �߲˵�λ�������_����_����_field = models.FloatField(db_column='�߲˵�λ�������(����/����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '��Ҫũ���ﵥλ�������_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ũ�����ܲ������_ǧ����_field = models.FloatField(db_column='ũ�����ܲ������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ʳ���ﲥ�����_ǧ����_field = models.FloatField(db_column='��ʳ���ﲥ�����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������ʳ�������_ǧ����_field = models.FloatField(db_column='������ʳ�������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������ʳ�������_ǧ����_field = models.FloatField(db_column='������ʳ�������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ﲥ�����_ǧ����_field = models.FloatField(db_column='���ﲥ�����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���Ȳ������_ǧ����_field = models.FloatField(db_column='���Ȳ������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �絾�������_ǧ����_field = models.FloatField(db_column='�絾�������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �е���һ�����������_ǧ����_field = models.FloatField(db_column='�е���һ�����������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ˫�����������_ǧ����_field = models.FloatField(db_column='˫�����������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    С�������_ǧ����_field = models.FloatField(db_column='С�������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��С�������_ǧ����_field = models.FloatField(db_column='��С�������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��С�������_ǧ����_field = models.FloatField(db_column='��С�������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ײ������_ǧ����_field = models.FloatField(db_column='���ײ������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���Ӳ������_ǧ����_field = models.FloatField(db_column='���Ӳ������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����������_ǧ����_field = models.FloatField(db_column='�����������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������ﲥ�����_ǧ����_field = models.FloatField(db_column='�������ﲥ�����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���������_ǧ����_field = models.FloatField(db_column='���������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ಥ�����_ǧ����_field = models.FloatField(db_column='���ಥ�����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �󶹲������_ǧ����_field = models.FloatField(db_column='�󶹲������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �̶��������_ǧ����_field = models.FloatField(db_column='�̶��������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��С���������_ǧ����_field = models.FloatField(db_column='��С���������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ಥ�����_ǧ����_field = models.FloatField(db_column='���ಥ�����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����������_ǧ����_field = models.FloatField(db_column='�����������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ϲ������_ǧ����_field = models.FloatField(db_column='���ϲ������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����������_ǧ����_field = models.FloatField(db_column='�����������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �Ͳ��Ѳ������_ǧ����_field = models.FloatField(db_column='�Ͳ��Ѳ������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ֥�鲥�����_ǧ����_field = models.FloatField(db_column='֥�鲥�����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����Ѳ������_ǧ����_field = models.FloatField(db_column='�����Ѳ������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����Ѳ������_ǧ����_field = models.FloatField(db_column='�����Ѳ������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �޻��������_ǧ����_field = models.FloatField(db_column='�޻��������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ಥ�����_ǧ����_field = models.FloatField(db_column='���ಥ�����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ƺ��鲥�����_ǧ����_field = models.FloatField(db_column='�ƺ��鲥�����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���鲥�����_ǧ����_field = models.FloatField(db_column='���鲥�����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���鲥�����_ǧ����_field = models.FloatField(db_column='���鲥�����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���鲥�����_ǧ����_field = models.FloatField(db_column='���鲥�����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ϲ������_ǧ����_field = models.FloatField(db_column='���ϲ������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���Ქ�����_ǧ����_field = models.FloatField(db_column='���Ქ�����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��˲������_ǧ����_field = models.FloatField(db_column='��˲������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��Ҷ�������_ǧ����_field = models.FloatField(db_column='��Ҷ�������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���̲������_ǧ����_field = models.FloatField(db_column='���̲������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �߲˲������_ǧ����_field = models.FloatField(db_column='�߲˲������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ҩ�Ĳ������_ǧ����_field = models.FloatField(db_column='ҩ�Ĳ������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ����ũ���ﲥ�����_ǧ����_field = models.FloatField(db_column='����ũ���ﲥ�����(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����ϲ������_ǧ����_field = models.FloatField(db_column='�����ϲ������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '��Ҫũ���ﲥ�����_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ľ�Ĳ���_��������_field = models.FloatField(db_column='ľ�Ĳ���(��������)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �𽺲���_��_field = models.FloatField(db_column='�𽺲���(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��֬����_��_field = models.FloatField(db_column='��֬����(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_��_field = models.FloatField(db_column='�������(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ͩ�Ѳ���_��_field = models.FloatField(db_column='��ͩ�Ѳ���(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �Ͳ��Ѳ���_��_field = models.FloatField(db_column='�Ͳ��Ѳ���(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����Ѳ���_��_field = models.FloatField(db_column='�����Ѳ���(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �屶�Ѳ���_��_field = models.FloatField(db_column='�屶�Ѳ���(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��Ƭ����_��_field = models.FloatField(db_column='��Ƭ����(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ����Ƭ����_��_field = models.FloatField(db_column='����Ƭ����(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �Ͻ�����_��_field = models.FloatField(db_column='�Ͻ�����(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '��Ҫ�ֲ�Ʒ����_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ũ������ҵ����ֵ_��Ԫ_field = models.FloatField(db_column='ũ������ҵ����ֵ(��Ԫ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ũҵ����ֵ_��Ԫ_field = models.FloatField(db_column='ũҵ����ֵ(��Ԫ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ҵ����ֵ_��Ԫ_field = models.FloatField(db_column='��ҵ����ֵ(��Ԫ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ҵ����ֵ_��Ԫ_field = models.FloatField(db_column='��ҵ����ֵ(��Ԫ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ҵ����ֵ_��Ԫ_field = models.FloatField(db_column='��ҵ����ֵ(��Ԫ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'ũ������ҵ����ֵ_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ũ������ҵ�ܲ�ֵ_��Ԫ_field = models.FloatField(db_column='ũ������ҵ�ܲ�ֵ(��Ԫ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ũҵ�ܲ�ֵ_��Ԫ_field = models.FloatField(db_column='ũҵ�ܲ�ֵ(��Ԫ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ҵ�ܲ�ֵ_��Ԫ_field = models.FloatField(db_column='��ҵ�ܲ�ֵ(��Ԫ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ҵ�ܲ�ֵ_��Ԫ_field = models.FloatField(db_column='��ҵ�ܲ�ֵ(��Ԫ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ҵ�ܲ�ֵ_��Ԫ_field = models.FloatField(db_column='��ҵ�ܲ�ֵ(��Ԫ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ũ������ҵ�ܲ�ֵָ��_�ٷ�֮_field = models.FloatField(db_column='ũ������ҵ�ܲ�ֵָ��(�ٷ�֮)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ũҵ�ܲ�ֵָ��_�ٷ�֮_field = models.FloatField(db_column='ũҵ�ܲ�ֵָ��(�ٷ�֮)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ҵ�ܲ�ֵָ��_�ٷ�֮_field = models.FloatField(db_column='��ҵ�ܲ�ֵָ��(�ٷ�֮)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ҵ�ܲ�ֵָ��_�ٷ�֮_field = models.FloatField(db_column='��ҵ�ܲ�ֵָ��(�ٷ�֮)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ҵ�ܲ�ֵָ��_�ٷ�֮_field = models.FloatField(db_column='��ҵ�ܲ�ֵָ��(�ٷ�֮)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'ũ������ҵ�ܲ�ֵ��ָ��_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ��Ч������_ǧ����_field = models.FloatField(db_column='��Ч������(ǧ����)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ũ�û���ʩ���۴���_���_field = models.FloatField(db_column='ũ�û���ʩ���۴���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ũ�õ���ʩ���۴���_���_field = models.FloatField(db_column='ũ�õ���ʩ���۴���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ũ���׷�ʩ���۴���_���_field = models.FloatField(db_column='ũ���׷�ʩ���۴���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ũ�üط�ʩ���۴���_���_field = models.FloatField(db_column='ũ�üط�ʩ���۴���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ũ�ø��Ϸ�ʩ���۴���_���_field = models.FloatField(db_column='ũ�ø��Ϸ�ʩ���۴���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ����ˮ��վ����_��_field = models.FloatField(db_column='����ˮ��վ����(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ����ˮ��վװ������_��ǧ��_field = models.FloatField(db_column='����ˮ��վװ������(��ǧ��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ũ���õ���_��ǧ��Сʱ_field = models.FloatField(db_column='ũ���õ���(��ǧ��Сʱ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '��Ч������ũ�û���ʩ����ũ��ˮ��վ���õ���_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ˮ��Ʒ�ܲ���_���_field = models.FloatField(db_column='ˮ��Ʒ�ܲ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���̲���_��_field = models.FloatField(db_column='���̲���(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ֳ����_��_field = models.FloatField(db_column='��ֳ����(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_��_field = models.FloatField(db_column='�������(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Ϻз�����_��_field = models.FloatField(db_column='Ϻз�����(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_��_field = models.FloatField(db_column='�������(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_��_field = models.FloatField(db_column='�������(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ˮ��Ʒ����_���_field = models.FloatField(db_column='��ˮ��Ʒ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����̲���_��_field = models.FloatField(db_column='�����̲���(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ˮ��ֳ����_��_field = models.FloatField(db_column='��ˮ��ֳ����(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��Ȼ������ˮ��Ʒ����_���_field = models.FloatField(db_column='��Ȼ������ˮ��Ʒ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �˹���ֳ��ˮ��Ʒ����_���_field = models.FloatField(db_column='�˹���ֳ��ˮ��Ʒ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ຣˮ��Ʒ����_���_field = models.FloatField(db_column='���ຣˮ��Ʒ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Ϻз�ຣˮ��Ʒ����_���_field = models.FloatField(db_column='Ϻз�ຣˮ��Ʒ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ຣˮ��Ʒ����_���_field = models.FloatField(db_column='���ຣˮ��Ʒ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ຣˮ��Ʒ����_���_field = models.FloatField(db_column='���ຣˮ��Ʒ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ˮ��Ʒ����_���_field = models.FloatField(db_column='��ˮ��Ʒ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ˮ���̲���_��_field = models.FloatField(db_column='��ˮ���̲���(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ˮ��ֳ����_��_field = models.FloatField(db_column='��ˮ��ֳ����(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��Ȼ������ˮ��Ʒ����_���_field = models.FloatField(db_column='��Ȼ������ˮ��Ʒ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �˹���ֳ��ˮ��Ʒ����_���_field = models.FloatField(db_column='�˹���ֳ��ˮ��Ʒ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���൭ˮ��Ʒ����_���_field = models.FloatField(db_column='���൭ˮ��Ʒ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Ϻз�൭ˮ��Ʒ����_���_field = models.FloatField(db_column='Ϻз�൭ˮ��Ʒ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���൭ˮ��Ʒ����_���_field = models.FloatField(db_column='���൭ˮ��Ʒ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'ˮ��Ʒ����_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ���������_��ͷ_field = models.FloatField(db_column='���������(��ͷ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ţ��������_��ͷ_field = models.FloatField(db_column='ţ��������(��ͷ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���������_��ֻ_field = models.FloatField(db_column='���������(��ֻ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ݳ�����_��ֻ_field = models.FloatField(db_column='���ݳ�����(��ֻ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '���������_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ���������ͷ��_��ͷ_field = models.FloatField(db_column='���������ͷ��(��ͷ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ţ��ĩ����_��ͷ_field = models.FloatField(db_column='ţ��ĩ����(��ͷ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ����ĩ����_��ͷ_field = models.FloatField(db_column='����ĩ����(��ͷ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ¿��ĩ����_��ͷ_field = models.FloatField(db_column='¿��ĩ����(��ͷ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ����ĩ����_��ͷ_field = models.FloatField(db_column='����ĩ����(��ͷ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������ĩ����_��ͷ_field = models.FloatField(db_column='������ĩ����(��ͷ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����ͷ��_��ͷ_field = models.FloatField(db_column='�����ͷ��(��ͷ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����ֻ��_��ͷ_field = models.FloatField(db_column='�����ֻ��(��ͷ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ɽ����ĩ����_��ͷ_field = models.FloatField(db_column='ɽ����ĩ����(��ͷ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������ĩ����_��ͷ_field = models.FloatField(db_column='������ĩ����(��ͷ)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '��������_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    �������_���_field = models.FloatField(db_column='�������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_���_field = models.FloatField(db_column='�������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ţ�����_���_field = models.FloatField(db_column='ţ�����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_���_field = models.FloatField(db_column='�������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ţ�̲���_���_field = models.FloatField(db_column='ţ�̲���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ����ë����_��_field = models.FloatField(db_column='����ë����(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ϸ��ë����_��_field = models.FloatField(db_column='ϸ��ë����(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ϸ��ë����_��_field = models.FloatField(db_column='��ϸ��ë����(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ɽ��ë����_��_field = models.FloatField(db_column='ɽ��ë����(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���޲���_��_field = models.FloatField(db_column='���޲���(��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ݵ�����_���_field = models.FloatField(db_column='�ݵ�����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���۲���_���_field = models.FloatField(db_column='���۲���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '���Ʒ����_csv'


class Csv(models.Model):
    ʡ�ݱ��� = models.IntegerField(blank=True, null=True)
    ʡ�� = models.CharField(max_length=8, blank=True, null=True)
    ��� = models.IntegerField(blank=True, null=True)
    ��Ҷ����_���_field = models.FloatField(db_column='��Ҷ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������_���_field = models.FloatField(db_column='������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �̲����_���_field = models.FloatField(db_column='�̲����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ˮ������_���_field = models.FloatField(db_column='ˮ������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �㽶����_���_field = models.FloatField(db_column='�㽶����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ƻ������_���_field = models.FloatField(db_column='ƻ������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �̽۲���_���_field = models.FloatField(db_column='�̽۲���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����_���_field = models.FloatField(db_column='�����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���Ѳ���_���_field = models.FloatField(db_column='���Ѳ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ܲ���_���_field = models.FloatField(db_column='���ܲ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������_���_field = models.FloatField(db_column='�������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���Ӳ���_���_field = models.FloatField(db_column='���Ӳ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ԰��ˮ������_���_field = models.FloatField(db_column='԰��ˮ������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �Ϲ������_���_field = models.FloatField(db_column='�Ϲ������(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���ϲ���_���_field = models.FloatField(db_column='���ϲ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ϲ���_���_field = models.FloatField(db_column='��ϲ���(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ��ݮ����_���_field = models.FloatField(db_column='��ݮ����(���)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '��Ҷˮ������_csv'
