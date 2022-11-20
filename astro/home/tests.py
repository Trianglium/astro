from django.test import TestCase
from django.urls import reverse


class HomeTests(TestCase):
    def test_url_pattern(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/main.html")