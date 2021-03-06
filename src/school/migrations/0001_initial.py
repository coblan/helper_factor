# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-22 02:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='\u73ed\u7ea7\u540d\u79f0')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='\u5b66\u6821\u540d')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='\u59d3\u540d')),
                ('age', models.CharField(blank=True, max_length=20, verbose_name='\u5e74\u9f84')),
                ('gender', models.CharField(blank=True, choices=[('male', '\u7537'), ('female', '\u5973')], max_length=10, verbose_name='\u6027\u522b')),
                ('head', models.CharField(blank=True, max_length=500, verbose_name='\u5934\u50cf')),
                ('lclass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.LClass', verbose_name='\u73ed\u7ea7')),
            ],
        ),
    ]
