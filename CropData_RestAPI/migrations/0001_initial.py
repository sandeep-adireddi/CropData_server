# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-14 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseHolds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number_of_members', models.IntegerField()),
                ('Monthly_income', models.IntegerField()),
            ],
        ),
    ]
