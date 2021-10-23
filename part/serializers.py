from rest_framework.serializers import ModelSerializer
from part.models import Part


class PartSerializer(ModelSerializer):
    class Meta:
        model = Part
        fields = [
            "id", "name", "last_time", "hash_value", "status", "auto", "image_pos", "image_neg", "phrase_pos", "phrase_neg",
        ]


class UpdateStatusPartSerializer(ModelSerializer):
    class Meta:
        model = Part
        fields = [
            "status"
        ]


class UpdateAutoPartSerializer(ModelSerializer):
    class Meta:
        model = Part
        fields = [
            "auto"
        ]
