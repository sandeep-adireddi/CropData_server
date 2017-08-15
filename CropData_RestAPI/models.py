from __future__ import unicode_literals

from django.contrib.gis.db import models

# Create your models here.
class HouseHolds(models.Model):
	Location  =  models.PointField(null = True,blank = False)
	Number_of_members  =  models.IntegerField()
	Monthly_income = models.IntegerField()

class Farms(models.Model):
	Location  = models.PolygonField(null = True,blank = False)
	HouseHold = models.ForeignKey(HouseHolds, on_delete = models.CASCADE, null = True)
	TotalArea = models.FloatField()

class Wells(models.Model):
	Farm = models.ForeignKey(Farms, on_delete = models.CASCADE, null = True)
	Depth = models.FloatField()
	Location = models.PointField(null = True,blank = False)
	Average_yield = models.FloatField()

class HouseHold_Photos(models.Model):
	HouseHold = models.ForeignKey(HouseHolds, on_delete = models.CASCADE, null = True)
	Image = models.ImageField(upload_to = 'HouseHold_Photos')

class Farm_Photos(models.Model):
	Farm  = models.ForeignKey(Farms, on_delete = models.CASCADE, null = True)
	Image = models.ImageField(upload_to = 'Farm_Photos')

class HouseHold_audio(models.Model):
	HouseHold = models.ForeignKey(HouseHolds, on_delete = models.CASCADE, null = True)
	Audio = models.FileField(upload_to = 'HouseHold_audio')

class Farm_audio(models.Model):
	Farm  = models.ForeignKey(Farms, on_delete = models.CASCADE)
	Audio = models.FileField(upload_to = 'Farm_audio')

class HouseHold_members(models.Model):
	HouseHold = models.ForeignKey(HouseHolds, on_delete = models.CASCADE, null = True)
	Name = models.CharField(max_length = 50)
	Relation = models.CharField(max_length = 50)
	Age = models.IntegerField()

class Well_Yield(models.Model):
	Well = models.ForeignKey(Wells, on_delete = models.CASCADE)
	Yield = models.FloatField()
	Time = models.DateTimeField(auto_now_add = True, blank = False)


class Seasons(models.Model):
	Season = models.CharField(max_length = 50)

class Crops(models.Model):
	Farm = models.ForeignKey(Farms, on_delete = models.CASCADE)
	Season = models.ForeignKey(Seasons,on_delete = models.CASCADE)
	Crop = models.CharField(max_length = 50)

class Extent(models.Model):
	Crop = models.ForeignKey(Crops,on_delete = models.CASCADE)
	Extent = models.FloatField()