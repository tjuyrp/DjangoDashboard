# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0014_topposts_bi_topposts_pvn_topposts_rol_topposts_rw_topposts_we_topposts_wh'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_BI',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('Other', models.IntegerField()),
                ('Direct', models.IntegerField()),
                ('Email', models.IntegerField()),
                ('Organic_Search', models.IntegerField()),
                ('Paid_Search', models.IntegerField()),
                ('Referral', models.IntegerField()),
                ('Social', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users_MH',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('Other', models.IntegerField()),
                ('Direct', models.IntegerField()),
                ('Email', models.IntegerField()),
                ('Organic_Search', models.IntegerField()),
                ('Paid_Search', models.IntegerField()),
                ('Referral', models.IntegerField()),
                ('Social', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users_PVN',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('Other', models.IntegerField()),
                ('Direct', models.IntegerField()),
                ('Email', models.IntegerField()),
                ('Organic_Search', models.IntegerField()),
                ('Paid_Search', models.IntegerField()),
                ('Referral', models.IntegerField()),
                ('Social', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users_ROL',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('Other', models.IntegerField()),
                ('Direct', models.IntegerField()),
                ('Email', models.IntegerField()),
                ('Organic_Search', models.IntegerField()),
                ('Paid_Search', models.IntegerField()),
                ('Referral', models.IntegerField()),
                ('Social', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users_RW',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('Other', models.IntegerField()),
                ('Direct', models.IntegerField()),
                ('Email', models.IntegerField()),
                ('Organic_Search', models.IntegerField()),
                ('Paid_Search', models.IntegerField()),
                ('Referral', models.IntegerField()),
                ('Social', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users_WE',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('Other', models.IntegerField()),
                ('Direct', models.IntegerField()),
                ('Email', models.IntegerField()),
                ('Organic_Search', models.IntegerField()),
                ('Paid_Search', models.IntegerField()),
                ('Referral', models.IntegerField()),
                ('Social', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users_WH',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('Other', models.IntegerField()),
                ('Direct', models.IntegerField()),
                ('Email', models.IntegerField()),
                ('Organic_Search', models.IntegerField()),
                ('Paid_Search', models.IntegerField()),
                ('Referral', models.IntegerField()),
                ('Social', models.IntegerField()),
            ],
        ),
    ]
