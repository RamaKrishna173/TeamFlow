from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):

    THEME_CHOICES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    theme = models.CharField(
        max_length=10,
        choices=THEME_CHOICES,
        default='light'
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:

        UserProfile.objects.create(
            user=instance
        )


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    UserProfile.objects.get_or_create(
        user=instance
    )
