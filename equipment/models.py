from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from band.models import MusicBand


class TypeOfEquipment(models.Model):
    name = models.CharField(max_length=100, primary_key=True, default='Неизвестно')

    def __str__(self):
        return self.name


class Equipment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='equipment_owner')
    name = models.CharField(max_length=200)
    type = models.ForeignKey(TypeOfEquipment, on_delete=models.SET_DEFAULT, default='Неизвестно')

    STATE_CHOICES = (
        ('1', 'Активен'),
        ('0', 'Списан'),
    )
    state = models.CharField(max_length=5, choices=STATE_CHOICES, default='1')
    description = models.TextField(blank=True, null=True, max_length=1000)
    register_date = models.DateTimeField(auto_created=True)
    music_band = models.ForeignKey(MusicBand, related_name='music_band',
                                   on_delete=models.SET_NULL,
                                   null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'name'], name='unique_equipment')
        ]
        ordering = ('-register_date',)

    def __str__(self):
        return self.name

