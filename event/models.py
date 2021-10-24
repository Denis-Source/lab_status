from django.db import models
from django.utils import timezone
from part.models import Part
from django.conf import settings


class Event(models.Model):
    title = models.CharField(max_length=32)
    part = models.ForeignKey(Part, related_name="parts", on_delete=models.CASCADE)
    camera_name = models.CharField(max_length=16, null=True, blank=True)

    time = models.DateTimeField(default=timezone.now)
    level = models.CharField(max_length=32)

    source = models.CharField(max_length=32)
    is_authorised = models.BooleanField(default=False)

    image_path = models.CharField(max_length=128, null=True, blank=True)
    is_video_recorded = models.BooleanField(default=False)
    video_path = models.CharField(max_length=128, null=True, blank=True)

    def get_video_url(self):
        return f"{settings.MEDIA_URL}{settings.CAMERA_FOLDER}{self.video_path}"
