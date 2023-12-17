from common.models.mixins import BaseDictModelMixin


class Skill(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Genre(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
