# five/models.py

from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # duration in minutes

    def __str__(self):
        return self.name
