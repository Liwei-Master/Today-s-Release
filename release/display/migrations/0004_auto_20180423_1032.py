# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-23 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0003_auto_20180423_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='source',
            new_name='item_source',
        ),
    ]
