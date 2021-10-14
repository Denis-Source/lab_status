from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class LabUser(AbstractUser):
    position = models.CharField(max_length=16, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    key_card_hash = models.CharField(max_length=32, blank=True, null=True)
    pin_code_hash = models.CharField(max_length=32, blank=True, null=True)
    telegram_id = models.CharField(max_length=64, blank=True, null=True)

    last_time_status_changed = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False, blank=True, null=True)

    image = models.ImageField(upload_to="lab_user/", blank=True, null=True)

    def change_status(self, new_status=True):
        self.last_time = timezone.now()
        self.status = new_status
        self.save()