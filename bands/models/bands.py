from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Band(models.Model):
    name = models.CharField(unique=True, max_length=100,
                            help_text='Введите название вашей музыкальной группы',
                            verbose_name='Музыкальный коллектив', )
    leader = models.ForeignKey(User, models.RESTRICT, 'band_leaders',
                               verbose_name='Руководитель музыкального коллектива', )
    members = models.ManyToManyField(User, 'band_members',
                                     verbose_name='Участники музыкального коллектива', blank=True, )
    # created_by = models.ForeignKey()
    # updated_by = models.ForeignKey()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации в системе')

    class Meta:
        verbose_name = 'Музыкальный коллектив'
        verbose_name_plural = 'Музыкальные коллективы'
        ordering = ('-created_date',)

    def __str__(self):
        return f"{self.name} ({self.pk})"


class Group(models.Model):
    band = models.ForeignKey('bands.Band', models.CASCADE, 'groups',
                             verbose_name='Музыкальный коллектив', )
    name = models.CharField(max_length=100,
                            help_text='Введите название музыкальной группы',
                            verbose_name='Музыкальная группа', )
    manager = models.ForeignKey(User, models.RESTRICT, 'group_managers',
                                verbose_name='Ответственный за музыкальную группу', )
    members = models.ManyToManyField(User, 'group_members',
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
