# Generated by Django 4.2.7 on 2023-11-28 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('repertoire', '0001_initial'),
        ('band', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_datetime', models.DateTimeField()),
                ('place', models.CharField(max_length=100)),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('level', models.CharField(choices=[('6', 'Школьный'), ('5', 'Студенческий'), ('4', 'Городской'), ('3', 'Областной'), ('2', 'Федеральный'), ('1', 'Мировой')], max_length=1)),
                ('sponsor', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ['-start_datetime', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artists', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('composition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repertoire.adaptation')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('music_band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='band.musicband')),
            ],
            options={
                'verbose_name': 'Выступление',
                'verbose_name_plural': 'Выступления',
                'ordering': ['-event__start_datetime', 'music_band__name', 'composition__original__title'],
            },
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.UniqueConstraint(fields=('name', 'start_datetime'), name='unique_event'),
        ),
        migrations.AddConstraint(
            model_name='performance',
            constraint=models.UniqueConstraint(fields=('event', 'composition', 'music_band'), name='unique_performance'),
        ),
    ]
