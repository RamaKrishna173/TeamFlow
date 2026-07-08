from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Task(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]


    PRIORITY_CHOICES = [ 
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]


    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )


    title = models.CharField(
        max_length=200
    )


    description = models.TextField(
        blank=True
    )


    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )


    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )


    due_date = models.DateField(
        null=True,
        blank=True
    )


    parent_task = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subtasks'
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.title





class Comment(models.Model):

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="comments"
    )


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    message = models.TextField()


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.user.username} - {self.task.title}"





class ActivityLog(models.Model):

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="activities"
    )


    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )


    action = models.CharField(
        max_length=255
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.action
