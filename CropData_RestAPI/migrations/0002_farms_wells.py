# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-14 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CropData_RestAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TotalArea', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Wells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Depth', models.DecimalField(decimal_places=5, max_digits=10)),
                ('Average_yield', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
    ]
