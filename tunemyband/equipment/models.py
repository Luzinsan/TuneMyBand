from app_auth.models import CustomUser
from django.db import models
from django.utils import timezone
from band.models import MusicBand


class Equipment(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,
                              null=True, related_name='equipment_owners')
    name = models.CharField(max_length=200)

    STATE_CHOICES = (
        ('1', 'Активен'),
        ('0', 'Списан'),
    )
    state = models.CharField(max_length=5, choices=STATE_CHOICES, default='1')
    description = models.TextField(blank=True, null=True, max_length=1000)
    register_date = models.DateTimeField(auto_now_add=True)
    music_band = models.ForeignKey(MusicBand, related_name='music_band', on_delete=models.SET_NULL,
                                   null=True, blank=True)

    class Meta:
        ordering = ('-register_date',)

    def __str__(self):
        return self.name




