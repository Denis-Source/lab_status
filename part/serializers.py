from rest_framework.serializers import ModelSerializer
from part.models import Part


class PartSerializer(ModelSerializer):
    class Meta:
        model = Part
        fields = [
            "name", "last_time", "hash_value", "status", "auto", "image_pos", "image_neg", "phrase_pos", "phrase_neg"
        ]
