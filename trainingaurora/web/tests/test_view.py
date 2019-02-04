import json
from django.test import TestCase , Client
#from .models import City , Tour
from .views import Tourviewset , Cityviewset
from rest_framework import status
from rest_framework.test import APIRequestFactory , APITestCase


factory = APIRequestFactory()
client = Client(SERVER_NAME='localhost')



#view test 
class CityApiTestCase(APITestCase):
    
    def setUp(self):
        request = factory.post('/app/city' , )
            

    



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



#model test 

class CityModelTestCase(TestCase):

    def setUp(self):
        City.objects.create(
            name='mamadAbad' , population=1969
        )
        City.objects.create(
            name='berlin' , population=43452300
        )
    
    def test_city_objects(self):
        city_mamadAbad = City.objects.get(name='mamadAba')
        city_berlin = City.objects.get(name='berlin')






#class TourTestCase(TestCase):



