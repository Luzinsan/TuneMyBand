from django.conf import settings
from django.db import models
import uuid


class TypeOfEquipment(models.Model):
    name = models.CharField(max_length=100, primary_key=True,
                            verbose_name='Тип оборудования/инструмента',
                            help_text='Введите новую разновидность оборудования/инструмента')

    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудований'

    def __str__(self):
        return self.name


class Equipment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              related_name='equipment_owner', verbose_name='Владелец оборудования/инструмента',
                              help_text='Укажите владельца данного оборудования/инструмента')
    name = models.CharField(max_length=200, verbose_name='Название оборудования/инструмента',
                            help_text='Введите уникальное название модели оборудования/инструмента')
    type = models.ForeignKey(TypeOfEquipment, on_delete=models.CASCADE,
                             verbose_name='Тип оборудования/инструмента',
                             help_text='Выберите тип оборудования/инструмента')
    state = models.BooleanField(default=True,
                                verbose_name='Активно/Списано оборудование',
                                help_text='Отметьте текущее состояние оборудования/инструмента')
    description = models.TextField(blank=True, null=True, max_length=1000,
                                   verbose_name='Описание',
                                   help_text='Опишите основные характеристики оборудования/инструмента')
    register_date = models.DateField(auto_created=True, verbose_name='Дата введения в эксплуатацию',
                                     help_text='Укажите дату начала активного использования оборудования/инструмента')
    music_band_show = models.BooleanField(default=True,
                                          verbose_name='Отображать в музыкальной группе?',
                                          help_text='Укажите, стоит ли отображать ваш инструмент в списке инструментов '
                                                    'музыкального коллектива, или нет?')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'name'], name='unique_equipment')
        ]
        ordering = ('-register_date',)
        get_latest_by = "-register_date"
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'

    def __str__(self):
        return self.name
