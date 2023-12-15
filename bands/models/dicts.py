from common.models.mixins import BaseDictModelMixin


class TypeEquipment(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудований'


class Skills(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Genre(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Level(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'

