from django.db import models


class Project(models.Model):

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]


    STATUS_CHOICES = [
        ('Planning', 'Planning'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]


    name = models.CharField(max_length=100)

    description = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField()


    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Planning'
    )


    def __str__(self):
        return self.name