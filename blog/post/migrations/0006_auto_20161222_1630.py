# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20161222_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
