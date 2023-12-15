from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Rehearsal(models.Model):
    group = models.ForeignKey('bands.Group', models.CASCADE, 'rehearsals_groups',
                              verbose_name='Музыкальная группа',)
    date = models.DateField(null=False, blank=False, verbose_name='Дата',)
    time_start = models.TimeField(null=False, blank=False, verbose_name='Время начала',)
    time_end = models.TimeField(null=True, blank=True, verbose_name='Время окончания',)

    members = models.ManyToManyField(User, 'rehearsals_users',
                                    verbose_name='Участники',)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.group} - {self.date} - {self.time_start}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['group', 'date', 'time_start'],
                                    name='unique_rehearsal')
        ]
        verbose_name = 'Репетиция'
        verbose_name_plural = 'Репетиции'
