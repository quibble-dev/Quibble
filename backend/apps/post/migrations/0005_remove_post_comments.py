# Generated by Django 5.1.7 on 2025-04-06 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_post_is_public_post_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]
