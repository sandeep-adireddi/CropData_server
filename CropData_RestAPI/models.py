from __future__ import unicode_literals

from django.db import models

# Create your models here.
class HouseHolds(models.Model):
    Number_of_members=models.IntegerField()
    Monthly_income=models.IntegerField()
class Farms(models.Model):
	HouseHold=models.ForeignKey(HouseHolds, on_delete=models.CASCADE)
	TotalArea=models.FloatField()

class Wells(models.Model):
	Farm=models.ForeignKey(Farm, on_delete=models.CASCADE)
	Depth=models.FloatField()
	Average_yield=models.FloatField()

class HouseHold_Photos(models.Model):
	HouseHold=models.ForeignKey(HouseHolds, on_delete=models.CASCADE)
	Image=models.ImageField(upload_to='HouseHold_Photos')

class Farm_Photos(models.Model):
	Farm=models.ForeignKey(Farm, on_delete=models.CASCADE)
	Image=models.ImageField(upload_to='Farm_Photos')

class HouseHold_audio(models.Model):
	HouseHold=models.ForeignKey(HouseHolds, on_delete=models.CASCADE)
	Image=models.ImageField(upload_to='HouseHold_audio')

class Farm_audio(models.Model):
	HouseHolds=models.ForeignKey(HouseHolds, on_delete=models.CASCADE)
	Image=models.ImageField(upload_to='Farm_audio')

class HouseHolds_members(models.Model):
	HouseHold=models.ForeignKey(HouseHolds, on_delete=models.CASCADE)
	Name=models.CharField()
	Relation=models.CharField()
	Age=models.IntegerField()

