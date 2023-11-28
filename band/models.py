import datetime

from django.db import models
from django.urls import reverse


class MusicBand(models.Model):
    name = models.CharField(unique=True, max_length=100,
                            help_text='Введите название вашей музыкальной группы', verbose_name='Музыкальная группа')
    date_created = models.DateField(auto_created=True, null=True, blank=True,
                                     help_text='Введите дату формирования вашей музыкальной группы',
                                     verbose_name='Дата создания')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации в системе')
    url = models.URLField(null=True, blank=True, help_text='Укажите ссылку, чтобы найти вашу группу на другом ресурсе',
                          verbose_name='URL')

    class Meta:
        verbose_name = 'Музыкальная группа'
        verbose_name_plural = 'Музыкальные группы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('band:detail', args=[str(self.id)])

