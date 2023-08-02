from .models import AboutUs, ContactInformation
from .serializers import AboutUsSerializer, ContactInformationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class AboutUsView(APIView):
    def get(self, request, format=None):
        about_us = AboutUs.objects.first()
        serializer = AboutUsSerializer(about_us)
        return Response(serializer.data)
    
    def put(self, request, format=None):
        about_us = AboutUs.objects.first()
        serializer = AboutUsSerializer(about_us, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ContactInformationView(APIView):
    def get(self, request, format=None):
        contact_information = ContactInformation.objects.first()
        serializer = ContactInformationSerializer(contact_information)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ContactInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)