from rest_framework.serializers import ModelSerializer, StringRelatedField
from event.models import Event


class EventSerializer(ModelSerializer):
    part = StringRelatedField()

    class Meta:
        model = Event
        fields = [
            "title", "part", "camera_name", "time", "status", "is_authorised", "image",
            "is_video_recorded", "video"
        ]
