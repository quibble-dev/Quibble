# Generated by Django 5.1.4 on 2024-12-17 06:02

import dynamic_filenames
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='QuibletModel',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(auto_now_add=True, verbose_name='create at'),
                ),
                (
                    'avatar',
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=dynamic_filenames.FilePattern(
                            filename_pattern='avatar/{uuid:s}{ext}'
                        ),
                        verbose_name='avatar',
                    ),
                ),
                ('is_public', models.BooleanField(default=True, verbose_name='is public')),
                (
                    'name',
                    models.CharField(
                        error_messages={'unique': 'Quiblet with this name already exists.'},
                        max_length=25,
                        unique=True,
                        verbose_name='name',
                    ),
                ),
                ('description', models.TextField(verbose_name='description')),
                (
                    'title',
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name='title'
                    ),
                ),
                (
                    'banner',
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=dynamic_filenames.FilePattern(
                            filename_pattern='banner/{uuid:s}{ext}'
                        ),
                        verbose_name='banner',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Quiblet',
                'verbose_name_plural': 'Quiblets',
                'ordering': ['-created_at'],
            },
        ),
    ]
