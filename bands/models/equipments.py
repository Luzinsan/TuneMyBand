import pdb

from django.db import models
from django.contrib.auth import get_user_model

from bands.models.dicts import TypeEquipment

User = get_user_model()


class Equipment(models.Model):
    owner = models.ForeignKey(User, models.CASCADE, 'equipments_users',
                              verbose_name='Владелец', )
    name = models.CharField(max_length=200, verbose_name='Название', )
    type = models.ForeignKey('bands.TypeEquipment', models.RESTRICT, 'equipments_types',
                             verbose_name='Тип', blank=True, null=True,
                             )
    status = models.BooleanField(default=True,
                                 verbose_name='Состояние',
                                 help_text='Активно/списано оборудование/инструмент.', )
    description = models.TextField(blank=True, null=True, max_length=1000,
                                   verbose_name='Описание',
                                   help_text='Основные характеристики оборудования/инструмента')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'name'], name='unique_user_equipment')
        ]
        ordering = ('-name',)
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'

    def __str__(self):
        return f"{self.owner} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.type:
           type, created = TypeEquipment.objects.get_or_create(
               code='test',
               defaults={
                   'name': 'Test',
                   'is_active': True,
                   'sort': 0,
               }
           )
           self.type = type
        return super(Equipment, self).save(*args, **kwargs)

