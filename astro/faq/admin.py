from django.contrib import admin
from .models import Resource, AstroPoint, Rule, Tag

admin.site.register(Resource)
admin.site.register(AstroPoint)
admin.site.register(Rule)
admin.site.register(Tag)
