from django.test import TestCase
from django.urls import reverse
from polls.models import Question, Choice


class PollsIndexTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.question = Question.objects.create(question_text="", pub_date="")
        cls.choice = Choice.objects.create(question="", choice_text="", votes="")

    def test_url_pattern(self):
        response = self.client.get("/polls")
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        response = self.client.get(reverse("polls-index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "polls/index.html")


class PollsDetailTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.question = Question.objects.create(question_text="", pub_date="")
        cls.choice = Choice.objects.create(question="", choice_text="", votes="")

    def test_url_pattern(self):
        response = self.client.get("/polls/1")
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        response = self.client.get(reverse("poll-details"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "polls/detail.html")
