# Generated by Django 4.2.7 on 2023-11-15 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0002_alter_customuser_skills'),
        ('equipment', '0002_equipment_music_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipment_owners', to='app_auth.customuser'),
        ),
    ]
