from django.db import models
from django.utils.translation import ugettext_lazy as _


#class Destination(models.Model):
#
#    name = models.CharField(
#        max_length=50
#        )
#
#    dest = models.ManyToManyField(
#        verbose_name=_('dest'),
#        help_text=_('desitnation tour to city table'),
#       City
#        )
#
#   def __str__(self):
#        return self.name
#
#
#    class Meta:
#        verbose_name=_("destination")
#        verbose_name_plural=_("destinations")

class City(models.Model):
    name = models.CharField(
        max_length=500
        )
    population = models.BigIntegerField(
        blank=True, 
        null=True
        )

    def get_objects(self):
        return self.name + 'is created with' + self.population + 'population'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name=_('city')
        verbose_name_plural=_('cities')
    




class Tour(models.Model):
    
    name = models.CharField(
        max_length=500
        )

    destination = models.ForeignKey(
        City,
        verbose_name=_('destination'),
        help_text=_('desitnation tour to destination table'),
        related_name='destination_goal', #naming for related_name is wrong, it should be sth like get_tours or sth
        on_delete=models.CASCADE,
        blank=True,
        null=True
        )

    def __str__(self):
        return self.name

    def get_objects(self):
        return self.name + 'created with' + str(self.destination)

    class Meta:
        verbose_name=_("tour")
        verbose_name_plural=_("tours")
