# Generated by Django 5.1.4 on 2025-02-08 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_community_nsfw_community_topics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='is_public',
        ),
        migrations.AddField(
            model_name='community',
            name='type',
            field=models.CharField(
                choices=[
                    ('PUBLIC', 'Public'),
                    ('RESTRICTED', 'Restricted'),
                    ('PRIVATE', 'Private'),
                ],
                default='PUBLIC',
            ),
        ),
    ]
