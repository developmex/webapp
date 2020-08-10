# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-08-08 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='end',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='id',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='name',
            new_name='event_name',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='start',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='events',
            name='event_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]