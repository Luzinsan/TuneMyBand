from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from band.models import MusicBand


class TypeOfEquipment(models.Model):
    name = models.CharField(max_length=100, primary_key=True, default='Неизвестно',
                            verbose_name='Тип оборудования/инструмента',
                            help_text='Введите новую разновидность оборудования/инструмента')

    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудований'

    def __str__(self):
        return self.name


class Equipment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='equipment_owner', verbose_name='Владелец оборудования/инструмента',
                              help_text='Укажите владельца данного оборудования/инструмента')
    name = models.CharField(max_length=200, verbose_name='Название оборудования/инструмента',
                            help_text='Введите уникальное название модели оборудования/инструмента')
    type = models.ForeignKey(TypeOfEquipment, on_delete=models.SET_DEFAULT, default='Неизвестно',
                             verbose_name='Тип оборудования/инструмента',
                             help_text='Выберите тип оборудования/инструмента')

    STATE_CHOICES = (
        ('1', 'Активен'),
        ('0', 'Списан'),
    )
    state = models.CharField(max_length=5, choices=STATE_CHOICES, default='1',
                             verbose_name='Состояние',
                             help_text='Выберите текущее состояние оборудования/инструмента')
    description = models.TextField(blank=True, null=True, max_length=1000,
                                   verbose_name='Описание',
                                   help_text='Опишите основные характеристики оборудования/инструмента')
    register_date = models.DateField(auto_created=True, verbose_name='Дата введения в эксплуатацию',
                                     help_text='Укажите дату начала активного использования оборудования/инструмента')
    music_band = models.ForeignKey(MusicBand, related_name='music_band',
                                   on_delete=models.SET_NULL,
                                   null=True, blank=True, verbose_name='Музыкальная группа',
                                   help_text='Укажите коллектив, в котором территориально '
                                             'находится данное оборудование/инструмент')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'name'], name='unique_equipment')
        ]
        ordering = ('-register_date',)
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'

    def __str__(self):
        return self.name

