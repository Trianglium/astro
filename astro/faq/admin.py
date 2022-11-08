from django.contrib import admin
from .models import Resource, AstroPoint, Rule

admin.site.register(Resource)
admin.site.register(AstroPoint)
admin.site.register(Rule)
