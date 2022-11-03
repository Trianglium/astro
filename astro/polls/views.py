from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Question, Choice
from django.utils import timezone


class PollsIndex(ListView):
    template_name = "polls/index.html"
    model = Question
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class PollDetail(DetailView):
    template_name = "polls/detail.html"
    model = Question


class PollResults(DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:poll-results", args=(question.id,)))


class CreatePoll(CreateView):
    model = Question
    fields = ["question_text", "pub_date", "tags"]


class UpdatePoll(UpdateView):
    model = Question
    fields = ["question_text", "pub_date", "tags"]


class DeletePoll(DeleteView):
    model = Question
    success_url = reverse_lazy("polls-index")
