# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cctv', '0009_auto_20180913_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='camera_info',
            field=models.CharField(default='', max_length=200),
        ),
    ]