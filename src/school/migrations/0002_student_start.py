# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-22 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='start',
            field=models.DateField(blank=True, null=True, verbose_name='\u5165\u5b66\u65e5\u671f'),
        ),
    ]