from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta


class Profile(models.Model):
    user = models.OneToOneField('accounts.User', models.CASCADE,
                                related_name='profile', verbose_name='Пользователь',
                                primary_key=True)
    photo = models.ImageField(null=True, blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', null=True, blank=True, )
    sex = models.CharField(max_length=1, default='n', verbose_name='Пол',
                           choices=(
                               ('m', 'Мужской'),
                               ('f', 'Женский'),
                               ('n', 'Не определён')
                           ))
    about = models.TextField(null=True, blank=True, verbose_name='О себе')
    skills = models.ManyToManyField('accounts.Skill', 'profiles_skills',
                                    verbose_name='Навыки', blank=True)
    genres = models.ManyToManyField('accounts.Genre', 'profiles_genres',
                                    verbose_name='Любимые жанры', blank=True)
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return str(self.user)


