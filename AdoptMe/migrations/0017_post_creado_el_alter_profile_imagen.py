# Generated by Django 4.1.7 on 2023-04-22 21:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AdoptMe', '0016_alter_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='creado_el',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
    ]