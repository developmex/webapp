# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-08-04 12:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0002_invoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='customer',
            new_name='passenger',
        ),
        migrations.AddField(
            model_name='invoice',
            name='miles',
            field=models.CharField(default=datetime.datetime(2020, 8, 4, 12, 27, 11, 378886, tzinfo=utc), max_length=6),
            preserve_default=False,
        ),
    ]
