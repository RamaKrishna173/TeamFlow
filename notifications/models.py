from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):

    TYPE_CHOICES = [
        ('Assignment', 'Assignment'),
        ('Status Change', 'Status Change'),
        ('Comment', 'Comment'),
        ('General', 'General'),
    ]


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications'
    )


    message = models.CharField(
        max_length=255
    )


    notification_type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default='General'
    )


    event_key = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )


    is_read = models.BooleanField(
        default=False
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.message