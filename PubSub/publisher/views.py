from django.shortcuts import render
from rest_framework import generics,status
from .models import PublisherModel
from rest_framework.views import APIView
from rest_framework.response import Response
from publisher.serializers.publisher_serializer import PublisherSerializer

class PublisherCreate(APIView):
    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PublisherListview(generics.ListCreateAPIView):
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializer

class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializer

