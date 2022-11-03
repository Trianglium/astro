from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=150)
    author = models.TextField()
    link = models.URLField(blank=True)
