from rest_framework.serializers import ModelSerializer
from lab_user.models import LabUser


class LabUserSerializer(ModelSerializer):
    class Meta:
        model = LabUser
        fields = [
            "username", "first_name", "last_name", "email", "image", "status", "position", "bio",
            "last_time_status_changed"
        ]


class LabUserConfidentialSerializer(ModelSerializer):
    class Meta:
        model = LabUser
        fields = [
            "username", "first_name", "last_name", "email", "image", "status", "position", "bio", "key_card_hash",
            "pin_code_hash", "telegram_id", "last_time_status_changed", "date_joined", "is_superuser", "last_login"
        ]
