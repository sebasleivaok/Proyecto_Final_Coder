# Generated by Django 4.1.7 on 2023-04-15 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdoptMe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='descripccion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='descripccion_carousel',
            new_name='descripcion_carousel',
        ),
    ]
