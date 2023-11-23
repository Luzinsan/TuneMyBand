from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from band.models import MusicBand
from filer.fields.image import FilerImageField


class Skills(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=12, blank=True, verbose_name='Номер телефона')
    photo = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
    birthday = models.DateField(default=date.today() - relativedelta(years=20), verbose_name='Дата рождения')
    sex = models.CharField(max_length=1, default='n', verbose_name='Пол',
                           choices=(
                               ('m', 'Мужской'),
                               ('f', 'Женский'),
                               ('n', 'Не определён')
                           ))
    about = models.TextField(null=True, blank=True, verbose_name='О себе')
    skills = models.ManyToManyField(Skills, verbose_name='Навыки', blank=True,
                                            related_name='user_skills', related_query_name='skill')
    genres = models.ManyToManyField(Genre, verbose_name='Любимые жанры', default='Другое', blank=True,
                                    related_name='user_genres', related_query_name='genre')
    music_band = models.ForeignKey(MusicBand, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'

