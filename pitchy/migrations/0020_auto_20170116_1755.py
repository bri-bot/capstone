# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitchy', '0019_auto_20170113_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_handle',
            field=models.CharField(max_length=20),
        ),
    ]
