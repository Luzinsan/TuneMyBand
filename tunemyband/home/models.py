from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
# from repertoire.models import Genre


class Skills(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    # place =
    sex = models.CharField(max_length=1, default='n', verbose_name='Пол',
                           choices=(
                               ('m', 'Мужской'),
                               ('f', 'Женский'),
                               ('n', 'Не определён')
                           ))
    birthday = models.DateField(auto_now=True, verbose_name='День рождения')
    about = models.TextField(null=True, blank=True, verbose_name='О себе')
    skills = models.ManyToManyField(Skills, default='Другое', verbose_name='Навыки')
    # genres = models.ManyToManyField(Genre, default='Другое')

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'
        ordering = ['-user']


class MusicBand(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    register_date = models.DateField(auto_now=True)
    url = models.URLField()
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name
