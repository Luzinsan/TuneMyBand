from django.conf import settings
from django.db import models
from django.utils import timezone


class Equipment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    state = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    register_date = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    def register(self):
        self.register_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name




