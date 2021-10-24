from rest_framework.serializers import ModelSerializer, StringRelatedField
from event.models import Event


class EventSerializer(ModelSerializer):
    part = StringRelatedField()

    class Meta:
        model = Event
        fields = [
            "id", "title", "part", "level", "camera_name", "time", "is_authorised", "image_path",
            "is_video_recorded", "video_path"
        ]


class EventCreateSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id", "title", "part", "level", "source", "camera_name", "is_authorised", "image_path"
        ]


class EventAddVideoSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "video_path"
        ]
