import json
from django.test import TestCase , Client
from ..models import City , Tour

    



class TourModelTestCase(TestCase):

    def setUp(self):
        self.cityone = City.objects.create(
            name = 'cityonefortourtest' , population=1212121
            )
        self.citytwo = City.objects.create(
            name = 'citytwofortourtest' , population=9988999
        )
        self.tourone = Tour.objects.create(
            name = 'touronetesting' , destination = self.cityone
        )
        self.tourtwo = Tour.objects.create(
            name = 'tourtwotesting' , destination = self.citytwo
        )



    def test_select_tour(self):
        tour_one = Tour.objects.get(name='touronetesting')
        tour_two = Tour.objects.get(name='tourtwotesting')


        self.assertEqual(
            tour_one.name , 'touronetesting'
        )
        self.assertEqual(
            tour_two.name , 'tourtwotesting'
        )



#model test 

class CityModelTestCase(TestCase):


    def setUp(self):
        self.cityshahryek = City.objects.create(
            name='shahryek' , population=1969
        )
        self.berlin = City.objects.create(
            name='berlin' , population=43452300
        )
    def test_selectcity(self):
        city_shahryek = City.objects.get(name='shahryek')
        
        city_berlin = City.objects.get(name='berlin')

        self.assertEqual(
            city_shahryek.name , 'shahryek'
        )
        self.assertEqual(
            city_berlin.name , 'berlin'
        )







#class TourTestCase(TestCase):



