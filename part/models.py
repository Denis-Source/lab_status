from django.db import models
from django.utils import timezone


class Part(models.Model):
    name = models.CharField(max_length=32, unique=True)
    last_time = models.DateTimeField(default=timezone.now)
    hash_value = models.CharField(max_length=32, blank=True, null=True)

    status = models.BooleanField(default=False)
    auto = models.BooleanField(default=True)

    image_pos = models.ImageField(upload_to="event/pos/", blank=True, null=True)
    image_neg = models.ImageField(upload_to="event/neg/", blank=True, null=True)

    def status_image(self):
        if self.status:
            return self.image_pos.url
        else:
            return self.image_neg.url

    def change_status(self):
        self.last_time = timezone.now()
        self.status = not self.status
        self.save()

    def change_auto(self, new_status):
        self.status = new_status
        self.save()

    def __str__(self):
        return self.name.capitalize()
