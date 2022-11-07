from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html
import markdown

register = template.Library()


@register.filter
def md_safe(text):
    html = markdown.markdown(text)
    return html