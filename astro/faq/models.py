from django.db import models


class Resources(models.Model):
    title = models.CharField(max_length=150)
    author = models.TextField()
    link = models.URLField(blank=True)

