from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from home.models import Skills
from filer.fields.image import FilerImageField


class CustomUser(AbstractUser):
    phone_number = models.CharField(
        max_length=12, blank=True, verbose_name='Номер телефона')
    email = models.EmailField(
        max_length=255, unique=True, verbose_name='Почта')
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
    # genres = models.ManyToManyField(Genre, default='Другое')

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.',
        related_name='customuser_set',  # добавьте related_name
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',  # добавьте related_name
        related_query_name='user',
    )

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'


