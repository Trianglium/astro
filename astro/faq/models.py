from django.db import models


class Tag(models.Model):
    value = models.TextField(max_length=100, unique=True)

    class Meta:
        ordering = ["value"]

    def __str__(self):
        return self.value


class Resource(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150, blank=True)
    author = models.TextField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to="resources/", blank=True)
    image_link = models.URLField(blank=True)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name="resources", blank=True)

    def __str__(self):
        return self.title


PLANET = "planet"
SIGN = "sign"
HOUSE = "house"
ELEMENT = "element"
MODALITY = "modality"
CONCEPT = "concept"
QUALITY = "quality"
ASPECT = "aspect"
POLARITY = "polarity"
POINT = "point"

POINT_CATEGORIES = [
    (PLANET, "planet"),
    (SIGN, "sign"),
    (HOUSE, "house"),
    (ELEMENT, "element"),
    (MODALITY, "modality"),
    (CONCEPT, "concept"),
    (QUALITY, "quality"),
    (ASPECT, "aspect"),
    (POLARITY, "polarity"),
    (POINT, "point"),
]


class AstroPoint(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    symbol = models.TextField(blank=True)
    image_symbol = models.ImageField(upload_to="learn/", blank=True)
    tag = models.CharField(max_length=150, choices=POINT_CATEGORIES)

    def __str__(self):
        return self.name


class Rule(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
