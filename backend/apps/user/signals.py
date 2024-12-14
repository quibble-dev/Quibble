from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ProfileModel, User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        username = instance.email.split('@')[0]
        ProfileModel.objects.create(user=instance, username=username)
