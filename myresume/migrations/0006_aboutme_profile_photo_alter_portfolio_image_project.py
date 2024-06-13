# Generated by Django 5.0.4 on 2024-06-09 18:31

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0005_alter_aboutme_file_resume_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='profile_photo',
            field=models.ImageField(default=11, upload_to='profile_photos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image_project',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[1000, 667], upload_to='images/'),
        ),
    ]