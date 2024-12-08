from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile, User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        username = instance.email.split('@')[0]
        Profile.objects.create(user=instance, username=username)
