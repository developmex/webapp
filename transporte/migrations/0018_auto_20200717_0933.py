# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-07-17 09:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0017_order_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cutomer',
            new_name='customer',
        ),
    ]
