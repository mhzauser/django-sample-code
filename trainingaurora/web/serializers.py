from rest_framework import serializers
from .models import City , Tour 



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

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id' , 'name' , 'population')

# @mohandeath : TourSerializer ! not Tourserializer (typo)
class TourSerialzier(serializers.ModelSerializer):
    
    destination = CitySerializer(
        many=False,
        )

    class Meta:
        model = Tour
        fields = ('id' , 'name' , 'destination')
    
#    def create(self , validated_data):
#        #pay attention to the wright NAMINGs!
#        #we pop destination_data from the posted data in order to create the city objects first
#        destination_data = validated_data.pop('destination')
#        dest = City.objects.create(**destination_data)
#        tour = Tour.objects.create(destination =dest ,**validated_data)
#        return tour
        
        
        
        
        
        
        
class TourSerializerPost(serializers.ModelSerializer):

    
    class Meta:
        model = Tour
        fields = ('id' , 'name' , 'destination')    
