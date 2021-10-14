from django.utils import timezone
from django.db import models
from lab_user.models import LabUser


class Message(models.Model):
    body = models.TextField()
    author = models.ForeignKey(LabUser, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
