import json
from django.test import TestCase
#from .models import City , Tour
from ..views import Tourviewset , Cityviewset
from ..models import City , Tour
from django.urls import reverse
from rest_framework.test import APIClient , APITestCase 
    


#view test 


class TourTest(APIClient):

    def setUp(self):
        self.client = APIClient()

    def test_tour_list(self):
        response = self.client.get('/app/tour/')
        self.assertEqual(response.status_code , 200)



class CityTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        
    def test_city_list(self):
        getresponse = self.client.get('/app/city/')
        self.assertEqual(getresponse.status_code , 200)

    def test_city_post(self):
        postresponse = self.client.post('/app/city/', { 'name': 'viewtestcityone', 'population': 12314123} , format='json')
        self.assertEqual(postresponse , 201)



