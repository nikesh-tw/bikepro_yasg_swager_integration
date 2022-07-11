import json
import base64
from urllib import response
from django.shortcuts import render
from rest_framework import status

# Create your views here.
from .models import BikeDetail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from bike_app.serializers import BikeDetailSerializer,BikeDetailDataSerializer, decode_bike_number

class BikeDetailView(APIView):
    serialzer_class = BikeDetailSerializer

    def post(self, request):
        try:
            serializer = BikeDetailSerializer(data=request.data) #1
            if serializer.is_valid():
                result, bike_num = decode_bike_number(request.data.get('bike_number'))
                obj = BikeDetail.objects.filter(bike_number = bike_num).last()
                ser = BikeDetailDataSerializer(obj) #2
                return Response({'result':True,'message':'success','data':ser.data}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


