from rest_framework.serializers import ModelSerializer
from message.models import Message
from lab_user.serializers import LabUserSerializer


class MessageSerializer(ModelSerializer):
    author = LabUserSerializer()

    class Meta:
        model = Message
        fields = [
            "id", "body", "author", "time"
        ]


class MessageCreateSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = [
            "body",
        ]
