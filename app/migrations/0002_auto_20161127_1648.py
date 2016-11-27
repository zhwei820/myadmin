# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-27 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ads',
            options={'ordering': ['name'], 'verbose_name': '\u5e7f\u544a', 'verbose_name_plural': 'Ads'},
        ),
        migrations.AlterModelOptions(
            name='timeintervals',
            options={'verbose_name': '\u8ba1\u5212\u4efb\u52a1', 'verbose_name_plural': '\u5e7f\u544a\u6295\u653e\u8ba1\u5212\u4efb\u52a1'},
        ),
        migrations.AddField(
            model_name='ads',
            name='status',
            field=models.SmallIntegerField(choices=[(0, b'\xe6\x9c\xaa\xe4\xb8\x8a\xe7\xba\xbf'), (1, b'\xe4\xb8\x8a\xe7\xba\xbf'), (2, b'\xe6\x9a\x82\xe7\xbc\x93\xe4\xb8\x8a\xe7\xba\xbf'), (3, b'\xe4\xb8\x8b\xe7\xba\xbf')], db_index=True, default=0, help_text='\u5e7f\u544a\u72b6\u6001', verbose_name='\u72b6\u6001'),
        ),
    ]