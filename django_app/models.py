# django_app/models.py
from django.db import models


class Quote(models.Model):
    text = models.TextField()
    author = models.TextField()
    tags = models.TextField()

    def __str__(self):
        return f'{self.author} {self.text[:50]}'