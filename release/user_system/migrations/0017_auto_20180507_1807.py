# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-07 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_system', '0016_auto_20180506_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='item_title',
            field=models.CharField(default='news', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='label',
            field=models.CharField(default='最喜欢', max_length=10, unique=True),
        ),
    ]
