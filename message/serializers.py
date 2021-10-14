from rest_framework.serializers import ModelSerializer, StringRelatedField
from message.models import Message

class MessageSerializer(ModelSerializer):
    author = StringRelatedField()

    class Meta:
        model = Message
        fields = [
            "id", "body", "author"
        ]
