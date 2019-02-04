import json
from django.test import TestCase , Client
from ..models import City , Tour

    



class TourModelTestCase(TestCase):

    def setUp(self):
        cityone = City.objects.create(
            name = 'cityonefortourtest' , population=1212121
            )
        citytwo = City.objects.create(
            name = 'citytwofortourtest' , population=9988999
        )
        self.tourone = Tour.objects.create(
            name = 'touronetesting' , destination = cityone
        )
        self.tourtwo = Tour.objects.create(
            name = 'tourtwotesting' , destination = citytwo
        )



    def test_tour_objects(self):
        tour_one = Tour.objects.get(name='touronetesting')
        tour_two = Tour.objects.get(name='tourtwotesting')

        self.assertEqual(
            tour_one.get_objects() , "tour touronetesting created ..."
        )
        self.assertEqual(
            tour_two.get_objects() , "tour tourtwotesting created ..."
        )



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

        self.assertEqual(
            city_mamadAbad.get_objects() , "city mamamdabad created ..."
        )
        self.assertEqual(
            city_berlin.get_objects() , "city berlin created..."
        )







#class TourTestCase(TestCase):



