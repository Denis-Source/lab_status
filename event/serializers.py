from rest_framework.serializers import ModelSerializer, StringRelatedField
from event.models import Event


class EventSerializer(ModelSerializer):
    part = StringRelatedField()

    class Meta:
        model = Event
        fields = [
            "id", "title", "part", "level", "camera_name", "time", "is_authorised", "image",
            "is_video_recorded", "video"
        ]


class EventCreateSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "title", "part", "level", "source", "camera_name", "is_authorised", "image"
        ]


class EventAddVideoSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "video"
        ]
