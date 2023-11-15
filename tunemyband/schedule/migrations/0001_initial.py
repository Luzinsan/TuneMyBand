# Generated by Django 4.2.7 on 2023-11-15 18:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rehearsal',
            fields=[
                ('start_date', models.DateTimeField(primary_key=True, serialize=False)),
                ('end_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
