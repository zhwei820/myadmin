# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-07 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoJob',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('next_run_time', models.DateTimeField(db_index=True)),
                ('job_state', models.BinaryField()),
            ],
            options={
                'ordering': ('next_run_time',),
            },
        ),
    ]
