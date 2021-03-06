# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-06-22 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('facility', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=100)),
                ('destiny', models.CharField(max_length=100)),
                ('pick_up_facility', models.CharField(max_length=100)),
                ('reciving_facility', models.CharField(max_length=100)),
                ('reason_for_transfer', models.CharField(max_length=100)),
                ('passenger_information', models.CharField(max_length=100)),
                ('name_and_contact_informtion', models.CharField(max_length=100)),
                ('proof_of_service', models.CharField(max_length=100)),
                ('medical_condition', models.CharField(max_length=100)),
                ('does_patient_requiere_special_equipment', models.CharField(max_length=100)),
                ('physical_condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Costumer',
        ),
    ]
