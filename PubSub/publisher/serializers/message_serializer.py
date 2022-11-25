from rest_framework import serializers
from publisher.models import MessageModel

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = ['id', 'serviceNamePub', 'data', 'datetimeMutation', 'url' ]
        read_only_fields = ['serviceNamePub', 'id', ]

    def create(self, validated_data):
        mm = MessageModel()
        mm.data = self.data["data"]
        mm.datetimeMutation = self.data["datetimeMutation"]
        mm.url = self.data["url"]
        mm.serviceNamePub = self.context["request"].user.username
        mm.save()
        return mm

#    def to_representation(self, instance):
#        data = super(MessageSerializer, self).to_representation(instance)
#        id = self.data["id"] 
#        return {
#            "data" : data,
#            "id" : id,
#        }
        
        
        