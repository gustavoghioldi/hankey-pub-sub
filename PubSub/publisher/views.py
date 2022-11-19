import logging
from django.shortcuts import render
from rest_framework import generics
from .models import PublisherModel
from publisher.pubmodels.message_model import MessageModel
from publisher.serializers.publisher_serializer import PublisherSerializer
from publisher.serializers.message_serializer import MessageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

logger = logging.getLogger(__name__)

class IsServerPublisher(IsAuthenticated):
    def has_permission(self, request, view):
        if not request.user.is_service:
            return False
        else: 
            return bool(True)

class PublisherListview(generics.ListCreateAPIView):
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializer

class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializer

class MessageListCreateview(generics.ListCreateAPIView):
    permission_classes = (IsServerPublisher, )
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer

class MessageRetrieve(generics.RetrieveAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
