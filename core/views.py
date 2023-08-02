from .models import AboutUs
from .serializers import AboutUsSerializer
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
