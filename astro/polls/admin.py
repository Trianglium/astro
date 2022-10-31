from django.contrib import admin
from .models import Question, Choice

admin.register(Choice)
admin.register(Question)
