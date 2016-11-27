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
    Microwave, Fridge, WysiwygEditor, ReversionedItem, TimeIntervals, AD_STATUS_CHOICES


class TimeIntervalsInline(object):
    model = TimeIntervals
    extra = 0
    verbose_name_plural = 'TimeIntervals'


class AdsAdmin(object):
    search_fields = ('name', 'code')
    list_display = ('id', 'name', 'code', 'start_time', 'end_time', 'status')

    inlines = (TimeIntervalsInline,)
    model_icon = 'flag'

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
    model_icon = 'globe'

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
    model_icon = 'flag'

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
    model_icon = 'briefcase'
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

# Override auth admins
from django.contrib.auth.models import User
from xadmin.plugins.auth import UserAdmin, AdminPasswordChangeForm, PasswordChangeForm, ChangePasswordView, ChangeAccountPasswordView


class DemoUserAdmin(UserAdmin):
    actions = None

    def save_models(self):
        pass

    def delete_model(self):
        pass

xadmin.site.unregister(User)
xadmin.site.register(User, DemoUserAdmin)


class UnAdminPasswordChangeForm(AdminPasswordChangeForm):

    def save(self, commit=True):
        pass


class UnPasswordChangeForm(PasswordChangeForm):

    def save(self, commit=True):
        pass
xadmin.site.register(ChangePasswordView,
                     change_password_form=UnAdminPasswordChangeForm)
xadmin.site.register(ChangeAccountPasswordView,
                     change_password_form=UnPasswordChangeForm)

# Rewrite login view
xadmin.site.register(views.LoginView,
                     login_template="xadmin/views/demo_login.html"
                     )
