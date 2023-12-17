from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Band(models.Model):
    name = models.CharField(unique=True, max_length=100,
                            help_text='Введите название вашей музыкальной группы',
                            verbose_name='Название', )
    leader = models.ForeignKey(User, models.RESTRICT, 'bands_leaders',
                               verbose_name='Руководитель', )
    members = models.ManyToManyField(User, 'bands_members',
                                     verbose_name='Участники', blank=True, )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации в системе')

    class Meta:
        verbose_name = 'Музыкальный коллектив'
        verbose_name_plural = 'Музыкальные коллективы'
        ordering = ('-created_date',)

    def __str__(self):
        return f"{self.name} ({self.pk})"


class Group(models.Model):
    name = models.CharField(max_length=100,
                            help_text='Введите название музыкальной группы',
                            verbose_name='Музыкальная группа', )
    band = models.ForeignKey('bands.Band', models.CASCADE, 'groups_bands',
                             verbose_name='Музыкальный коллектив', )
    manager = models.ForeignKey(User, models.RESTRICT, 'groups_managers',
                                verbose_name='Ответственный за музыкальную группу', )
    members = models.ManyToManyField(User, 'groups_members',
                                     verbose_name='Участники музыкальной группы', blank=True, )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['band', 'name'], name='unique_band_group')
        ]
        verbose_name = 'Музыкальная группа'
        verbose_name_plural = 'Музыкальные группы'
        ordering = ('-name',)

    def __str__(self):
        return f"{self.band} - {self.name}"
