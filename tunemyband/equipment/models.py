from django.conf import settings
from django.db import models
from django.utils import timezone


class Equipment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    state = models.BooleanField(default=True)

    TYPES = (
        ('Музыкальный инструмент', (
            ('ud', 'Ударный'),
            ('med', 'Медный духовой'),
            ('der', 'Деревянный духовой'),
            ('str', 'Струнный'),
            ('kl', 'Клавишный'),
        )),
        ('Оборудование', (
            ('cab', 'Кабель'),
            ('vak', 'Звуковое оборудование'),
            ('mix', 'Микшер'),
            ('pedal', 'Педаль'),
        ),
        ),
         ('other', 'Другое'),
    )
    type = models.CharField(max_length=5, choices=TYPES, default='other')
    description = models.TextField(blank=True, null=True)
    register_date = models.DateTimeField(blank=True, null=True)

    def register(self):
        self.register_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name




