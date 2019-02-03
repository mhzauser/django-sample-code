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
        
        )

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
        related_name='destination_goal', 
        on_delete=models.CASCADE,
        blank=True,
        null=True
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name=_("tour")
        verbose_name_plural=_("tours")
