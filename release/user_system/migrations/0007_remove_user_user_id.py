# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-26 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_system', '0006_user_has_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
    ]
