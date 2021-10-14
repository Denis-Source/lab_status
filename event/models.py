from django.db import models
from django.utils import timezone
from part.models import Part


class Event(models.Model):
    title = models.CharField(max_length=32, unique=True)
    part = models.ForeignKey(Part, related_name="parts", on_delete=models.CASCADE)
    camera_name = models.CharField(max_length=16, null=True, blank=True)

    time = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    is_authorised = models.BooleanField(default=False)

    image = models.ImageField(upload_to="event/images/", null=True, blank=True)
    is_video_recorded = models.BooleanField(default=False)
    video = models.FileField(upload_to="event/videos/", null=True, blank=True)
