from django.db import models


class Document(models.Model):
    title = models.TextField()
    author = models.TextField(blank=True, default="unknown")
    pages = models.PositiveIntegerField(blank=True)
    cover = models.ImageField(upload_to="documents/", blank=True)

    def __str__(self):
        return f"{self.title}, {self.author}"
