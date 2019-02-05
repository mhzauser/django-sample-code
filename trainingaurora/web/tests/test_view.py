import json
from django.test import TestCase , Client
#from .models import City , Tour
from ..views import Tourviewset , Cityviewset
from ..models import City , Tour
from django.urls import reverse
from rest_framework.test import APIRequestFactory



client = Client(SERVER_NAME='localhost')
    


#view test 
class CityApiTestCase(TestCase):
    
    def setUp(self):
        self.cityone = City.objects.create(
            name='apicitytestone' , population=201
        )
        self.citytwo = City.objects.create(
            name='apicitytesttwo' , population=200
        )

    def test_api_city(self):
        cityone = self.cityone
        citytwo = self.citytwo

        

class TourApiTestCase(TestCase):

# how testing for id
    def setUp(self):
        

    def test_api_tour(self):

        self.tourone = {
            "name": "Apitourtestingone",
            "destination": {
                "id": 1,
            }
        }
        self.tourtwo = {
            "name": "Apitourtestingtwo",
            "destination": {
                "id": 2,
            }
        }        

#class TourModelTestCase(TestCase):
#
#    def setUp(self):
#        self.cityone = City.objecs.create(
#            name = 'cityonefortourtest' , population=1212121
#            )
#        citytwo = City.objects.create(
#            name = 'citytwofortourtest' , population=9988999
#        )
#        Tour.objects.create(
#            name = 'touronetesting' , destination = cityone
#        )
#        Tour.objects.create(
#            name = 'tourtwotesting' , destination = citytwo
#        )
#
#
#    def test_tour_objects(self):
#        tour_one = Tour.objects.get(name='touronetesting')
#        tour_two = Tour.objects.get(name='tourtwotesting')
#
#        self.assertEqual(
#            tour_one.get_objects() , "tour_one ..."
#        )
#        self.assertEqual(
#            tour_two.get_objects() , "tour_two ..."
#        )
#



#class CityModelTestCase(TestCase):
#
#    def setUp(self):
#        City.objects.create(
#            name='mamadAbad' , population=1969
#       )
#        City.objects.create(
#           name='berlin' , population=43452300
#        )
#    
#    def test_city_objects(self):
#        city_mamadAbad = City.objects.get(name='mamadAba')
#        city_berlin = City.objects.get(name='berlin')






#class TourTestCase(TestCase):



