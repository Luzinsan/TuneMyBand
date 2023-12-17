from django.contrib.auth import get_user_model
from django.db import models

from common.models.mixins import InfoMixin

User = get_user_model()


class Offer(InfoMixin):
    band = models.ForeignKey(
        'Band', models.RESTRICT, 'offers',
        verbose_name='Музыкальный коллектив',
    )
    org_accept = models.BooleanField(
        'Согласие коллектива', null=True, blank=True
    )
    user = models.ForeignKey(
        User, models.RESTRICT, 'offers',
        verbose_name='Пользователь',
    )
    user_accept = models.BooleanField(
        'Согласие пользователя', null=True, blank=True
    )

    class Meta:
        verbose_name = 'Оффер'
        verbose_name_plural = 'Офферы'
        ordering = ('-created_at',)
        unique_together = (('band', 'user'),)

    def __str__(self):
        return f'Оффер №{self.pk}'

    @property
    def is_from_org(self):
        return bool(self.user != self.created_by)

    @property
    def is_from_user(self):
        return bool(self.user == self.created_by)