# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-18 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170817_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='shift_availability',
            field=models.ManyToManyField(blank=True, null=True, to='core.Shift'),
        ),
    ]
