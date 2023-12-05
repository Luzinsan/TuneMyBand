# Generated by Django 5.0rc1 on 2023-12-05 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicBand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_created=True, blank=True, help_text='Введите дату формирования вашей музыкальной группы', null=True, verbose_name='Дата создания')),
                ('name', models.CharField(help_text='Введите название вашей музыкальной группы', max_length=100, unique=True, verbose_name='Музыкальная группа')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации в системе')),
                ('url', models.URLField(blank=True, help_text='Укажите ссылку, чтобы найти вашу группу на другом ресурсе', null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Музыкальная группа',
                'verbose_name_plural': 'Музыкальные группы',
                'ordering': ('-register_date',),
            },
        ),
    ]
