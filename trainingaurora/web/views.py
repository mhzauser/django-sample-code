from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import City , Tour 
from .serializers import CitySerializer , TourSerialzier , TourSerializerPost
from rest_framework_docs.api_docs import ApiDocumentation
#TourSerializerPost
# Create your views here.



#class Destinationviewset(Destinationmixin, viewsets.ModelViewSet):
#    pass

class Cityviewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    



class Tourviewset(viewsets.ModelViewSet):

    queryset = Tour.objects.all()

    def get_serializer_class(self):
        # @mohandeath : you need to read more about modelviewset use actions instead of request methods in case of modelviewset!!
        if self.action == 'create':
            return TourSerializerPost
        elif self.action == 'list': #put a goddamn ELSE otherwise all conditions may be executed!!
            return  TourSerialzier
        ## return self.serializer_class >> WHYY ???????


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

