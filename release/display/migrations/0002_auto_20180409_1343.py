# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-09 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='collect_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]