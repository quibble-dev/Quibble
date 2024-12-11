# Generated by Django 5.1.4 on 2024-12-11 02:49

import dynamic_filenames
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Quiblet',
            fields=[
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
                    'id',
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet='abcdefghijklmnopqrstuvwxyz0123456789',
                        editable=False,
                        length=7,
                        max_length=7,
                        prefix='',
                        primary_key=True,
                        serialize=False,
                        verbose_name='id',
                    ),
                ),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                (
                    'cover',
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=dynamic_filenames.FilePattern(
                            filename_pattern='cover/{uuid:s}{ext}'
                        ),
                        verbose_name='cover',
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
