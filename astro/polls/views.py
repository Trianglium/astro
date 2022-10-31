from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Question, Choice


class PollsIndex(ListView):
    template_name = "polls/index.html"
    model = Question

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class PollDetail(DetailView):
    pass
