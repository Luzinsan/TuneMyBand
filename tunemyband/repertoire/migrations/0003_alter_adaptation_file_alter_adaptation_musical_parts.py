# Generated by Django 4.2.7 on 2023-11-16 18:59

from django.db import migrations
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0017_image__transparent'),
        ('repertoire', '0002_alter_adaptation_musical_parts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adaptation',
            name='file',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adaptation_file', to='filer.file'),
        ),
        migrations.AlterField(
            model_name='adaptation',
            name='musical_parts',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adaptation_musical_parts', to='filer.file'),
        ),
    ]