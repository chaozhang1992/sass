# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-12-15 21:03
from __future__ import unicode_literals

from django.db import migrations
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='bucket',
            field= models.CharField(max_length=128, verbose_name='cos桶')
        ),
        migrations.AddField(
            model_name='project',
            name='region',
            field= models.CharField(max_length=32, verbose_name='cos区域')
        ),
    ]
