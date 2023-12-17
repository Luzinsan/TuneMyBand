from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from common.models.mixins import InfoMixin
from bands.managers.groups import GroupManager

User = get_user_model()


class Group(InfoMixin):
    band = models.ForeignKey(
        'Band', models.RESTRICT, 'groups',
        verbose_name='Музыкальная группа',
    )
    name = models.CharField('Название', max_length=255,)
    manager = models.ForeignKey(
        'Participant', models.RESTRICT, 'groups_managers',
        verbose_name='Менеджер',
    )
    members = models.ManyToManyField(
        'Participant', 'groups_members', verbose_name='Участники группы',
        blank=True, through='Member',
    )

    objects = GroupManager()

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Member(models.Model):
    group = models.ForeignKey(
        'Group', models.CASCADE, 'members_info',
    )
    participant = models.ForeignKey(
        'Participant', models.CASCADE, 'groups_info',
    )
    date_joined = models.DateField('Date joined', default=timezone.now)

    class Meta:
        verbose_name = 'Участник группы'
        verbose_name_plural = 'Участники групп'
        ordering = ('-date_joined',)
        unique_together = (('group', 'participant'),)

    def __str__(self):
        return f'Участник коллектива {self.participant}'
