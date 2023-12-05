from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from band.models import MusicBand
from django.urls import reverse

import uuid


class Skills(models.Model):
    name = models.CharField(max_length=100, primary_key=True,
                            verbose_name='Навык', help_text='Напишите название навыка')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, primary_key=True,
                            verbose_name='Жанр', help_text='Напишите название жанра/направления')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class User(AbstractUser):
    pubkey = models.UUIDField(
        default=uuid.uuid4, db_index=True, editable=False, unique=True
    )

    EMAIL_FIELD = "username"
    USERNAME_FIELD = "username"

    def __str__(self):
        return f"{self.username} - {self.first_name} {self.last_name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=12, blank=True, verbose_name='Номер телефона')
    photo = models.ImageField(null=True, blank=True)
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
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def get_absolute_url(self):
        return reverse('accounts:accounts', args=[str(self.id)])
