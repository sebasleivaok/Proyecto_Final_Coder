# Generated by Django 4.1.7 on 2023-04-17 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdoptMe', '0011_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
    ]