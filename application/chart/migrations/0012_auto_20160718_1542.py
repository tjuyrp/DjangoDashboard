# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0011_top4posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top4posts',
            name='link',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='top4posts',
            name='message',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='top4posts',
            name='pic',
            field=models.CharField(max_length=400),
        ),
    ]
