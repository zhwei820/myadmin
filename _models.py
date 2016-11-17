# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AChannelSet(models.Model):
    channel = models.CharField(unique=True, max_length=50)
    parent_id = models.IntegerField()
    weight = models.IntegerField()
    status = models.IntegerField()
    operator = models.CharField(max_length=50, blank=True, null=True)
    utime = models.DateTimeField()
    ctime = models.DateTimeField()
    remark = models.CharField(max_length=200)
    channel_type = models.CharField(max_length=10)
    is_public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_channel_set'


class AMenu(models.Model):
    type = models.CharField(max_length=20)
    action = models.CharField(unique=True, max_length=20)
    status = models.IntegerField()
    name = models.CharField(max_length=50)
    parent_id = models.IntegerField()
    icon = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'a_menu'


class AUserExtra(models.Model):
    permission_str = models.TextField()
    role = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'a_user_extra'


class AppCategory(models.Model):
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    is_active = models.IntegerField()
    order = models.IntegerField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_category'


class AppCity(models.Model):
    name = models.CharField(max_length=64)
    capital = models.IntegerField()
    area = models.BigIntegerField(blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    country = models.ForeignKey('AppCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_city'
        unique_together = (('name', 'country'),)


class AppContinent(models.Model):
    name = models.CharField(max_length=256)
    order = models.IntegerField()
    file = models.CharField(max_length=100)
    ctime = models.DateTimeField()
    pay_status = models.SmallIntegerField()
    utime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_continent'


class AppCountry(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=2)
    independence_day = models.DateField(blank=True, null=True)
    area = models.BigIntegerField(blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    order = models.IntegerField()
    description = models.TextField()
    architecture = models.TextField()
    continent = models.ForeignKey(AppContinent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_country'


class AppFridge(models.Model):
    name = models.CharField(max_length=64)
    type = models.SmallIntegerField()
    description = models.TextField()
    is_quiet = models.IntegerField()
    order = models.IntegerField()
    kitchensink = models.ForeignKey('AppKitchensink', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_fridge'


class AppKitchensink(models.Model):
    name = models.CharField(max_length=64)
    help_text = models.CharField(max_length=64)
    multiple_in_row = models.CharField(max_length=64)
    multiple2 = models.CharField(max_length=10)
    textfield = models.TextField()
    file = models.CharField(max_length=100)
    readonly_field = models.CharField(max_length=127)
    date = models.DateField(blank=True, null=True)
    date_and_time = models.DateTimeField(blank=True, null=True)
    date_widget = models.DateField(blank=True, null=True)
    datetime_widget = models.DateTimeField(blank=True, null=True)
    boolean = models.IntegerField()
    boolean_with_help = models.IntegerField()
    horizontal_choices = models.SmallIntegerField()
    vertical_choices = models.SmallIntegerField()
    choices = models.SmallIntegerField()
    hidden_checkbox = models.IntegerField()
    hidden_choice = models.SmallIntegerField()
    hidden_charfield = models.CharField(max_length=64)
    hidden_charfield2 = models.CharField(max_length=64)
    enclosed1 = models.CharField(max_length=64)
    enclosed2 = models.CharField(max_length=64)
    country = models.ForeignKey(AppCountry, models.DO_NOTHING)
    linked_foreign_key = models.ForeignKey(AppCountry, models.DO_NOTHING)
    raw_id_field = models.ForeignKey(AppCountry, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_kitchensink'


class AppMicrowave(models.Model):
    name = models.CharField(max_length=64)
    type = models.SmallIntegerField()
    is_compact = models.IntegerField()
    kitchensink = models.ForeignKey(AppKitchensink, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_microwave'


class AppReversioneditem(models.Model):
    name = models.CharField(max_length=64)
    quality = models.SmallIntegerField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_reversioneditem'


class AppWysiwygeditor(models.Model):
    name = models.CharField(max_length=64)
    redactor = models.TextField()
    redactor2 = models.TextField()
    ckeditor = models.TextField()

    class Meta:
        managed = False
        db_table = 'app_wysiwygeditor'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
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
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCommentFlags(models.Model):
    flag = models.CharField(max_length=30)
    flag_date = models.DateTimeField()
    comment = models.ForeignKey('DjangoComments', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_comment_flags'
        unique_together = (('user', 'comment', 'flag'),)


class DjangoComments(models.Model):
    object_pk = models.TextField()
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=254)
    user_url = models.CharField(max_length=200)
    comment = models.TextField()
    submit_date = models.DateTimeField()
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    is_public = models.IntegerField()
    is_removed = models.IntegerField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_comments'


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


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class HostAccessrecord(models.Model):
    date = models.DateField()
    user_count = models.IntegerField()
    view_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'host_accessrecord'


class HostHost(models.Model):
    name = models.CharField(max_length=64)
    nagios_name = models.CharField(max_length=64, blank=True, null=True)
    ip = models.CharField(max_length=39)
    internal_ip = models.CharField(max_length=39)
    user = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    ssh_port = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField()
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    cpu = models.CharField(max_length=64)
    core_num = models.SmallIntegerField()
    hard_disk = models.IntegerField()
    memory = models.IntegerField()
    system = models.CharField(max_length=32)
    system_version = models.CharField(max_length=32)
    system_arch = models.CharField(max_length=32)
    create_time = models.DateField()
    guarantee_date = models.DateField()
    service_type = models.CharField(max_length=32)
    description = models.TextField()
    idc = models.ForeignKey('HostIdc', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'host_host'


class HostHostgroup(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'host_hostgroup'


class HostHostgroupHosts(models.Model):
    hostgroup = models.ForeignKey(HostHostgroup, models.DO_NOTHING)
    host = models.ForeignKey(HostHost, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'host_hostgroup_hosts'
        unique_together = (('hostgroup', 'host'),)


class HostIdc(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    contact = models.CharField(max_length=32)
    telphone = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    customer_id = models.CharField(max_length=128)
    create_time = models.DateField()

    class Meta:
        managed = False
        db_table = 'host_idc'


class HostMaintainlog(models.Model):
    maintain_type = models.CharField(max_length=32)
    hard_type = models.CharField(max_length=16)
    time = models.DateTimeField()
    operator = models.CharField(max_length=16)
    note = models.TextField()
    host = models.ForeignKey(HostHost, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'host_maintainlog'


class OBanner(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    os_type = models.IntegerField(blank=True, null=True)
    pic_url = models.CharField(max_length=200, blank=True, null=True)
    click_url = models.CharField(max_length=500, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    channel = models.TextField(blank=True, null=True)
    channel_type = models.IntegerField()
    open_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'o_banner'


class OUserBasic(models.Model):
    uid = models.AutoField(primary_key=True)
    ctime = models.DateTimeField()
    channel = models.CharField(max_length=16)
    os_type = models.CharField(max_length=8)
    app_version = models.CharField(max_length=16)
    package_name = models.CharField(max_length=30)
    reg_ip = models.CharField(max_length=15)
    invite_uid = models.IntegerField()
    reg_source = models.CharField(max_length=2)
    reg_qid = models.CharField(max_length=64)
    bind_mobile = models.BigIntegerField()
    status = models.IntegerField()
    utime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'o_user_basic'


class OUserExtra(models.Model):
    uid = models.IntegerField(primary_key=True)
    reg_source = models.CharField(max_length=2)
    reg_qid = models.CharField(max_length=64)
    token = models.CharField(max_length=256)
    ticket = models.CharField(max_length=256)
    nickname = models.CharField(max_length=512)
    gender = models.CharField(max_length=1)
    figure_url = models.CharField(max_length=256)
    figure_url_other = models.CharField(max_length=1000, blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'o_user_extra'


class OUserMsg00(models.Model):
    uid = models.IntegerField()
    info_title = models.CharField(max_length=50)
    info_subtitle = models.CharField(max_length=64)
    content = models.TextField()
    share_msg = models.CharField(max_length=255)
    info_time = models.DateTimeField()
    info_type = models.IntegerField()
    info_notify = models.IntegerField()
    status = models.IntegerField()
    end_time = models.DateTimeField()
    click_url = models.CharField(max_length=300, blank=True, null=True)
    button_text = models.CharField(max_length=40, blank=True, null=True)
    url_images = models.CharField(max_length=500)
    share_url = models.CharField(max_length=500)
    category = models.CharField(max_length=20)
    icon = models.CharField(max_length=500)
    pid = models.IntegerField()
    package_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'o_user_msg_00'


class OVerifyLog(models.Model):
    pnum = models.BigIntegerField()
    device_id = models.CharField(max_length=50)
    status = models.IntegerField()
    code = models.CharField(max_length=6)
    package_name = models.CharField(max_length=100, blank=True, null=True)
    app_version = models.CharField(max_length=20, blank=True, null=True)
    os_type = models.CharField(max_length=20, blank=True, null=True)
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'o_verify_log'


class OVersion(models.Model):
    version = models.CharField(max_length=15)
    os_type = models.CharField(max_length=10)
    ctime = models.DateTimeField()
    what_news = models.TextField()
    update_is_recommend = models.IntegerField()
    update_is_force = models.IntegerField()
    app_id = models.IntegerField()
    dl_url = models.CharField(max_length=255)
    channel = models.CharField(max_length=36)
    status = models.IntegerField()
    rate = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'o_version'
        unique_together = (('version', 'os_type', 'app_id', 'channel'),)


class ReversionRevision(models.Model):
    date_created = models.DateTimeField()
    comment = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reversion_revision'


class ReversionVersion(models.Model):
    object_id = models.CharField(max_length=191)
    format = models.CharField(max_length=255)
    serialized_data = models.TextField()
    object_repr = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    revision = models.ForeignKey(ReversionRevision, models.DO_NOTHING)
    db = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'reversion_version'
        unique_together = (('db', 'content_type', 'object_id', 'revision'),)


class TDeviceUid(models.Model):
    device_id = models.CharField(max_length=50, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_device_uid'


class XadminBookmark(models.Model):
    title = models.CharField(max_length=128)
    url_name = models.CharField(max_length=64)
    query = models.CharField(max_length=1000)
    is_share = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xadmin_bookmark'


class XadminLog(models.Model):
    action_time = models.DateTimeField()
    ip_addr = models.CharField(max_length=39, blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.CharField(max_length=32)
    message = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'xadmin_log'


class XadminUsersettings(models.Model):
    key = models.CharField(max_length=256)
    value = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'xadmin_usersettings'


class XadminUserwidget(models.Model):
    page_id = models.CharField(max_length=256)
    widget_type = models.CharField(max_length=50)
    value = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'xadmin_userwidget'
