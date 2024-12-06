# Generated by Django 5.1.3 on 2024-12-06 15:53

import functools

import django.db.models.deletion
import dynamic_filenames
from django.conf import settings
from django.db import migrations, models

import apps.user.managers
import quibble.shared.mixins.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
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
                ('password', models.CharField(max_length=128, verbose_name='password')),
                (
                    'last_login',
                    models.DateTimeField(blank=True, null=True, verbose_name='last login'),
                ),
                (
                    'is_superuser',
                    models.BooleanField(
                        default=False,
                        help_text='Designates that this user has all permissions without explicitly assigning them.',
                        verbose_name='superuser status',
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        max_length=254, unique=True, verbose_name='email address'
                    ),
                ),
                (
                    'date_joined',
                    models.DateTimeField(auto_now_add=True, verbose_name='date joined'),
                ),
                (
                    'is_staff',
                    models.BooleanField(
                        default=False,
                        help_text='Designates whether the user can log into this admin site.',
                        verbose_name='staff status',
                    ),
                ),
                (
                    'is_active',
                    models.BooleanField(
                        default=True,
                        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                        verbose_name='active',
                    ),
                ),
                (
                    'groups',
                    models.ManyToManyField(
                        blank=True,
                        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.group',
                        verbose_name='groups',
                    ),
                ),
                (
                    'user_permissions',
                    models.ManyToManyField(
                        blank=True,
                        help_text='Specific permissions for this user.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.permission',
                        verbose_name='user permissions',
                    ),
                ),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['-date_joined'],
            },
            managers=[
                ('objects', apps.user.managers.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
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
                    'color',
                    models.CharField(
                        choices=[
                            ('primary', 'primary'),
                            ('secondary', 'secondary'),
                            ('accent', 'accent'),
                            ('neutral', 'neutral'),
                            ('info', 'info'),
                            ('success', 'success'),
                            ('warning', 'warning'),
                            ('error', 'error'),
                        ],
                        default=functools.partial(
                            quibble.shared.mixins.models.get_random_color,
                            *(
                                [
                                    ('primary', 'primary'),
                                    ('secondary', 'secondary'),
                                    ('accent', 'accent'),
                                    ('neutral', 'neutral'),
                                    ('info', 'info'),
                                    ('success', 'success'),
                                    ('warning', 'warning'),
                                    ('error', 'error'),
                                ],
                            ),
                            **{},
                        ),
                        max_length=25,
                        verbose_name='color',
                    ),
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
                (
                    'username',
                    models.CharField(max_length=25, unique=True, verbose_name='username'),
                ),
                (
                    'first_name',
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name='first name'
                    ),
                ),
                (
                    'last_name',
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name='last name'
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='profiles',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'ordering': ['-created_at'],
            },
        ),
    ]
