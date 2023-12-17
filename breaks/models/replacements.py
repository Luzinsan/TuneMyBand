from django.contrib.auth import get_user_model
from django.db import models

from common.models.mixins import InfoMixin

User = get_user_model()


class GroupInfo(models.Model):
    group = models.OneToOneField(
        'bands.Group', models.CASCADE, related_name='breaks_info',
        verbose_name='Группа', primary_key=True,
    )
    min_active = models.PositiveSmallIntegerField(
        'Мин. число активных участников', null=True, blank=True,
    )
    break_start = models.TimeField('Начало репетиции', null=True, blank=True, )
    break_end = models.TimeField('Конец репетиции', null=True, blank=True, )
    break_max_duration = models.PositiveSmallIntegerField(
        'Макс. длительность репетиции', null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Параметр репетиции'
        verbose_name_plural = 'Параметры репетиций'

    def __str__(self):
        return f'Break Info'


class Replacement(InfoMixin):
    group = models.ForeignKey(
        'breaks.GroupInfo', models.CASCADE, 'replacements',
        verbose_name='Группа',
    )
    date = models.DateField('Дата')
    break_start = models.TimeField('Начало репетиции')
    break_end = models.TimeField('Конец репетиции')
    break_max_duration = models.PositiveSmallIntegerField(
        'Макс. продолжительность репетиции',
    )
    min_active = models.PositiveSmallIntegerField(
        'Мин. число активных участников', null=True, blank=True,
    )

    members = models.ManyToManyField(
        'bands.Member', related_name='replacements',
        verbose_name='Участники смены', through='ReplacementMember'
    )

    class Meta:
        verbose_name = 'Репетиционный день'
        verbose_name_plural = 'Репетиционные дни'
        ordering = ('-date',)

    def __str__(self):
        return f'Репетиционный день №{self.pk} для {self.group}'


class ReplacementMember(models.Model):
    member = models.ForeignKey(
        'bands.Member', models.CASCADE, 'replacements_info',
        verbose_name='Участник'
    )
    replacement = models.ForeignKey(
        'breaks.Replacement', models.CASCADE, 'members_info',
        verbose_name='Репетиционный день'
    )
    status = models.ForeignKey(
        'breaks.ReplacementStatus', models.RESTRICT, 'members',
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Репетиционный день - участник группы'
        verbose_name_plural = 'Репетиционные дни - участники группы'

    def __str__(self):
        return f'Участник репетиционного дня {self.member.participant.user} ({self.pk})'
