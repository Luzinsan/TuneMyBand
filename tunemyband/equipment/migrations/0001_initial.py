# Generated by Django 5.0rc1 on 2023-11-20 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_auth', '0001_initial'),
        ('band', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfEquipment',
            fields=[
                ('name', models.CharField(default='Неизвестно', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('state', models.CharField(choices=[('1', 'Активен'), ('0', 'Списан')], default='1', max_length=5)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('music_band', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='music_band', to='band.musicband')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment_owner', to='app_auth.customuser')),
                ('type', models.ForeignKey(default='Неизвестно', on_delete=django.db.models.deletion.SET_DEFAULT, to='equipment.typeofequipment')),
            ],
            options={
                'ordering': ('-register_date',),
            },
        ),
        migrations.AddConstraint(
            model_name='equipment',
            constraint=models.UniqueConstraint(fields=('owner', 'name'), name='unique_equipment'),
        ),
    ]
