import datetime

from django.db import models
from django.conf import settings


class MusicBand(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    register_date = models.DateField(auto_created=True, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

