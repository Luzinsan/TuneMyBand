from django.conf import settings
from django.db import models
from django.utils import timezone
from band.models import MusicBand
from accounts.models import User


class Rehearsal(models.Model):
    music_band = models.ForeignKey(MusicBand, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    place = models.CharField(max_length=150, null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    participants = models.ManyToManyField(User, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.music_band}/{self.start_date}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['music_band', 'start_date'], name='unique_rehearsal_music_band')
        ]
        verbose_name = 'Репетиция'
        verbose_name_plural = 'Репетиции'
