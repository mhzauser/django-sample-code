from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import City , Tour 
from .serializers import Cityserializer , Tourserialzier 


#from .serializers import TourSerializerPost
# Create your views here.



#class Destinationviewset(Destinationmixin, viewsets.ModelViewSet):
#    pass

class Cityviewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = Cityserializer



class Tourviewset(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = Tourserialzier

    def createtour(self ,request):
        if request.method == 'POST':
            serializer = TourSerializerPost(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'alert': 'done'})
            return Response({'alert' : 'ops!'}) 

#    def get_serializer_class(self):
#        if self.request.method == 'POST':
#            self.serializer_class = TourSerializerPost
#        if self.request.method == 'GET':
#            self.serializer_class = Tourserialzier
#        return self.serializer_class 


#    def get_queryset(self):

        
    
#    def showtourdetial(self , request):
#        if request.method == 'GET':
#            serializer = Tourserialzier()
#            return Response(serlizer.data)
#
#    def createtour(self ,request):
#        if request.method == 'POST':
#            serializer = TourSerializerPost(data=request.data)
#            if serializer.is_valid():
#                serializer.save()
#                return Response({'alert': 'done'})
#            return Response({'alert' : 'ops!'})

