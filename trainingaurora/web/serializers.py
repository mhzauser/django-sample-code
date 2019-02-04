from rest_framework import serializers
from .models import City , Tour 
import json


#class Destserializer(serializers.RelatedField):
#    
#    dest = serializers.SlugRelatedField(
#        many = True,
#        read_only= True,
#        slug_field='name'
#    )
#
#    class Meta:
#        model = Destination
#        fields = ('id' , 'name' , 'dest')
#
#    def create(self , validated_data):
#       dest_data = validated_data.pop('dest')
#        dest = Destination.objects.create(**validated_data)
#        Cityserializer.objects.create(population=dest , **dest_data)

class Cityserializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id' , 'name' , 'population')


class Tourserialzier(serializers.ModelSerializer):
    
    destination = Cityserializer(
        many=False,
        )

    class Meta:
        model = Tour
        fields = ('id' , 'name' , 'destination')
    
    def create(self , validation_data):
        tour_data = validation_data.pop('destination')
        
        tour_create = Tour.objects.create(
            **validation_data
            )
        
        City.objects.create(
            destination=tour_create,
            **validation_data
            )
        #city_detail = City.objects.get_or_create(name=[{'destination': 'name'}] , population=[{'destination' : 'population'}])
        #, population=
        return tour_create



#class TourSerializerPost(serializers.ModelSerializer):
#
#    
#    class Meta:
#        model = Tour
#        fields = ('id' , 'name' , 'destination')    