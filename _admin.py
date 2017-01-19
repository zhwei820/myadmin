# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models

class ContinentAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'name',
        'order',
        'file',
        'pay_status',
        'ctime',
        'utime',
    )
    list_filter = ('ctime', 'utime')
    search_fields = ('name',)


class CountryAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'name',
        'code',
        'independence_day',
        'continent',
        'area',
        'population',
        'order',
        'description',
        'architecture',
    )
    list_filter = ('independence_day', 'continent')
    search_fields = ('name',)


class KitchenSinkAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'name',
        'help_text',
        'multiple_in_row',
        'multiple2',
        'textfield',
        'file',
        'readonly_field',
        'date',
        'date_and_time',
        'date_widget',
        'datetime_widget',
        'boolean',
        'boolean_with_help',
        'horizontal_choices',
        'vertical_choices',
        'choices',
        'hidden_checkbox',
        'hidden_choice',
        'hidden_charfield',
        'hidden_charfield2',
        'country',
        'linked_foreign_key',
        'raw_id_field',
        'enclosed1',
        'enclosed2',
    )
    list_filter = (
        'date',
        'date_and_time',
        'date_widget',
        'datetime_widget',
        'boolean',
        'boolean_with_help',
        'hidden_checkbox',
        'country',
        'linked_foreign_key',
        'raw_id_field',
    )
    search_fields = ('name',)


class FridgeAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'kitchensink',
        'name',
        'type',
        'description',
        'is_quiet',
        'order',
    )
    list_filter = ('kitchensink', 'is_quiet')
    search_fields = ('name',)


class MicrowaveAdmin(admin.ModelAdmin):

    list_display = (u'id', 'kitchensink', 'name', 'type', 'is_compact')
    list_filter = ('kitchensink', 'is_compact')
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'name',
        'slug',
        'parent',
        'is_active',
        'order',
        u'lft',
        u'rght',
        u'tree_id',
        u'level',
    )
    list_filter = ('parent', 'is_active')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}


class CityAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'name',
        'country',
        'capital',
        'area',
        'population',
    )
    list_filter = ('country', 'capital')
    search_fields = ('name',)


class WysiwygEditorAdmin(admin.ModelAdmin):

    list_display = (u'id', 'name', 'redactor', 'redactor2', 'ckeditor')
    search_fields = ('name',)


class ReversionedItemAdmin(admin.ModelAdmin):

    list_display = (u'id', 'name', 'quality', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Continent, ContinentAdmin)
_register(models.Country, CountryAdmin)
_register(models.KitchenSink, KitchenSinkAdmin)
_register(models.Fridge, FridgeAdmin)
_register(models.Microwave, MicrowaveAdmin)
_register(models.Category, CategoryAdmin)
_register(models.City, CityAdmin)
_register(models.WysiwygEditor, WysiwygEditorAdmin)
_register(models.ReversionedItem, ReversionedItemAdmin)
