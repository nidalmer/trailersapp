# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-06 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20160906_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trailer',
            name='number',
        ),
        migrations.AddField(
            model_name='trailer',
            name='trailer_title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
