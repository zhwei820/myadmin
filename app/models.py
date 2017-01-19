# coding=utf-8

from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

PRESENT_STATE_CHOICES = (
    (-1, "作弊"),
    (1, "待审核"),
    (2, "审核通过"),
    (3, "提现成功"),
    (4, "提现失败"),
    (5, "打款中"),
    (6, "已退款"),
    (7, "人工退款"),
    (8, "账目不平"),
)

AD_STATUS_CHOICES = (
    (0, "未上线"),
    (1, "上线"),
    (2, "暂缓上线"),
    (3, "下线"),
)

from multiselectfield import MultiSelectField

MY_CHOICES = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))

MY_CHOICES2 = ((1, '大图广告'),
               (2, '首页banner'),
               (3, '特惠banner'),
               (4, '右拉banner'),
               (5, '列表页'))


class Ads(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=2,
                            help_text='ISO 3166-1 alpha-2 - two character '
                                      'country code')
    description = models.TextField(blank=True,
                                   help_text='Try and enter few some more '
                                             'lines')
    cpm_num_all = models.IntegerField(default=0)
    cpc_num_all = models.IntegerField(default=0)
    my_field = MultiSelectField(choices=MY_CHOICES)
    my_field2 = MultiSelectField(choices=MY_CHOICES2,
                                 max_choices=10,
                                 max_length=10)
    start_time = models.DateTimeField(u"开始时间")
    end_time = models.DateTimeField(u"结束时间")
    status = models.SmallIntegerField(
        u"状态", default=0, db_index=True,
        choices=AD_STATUS_CHOICES,
        help_text=u"广告状态")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "广告"
        verbose_name = "广告"


class TimeIntervals(models.Model):
    start_time = models.DateTimeField(u"开始时间")
    end_time = models.DateTimeField(u"结束时间")
    ad = models.ForeignKey(Ads)
    cpm_num1 = models.IntegerField(default=0)
    cpc_num1 = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.start_time)[0:10]

    class Meta:
        verbose_name_plural = "广告投放计划任务"
        verbose_name = "计划任务"


class Continent(models.Model):
    name = models.CharField(max_length=256)
    order = models.IntegerField()
    file = models.ImageField(u'Image')
    pay_status = models.SmallIntegerField(
        u"状态", default=2, db_index=True,
        choices=PRESENT_STATE_CHOICES,
        help_text=u"管理员不能直接置退款, 添加人工退款, 系统会自动核实帐目退款")
    ctime = models.DateTimeField(u"创建时间", auto_now_add=True, db_index=True)
    utime = models.DateTimeField(u"更新时间", auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = u"大洲"
        verbose_name_plural = "大洲"

    def save(self, force_insert=False, force_update=False, using=None):
        return super(Continent, self).save(force_insert, force_update, using)


class Country(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=2,
                            help_text='ISO 3166-1 alpha-2 - two character '
                                      'country code')
    independence_day = models.DateField(blank=True, null=True)
    continent = models.ForeignKey(Continent, null=True)
    area = models.BigIntegerField(blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True,
                                   help_text='Try and enter few some more '
                                             'lines')
    architecture = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = u"国家"
        verbose_name_plural = "国家"


TYPE_CHOICES = ((1, 'Awesome'), (2, 'Good'), (3, 'Normal'), (4, 'Bad'))
TYPE_CHOICES2 = ((1, 'Hot'), (2, 'Normal'), (3, 'Cold'))
TYPE_CHOICES3 = ((1, 'Tall'), (2, 'Normal'), (3, 'Short'))


class KitchenSink(models.Model):
    name = models.CharField(max_length=64)
    help_text = models.CharField(max_length=64,
                                 help_text="Enter fully qualified name")
    multiple_in_row = models.CharField(max_length=64,
                                       help_text='Help text for multiple')
    multiple2 = models.CharField(max_length=10, blank=True)
    textfield = models.TextField(blank=True,
                                 verbose_name='Autosized textarea',
                                 help_text='Try and enter few some more lines')

    file = models.FileField(upload_to='.', blank=True)
    readonly_field = models.CharField(
        max_length=127, default='Some value here')

    date = models.DateField(blank=True, null=True)
    date_and_time = models.DateTimeField(blank=True, null=True)

    date_widget = models.DateField(blank=True, null=True)
    datetime_widget = models.DateTimeField(blank=True, null=True)

    boolean = models.BooleanField(default=True)
    boolean_with_help = models.BooleanField(
        help_text="Boolean field with help text")

    horizontal_choices = models.SmallIntegerField(choices=TYPE_CHOICES,
                                                  default=1,
                                                  help_text='Horizontal '
                                                            'choices look '
                                                            'like this')
    vertical_choices = models.SmallIntegerField(choices=TYPE_CHOICES2,
                                                default=2,
                                                help_text="Some help on "
                                                          "vertical choices")
    choices = models.SmallIntegerField(choices=TYPE_CHOICES3,
                                       default=3,
                                       help_text="Help text")
    hidden_checkbox = models.BooleanField()
    hidden_choice = models.SmallIntegerField(choices=TYPE_CHOICES3,
                                             default=2, blank=True)
    hidden_charfield = models.CharField(max_length=64, blank=True)
    hidden_charfield2 = models.CharField(max_length=64, blank=True)

    country = models.ForeignKey(Country, related_name='foreign_key_country')
    linked_foreign_key = models.ForeignKey(Country, limit_choices_to={
        'continent__name': 'Europe'}, related_name='foreign_key_linked')
    raw_id_field = models.ForeignKey(Country,
                                     help_text='Regular raw ID field',
                                     null=True, blank=True)

    enclosed1 = models.CharField(max_length=64, blank=True)
    enclosed2 = models.CharField(max_length=64, blank=True)

    def __unicode__(self):
        return self.name

# Inline model for KitchenSink


class Fridge(models.Model):
    kitchensink = models.ForeignKey(KitchenSink)
    name = models.CharField(max_length=64)
    type = models.SmallIntegerField(choices=TYPE_CHOICES3)
    description = models.TextField(blank=True)
    is_quiet = models.BooleanField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.name


# Inline model for KitchenSink
class Microwave(models.Model):
    kitchensink = models.ForeignKey(KitchenSink)
    name = models.CharField(max_length=64)
    type = models.SmallIntegerField(choices=TYPE_CHOICES3, default=2,
                                    help_text='Choose wisely')
    is_compact = models.BooleanField()

    def __unicode__(self):
        return self.name


##################################
#
# Integrations examples
#
##################################

#
# Django-mptt
# https://github.com/django-mptt/django-mptt/
#
class Category(MPTTModel):
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children')
    is_active = models.BooleanField()
    order = models.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories (django-mptt)"

    class MPTTMeta:
        order_insertion_by = ['order']

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        Category.objects.rebuild()


#
# Django-select2
# https://github.com/applegrew/django-select2
#
class City(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country)
    capital = models.BooleanField()
    area = models.BigIntegerField(blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'country')
        verbose_name = u"城市"
        verbose_name_plural = "城市"


class WysiwygEditor(models.Model):
    name = models.CharField(max_length=64)
    redactor = models.TextField(verbose_name='Redactor small', blank=True)
    redactor2 = models.TextField(verbose_name='Redactor2', blank=True)
    ckeditor = models.TextField(verbose_name='CKEditor', blank=True)

    def __unicode__(self):
        return self.name


class ReversionedItem(models.Model):
    name = models.CharField(max_length=64)
    quality = models.SmallIntegerField(choices=TYPE_CHOICES, default=1)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class ZUser(models.Model):
    uid = models.AutoField(primary_key=True)
    pnum = models.BigIntegerField(unique=True)
    pnum_md5 = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    status = models.IntegerField()
    device_id = models.CharField(unique=True, max_length=50)
    imsi = models.CharField(max_length=50)
    os_type = models.CharField(max_length=50)
    ctime = models.DateTimeField()
    register_ip = models.CharField(max_length=15)
    invite_code = models.IntegerField()
    channel = models.CharField(max_length=15, blank=True, null=True)
    ulevel = models.IntegerField()
    from_app = models.IntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'z_user'
