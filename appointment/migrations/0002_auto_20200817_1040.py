# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-08-17 10:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='appointment_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='appointments',
            name='pick_up_date',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
        migrations.AddField(
            model_name='appointments',
            name='pick_up_time',
            field=models.TimeField(null=True),
        ),
    ]
