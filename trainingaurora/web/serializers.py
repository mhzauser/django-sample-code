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
    
#    def create(self , validation_data):
#        tour_data = validation_data.pop('destination')
#       city_detail = City.object.get().filter(name=[{'destination': 'name'}])
#        return Tour.objects.create(destination=city_detail , **validation_data)
#
class TourSerializerPost(serializers.ModelSerializer):

    
    class Meta:
        model = Tour
        fields = ('id' , 'name' , 'destination')    