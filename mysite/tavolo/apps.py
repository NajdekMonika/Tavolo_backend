from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from .utils import update_clusters


class TavoloConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tavolo'


@receiver(post_save, sender=User)
def handle_user_save(sender, instance, created, **kwargs):
    if created:
        update_clusters(instance)
