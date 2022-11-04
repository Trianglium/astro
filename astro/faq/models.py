from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=150)
    author = models.TextField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to="resources/", blank=True)
    image_link = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


PLANET = "planet"
SIGN = "sign"
HOUSE= "house"
POINTS = [
    (PLANET, "planet"),
    (SIGN, "sign"),
    (HOUSE, "house")
]

class AstroPoint(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    symbol = models.TextField(blank=True)
    tag = models.CharField(max_length=150, choices=POINTS)

    def __str__(self):
        return self.name


class Rule(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)