# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-15 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CropData_RestAPI', '0006_auto_20170815_0839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Crop', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HouseHold_Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Relation', models.CharField(max_length=50, null=True)),
                ('Age', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seasons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Season', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='crop',
            name='Farm',
        ),
        migrations.RemoveField(
            model_name='crop',
            name='Season',
        ),
        migrations.RemoveField(
            model_name='households_members',
            name='HouseHold',
        ),
        migrations.RemoveField(
            model_name='well_yield',
            name='Farm',
        ),
        migrations.AddField(
            model_name='well_yield',
            name='Well',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CropData_RestAPI.Wells'),
        ),
        migrations.AlterField(
            model_name='extent',
            name='Crop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CropData_RestAPI.Crops'),
        ),
        migrations.AlterField(
            model_name='extent',
            name='Extent',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='farm_audio',
            name='Audio',
            field=models.FileField(upload_to='Farm_audio'),
        ),
        migrations.AlterField(
            model_name='farms',
            name='TotalArea',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='household_audio',
            name='Audio',
            field=models.FileField(upload_to='HouseHold_audio'),
        ),
        migrations.AlterField(
            model_name='households',
            name='Monthly_income',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='households',
            name='Number_of_members',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='well_yield',
            name='Yield',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='wells',
            name='Average_yield',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='wells',
            name='Depth',
            field=models.FloatField(null=True),
        ),
        migrations.DeleteModel(
            name='Crop',
        ),
        migrations.DeleteModel(
            name='HouseHolds_members',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
        migrations.AddField(
            model_name='household_members',
            name='HouseHold',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CropData_RestAPI.HouseHolds'),
        ),
        migrations.AddField(
            model_name='crops',
            name='Farm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CropData_RestAPI.Farms'),
        ),
        migrations.AddField(
            model_name='crops',
            name='Season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CropData_RestAPI.Seasons'),
        ),
    ]