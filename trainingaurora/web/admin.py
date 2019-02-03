from django.contrib import admin
from .models import *
from django.utils.translation import ugettext as _ 
#from django.contrib.auth.models import Group , User


# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display = ('name' , 'population')
    search_fields = ('name' , 'population')


class TourAdmin(admin.ModelAdmin):
    list_display = ('name' , 'destination')
    search_fields = ('name' , 'destination')



admin.site.register(City , CityAdmin)
admin.site.register(Tour , TourAdmin)

#admin.site.register(Destination)