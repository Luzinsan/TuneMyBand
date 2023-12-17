import pdb

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from common.models.mixins import InfoMixin
from bands.constants import DIRECTOR_POSITION, MANAGER_POSITION, \
    OPERATOR_POSITION

User = get_user_model()


class Band(InfoMixin):
    name = models.CharField('Название', max_length=255)
    leader = models.ForeignKey(
        User, models.RESTRICT, 'bands_leaders',
        verbose_name='Руководитель'
    )
    participants = models.ManyToManyField(
        User, 'bands_participants', verbose_name='Участник',
        blank=True, through='participant'
    )

    class Meta:
        verbose_name = 'Музыкальный коллектив'
        verbose_name_plural = 'Музыкальные коллективы'
        ordering = ('name', 'id',)

    def __str__(self):
        return f'{self.name} ({self.pk})'

    @property
    def leader_participant(self):
        obj, create = self.participants_info.get_or_create(
            position_id=DIRECTOR_POSITION, defaults={'user': self.leader, }
        )
        return obj


class Participant(models.Model):
    band = models.ForeignKey(
        'Band', models.CASCADE, 'participants_info',
    )
    user = models.ForeignKey(
        User, models.CASCADE, 'bands_info',
    )
    position = models.ForeignKey(
        'Position', models.RESTRICT, 'participants',
    )
    date_joined = models.DateField('Date joined', default=timezone.now)

    class Meta:
        verbose_name = 'Участник коллектива'
        verbose_name_plural = 'Участники коллектива'
        ordering = ('-date_joined',)
        unique_together = (('band', 'user'),)

    def __str__(self):
        return f'Участник коллектива #{self.pk} {self.user}'

    @property
    def is_leader(self):
        if self.position_id == DIRECTOR_POSITION:
            return True
        return False

    @property
    def is_manager(self):
        if self.position_id == MANAGER_POSITION:
            return True
        return False

    @property
    def is_operator(self):
        if self.position_id == OPERATOR_POSITION:
            return True
        return False
