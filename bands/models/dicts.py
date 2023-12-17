from common.models.mixins import BaseDictModelMixin


class TypeEquipment(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудований'


class Level(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'

