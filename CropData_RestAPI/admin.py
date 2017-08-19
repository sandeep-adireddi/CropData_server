from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(HouseHolds)

admin.site.register(Farms)

admin.site.register(Wells)

admin.site.register(Seasons)


admin.site.register(Crops)
admin.site.register(Extent)


admin.site.register(Well_Yield)

admin.site.register(HouseHold_Members)

admin.site.register(HouseHold_Audio)

admin.site.register(HouseHold_Photos)

admin.site.register(Farm_Photos)
admin.site.register(Farm_Audio)

