from django.test import TestCase
from django.urls import reverse
from polls.models import Question, Choice


class PollsIndexTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass


class PollsDetailTest(TestCase):
    pass
