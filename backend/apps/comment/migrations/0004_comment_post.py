# Generated by Django 5.1.7 on 2025-04-06 06:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_alter_comment_commenter_alter_comment_created_at_and_more'),
        ('post', '0005_remove_post_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='comments',
                to='post.post',
                verbose_name='Post',
            ),
            preserve_default=False,
        ),
    ]
