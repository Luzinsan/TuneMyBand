from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TypeEquipment(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Тип оборудования/инструмента', )

    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудований'

    def __str__(self):
        return f"{self.name} ({self.pk})"


class Equipment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='equipments', verbose_name='Владелец оборудования/инструмента', )
    name = models.CharField(max_length=200, verbose_name='Название оборудования/инструмента', )
    type = models.ForeignKey(TypeEquipment, on_delete=models.CASCADE,
                             verbose_name='Тип оборудования/инструмента',
                             related_name='equipments')
    status = models.BooleanField(default=True,
                                 verbose_name='Состояние оборудования',
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
