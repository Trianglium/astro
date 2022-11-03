from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=150)
    author = models.TextField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to="resources/", blank=True)
    image_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
