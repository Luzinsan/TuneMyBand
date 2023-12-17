from django.contrib.auth import get_user_model
from django.db import models

from breaks.constants import BREAK_CREATED_STATUS, BREAK_CREATED_DEFAULT
from breaks.models.dicts import BreakStatus

User = get_user_model()


class Break(models.Model):
    replacement = models.ForeignKey(
        'breaks.Replacement', models.CASCADE, 'breaks', verbose_name='Репетиция',
    )
    member = models.ForeignKey(
        'breaks.ReplacementMember', models.CASCADE, 'breaks',
        verbose_name='Участник репетиции',
    )
    break_start = models.TimeField('Начало репетиции', null=True, blank=True,)
    break_end = models.TimeField('Конец репетиции', null=True, blank=True,)
    status = models.ForeignKey(
        'breaks.BreakStatus', models.RESTRICT, 'breaks', verbose_name='Статус',
        blank=True,
    )

    class Meta:
        verbose_name = 'Репетиция'
        verbose_name_plural = 'Репетиции'
        ordering = ('-replacement__date', 'break_start')

    def __str__(self):
        return f'Репетиция пользователя {self.member} ({self.pk})'

    def save(self, *args, **kwargs):
        if not self.pk:
            status, created = BreakStatus.objects.get_or_create(
                code=BREAK_CREATED_STATUS,
                defaults=BREAK_CREATED_DEFAULT
            )
            self.status = status
        return super(Break, self).save(*args, **kwargs)
