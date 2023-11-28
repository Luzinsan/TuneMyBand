from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from band.models import MusicBand


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


# class AlterUser(User):
#     first_name = models.CharField(_("first name"), max_length=150, null=False, blank=False)
#     last_name = models.CharField(_("last name"), max_length=150, null=False, blank=False)
#     email = models.EmailField(_("email address"), null=False, blank=False)


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
