from django.conf import settings
from django.db import models
from django.utils import timezone


class Rehearsal(models.Model):
    start_date = models.DateTimeField(primary_key=True)
    # place =
    end_time = models.DateTimeField()
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)
    description = models.TextField()
