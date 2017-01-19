#!/usr/bin/env python
# coding=utf-8
import xadmin
from xadmin import views
from django.conf import settings
from models import *
from xadmin.layout import *
from django.contrib import admin, messages

from xadmin.plugins.inline import Inline

from .models import Country, Continent, KitchenSink, Category, City, \
    Microwave, Fridge, WysiwygEditor, ReversionedItem, TimeIntervals, AD_STATUS_CHOICES, ZUser


class TimeIntervalsInline(object):
    model = TimeIntervals
    extra = 0
    verbose_name_plural = 'TimeIntervals'


class AdsAdmin(object):
    model_icon = 'fa fa-beer'

    search_fields = ('name', 'code')
    list_display = ('id', 'name', 'code', 'start_time', 'end_time', 'status')

    inlines = (TimeIntervalsInline,)

    actions = ("enable", "disable")

    def enable(self, request, queryset):
        queryset.update(status=1)
        messages.success(request,
                         '{0}上线成功: {1}'.format("", ""))
    enable.short_description = "上线"

    def disable(self, request, queryset):
        queryset.update(status=3)
        messages.success(request,
                         '{0}下线成功: {1}'.format("", ""))
    disable.short_description = "下线"


xadmin.site.register(Ads, AdsAdmin)


class CountryInline(object):
    model = Country
    fields = ('name', 'code', 'population',)
    extra = 1
    verbose_name_plural = 'Countries (Sortable example)'


class ContinentAdmin(object):
    search_fields = ('name',)
    list_display = (
        u'id',
        'name',
        'order',
        'head_img',
        'pay_status',
        'ctime',
        'utime',
    )
    inlines = (CountryInline,)
    model_icon = 'fa fa-flask'

    def head_img(self, obj):
        res = Continent.objects.filter(id=obj.id)
        if not res:
            return "-"
        return '<img src="%s%s" alt="head img" height=40/>' % (settings.CDN_URL, res[0].file)

    head_img.short_description = u"image file"
    head_img.allow_tags = True

    actions = ("create_user_ref",)
    list_per_page = 20

xadmin.site.register(Continent, ContinentAdmin)


class CityInline(object):
    model = City
    extra = 3
    verbose_name_plural = 'Cities'


class CountryAdmin(object):
    search_fields = ('name', 'code')
    list_display = ('name', 'code', 'continent', 'independence_day')
    list_filter = ('continent',)

    inlines = (CityInline,)
    model_icon = 'fa fa-bell'

    form_layout = (
        TabHolder(
            Tab('General',
                Fieldset(None,
                         'name', 'continent', 'code', 'independence_day',
                         css_class='unsort no_title'
                         ),
                Fieldset('Statistics',
                         'area', 'population',
                         description="EnclosedInput widget examples"
                         ),
                Fieldset('Autosized textarea',
                         'description',
                         description='AutosizedTextarea widget example - adapts height '
                         'based on user input'
                         ),
                ),
            Tab('Cities',
                Fieldset('Architecture',
                         'architecture',
                         description="Tabs can contain any fieldsets and inlines"
                         ),
                Inline(City),
                ),
        ),
    )

xadmin.site.register(Country, CountryAdmin)


# Inlines for KitchenSink
class FridgeInline(object):
    model = Fridge
    extra = 1
    verbose_name_plural = 'Fridges (Tabular inline)'
    style = "table"


class MicrowaveInline(object):
    model = Microwave
    extra = 1
    verbose_name_plural = 'Microwaves (Stacked inline)'

# Kitchen sink model admin


class KitchenSinkAdmin(object):
    inlines = (FridgeInline, MicrowaveInline)
    search_fields = ['name']
    list_editable = ('boolean', )
    list_filter = ('choices', 'date', 'country')
    readonly_fields = ('readonly_field',)
    raw_id_fields = ('raw_id_field',)
    model_icon = 'fa fa-bolt'
    form_layout = (
        Main(
            Fieldset(None,
                     'name', 'help_text', 'textfield',
                     Row('multiple_in_row', 'multiple2'),
                     'file', 'readonly_field',
                     css_class='unsort no_title'
                     ),
            Fieldset("Date and time",
                     'date_widget', 'datetime_widget',
                     description='Improved date/time widgets (SuitDateWidget, '
                     'SuitSplitDateTimeWidget) . Uses original JS.'
                     ),
            Fieldset("Foreign key relations",
                     'country', 'linked_foreign_key', 'raw_id_field',
                     description="Original select and linked select feature"
                     ),
            Fieldset("EnclosedInput widget",
                     PrependedText('enclosed1', 'G'), 'enclosed2',
                     description='Supports Twitter Bootstrap prepended, '
                     'appended inputs',
                     ),
            Fieldset("Boolean and choices",
                     'boolean', 'boolean_with_help', 'choices',
                     'horizontal_choices', 'vertical_choices'
                     ),
        ),
        Side(
            Fieldset('Collapsed settings',
                     'hidden_checkbox', 'hidden_choice'
                     ),
            Fieldset('And one more collapsable',
                     'hidden_charfield', 'hidden_charfield2'
                     ),
        )
    )

    list_display = (
        'name', 'help_text', 'choices', 'horizontal_choices', 'boolean')

xadmin.site.register(KitchenSink, KitchenSinkAdmin)


class ZUserAdmin(object):
    model_icon = 'fa fa-fire'

    search_fields = ('uid', 'pnum')
    list_editable = ("pnum", )
    list_display = ("uid", "pnum", "pnum_md5", "password", "status", "device_id", "imsi", "os_type", "ctime", "register_ip", "invite_code", "channel", "ulevel", "from_app", "update_time")

    actions = ("enable", "disable")
    aggregate_fields = {"status": "sum"}

    def enable(self, request, queryset):
        queryset.update(status=1)
        messages.success(request,
                         '{0}上线成功: {1}'.format("", ""))
    enable.short_description = "上线"

    def disable(self, request, queryset):
        queryset.update(status=3)
        messages.success(request,
                         '{0}下线成功: {1}'.format("", ""))
    disable.short_description = "下线"


xadmin.site.register(ZUser, ZUserAdmin)



from django.views.generic import FormView
from xadmin.views import ModelAdminView, CommAdminView
from django.views.generic.edit import FormMixinBase
from xadmin.sites import MergeAdminMetaclass
from django.utils import six
from django.template.response import TemplateResponse

# class Metaclass(FormMixinBase, MergeAdminMetaclass):
#     pass
#     """Resolve conflito de metaclass"""

# class MyModelView(six.with_metaclass(Metaclass, ModelAdminView, FormView):
#     ""Custom admin view: Inherits two views that have metaclasses"


class MyView(CommAdminView):
    base_template = 'xadmin/base_site.html'
    # @never_cache
    def get(self, request, *_kwargs):
        context = self.get_context()
        return TemplateResponse(self.request, [
        '500.html'
        ], self.get_context(), current_app=self.admin_site.name)

xadmin.site.register_view(r'^xadmin/welcome/$', MyView, name='app:MyView')

# xadmin.site.register_view(r'^myapp/myapp/add/$', MyModelView, name='myapp_myapp_add')
