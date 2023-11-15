from django.db import models
from django.conf import settings
from app_auth.models import CustomUser


class MusicBand(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    register_date = models.DateField(auto_now=True)
    url = models.URLField(null=True, blank=True)
    leader = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='leader',
                               null=True, blank=True)
    deputy = models.ManyToManyField(CustomUser, related_name='music_deputies', blank=True)
    members = models.ManyToManyField(CustomUser, related_name='music_members', blank=True)

    def __str__(self):
        return self.name

