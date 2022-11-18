from django.shortcuts import render
from rest_framework import generics,status
from .models import PublisherModel

from rest_framework.response import Response
from publisher.serializers.publisher_serializer import PublisherSerializer



class PublisherListview(generics.ListCreateAPIView):
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializer

class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializer

