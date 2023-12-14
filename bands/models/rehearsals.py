from django.contrib.auth import get_user_model
from django.db import models
from . import bands
User = get_user_model()


class Rehearsal(models.Model):
    group = models.ForeignKey(bands.Group, models.CASCADE, 'schedule')
    date = models.DateField(null=False, blank=False)
    time_start = models.TimeField(null=False, blank=False)
    time_end = models.TimeField(null=True, blank=True)

    members = models.ManyToManyField(User, 'schedule', blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.group} - {self.date} - {self.time_start}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['group', 'date', 'time_start'], name='unique_rehearsal')
        ]
        verbose_name = 'Репетиция'
        verbose_name_plural = 'Репетиции'
