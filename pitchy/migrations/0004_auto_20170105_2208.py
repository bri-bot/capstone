# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitchy', '0003_friendship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_handle',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
