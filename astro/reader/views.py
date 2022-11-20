from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Document


class DocIndex(ListView):
    template_name = "reader/doc.html"
    model = Document


class DocDetail(DetailView):
    template_name = "reader/page.html"
    model = Document
