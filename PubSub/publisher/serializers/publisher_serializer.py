from rest_framework import serializers
from publisher.models import PublisherModel

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherModel
        fields = "__all__"

