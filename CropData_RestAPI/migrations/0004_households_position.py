# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-15 08:12
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CropData_RestAPI', '0003_auto_20170814_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='households',
            name='position',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
