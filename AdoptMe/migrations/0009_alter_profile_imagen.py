# Generated by Django 4.1.7 on 2023-04-17 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdoptMe', '0008_alter_profile_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
    ]
