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



    def test_select_tour(self):
        tour_one = Tour.objects.get(name='touronetesting')
        tour_two = Tour.objects.get(name='tourtwotesting')

        self.assertEqual(
            tour_one.select_tour() , "tour touronetesting created ..."
        )
        self.assertEqual(
            tour_two.select_tour() , "tour tourtwotesting created ..."
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
    
    def test_select_city(self):
        city_mamadAbad = City.objects.filter(name='mamadAbad')
        city_berlin = City.objects.filter(name='berlin')

        self.assertEqual(
            city_mamadAbad.select_city() , "city mamamdabad created ..."
        )
        self.assertEqual(
            city_berlin.select_city() , "city berlin created..."
        )







#class TourTestCase(TestCase):



