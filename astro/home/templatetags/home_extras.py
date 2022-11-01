from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = template.Library()






@register.inclusion_tag("home/current_planets.html")
def current_planets():
    return {"title": "Current Planets"}
