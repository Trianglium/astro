from django.test import TestCase
from django.urls import reverse
from faq.models import Resource, AstroPoint

class FAQIndexTests(TestCase):
    @classmethod
    def setUp(cls):
        cls.astro_point = AstroPoint.objects.create()

    def test_url_pattern(self):
        response = self.client.get("/learn")
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        response = self.client.get(reverse("faq-index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "faq/faq_index.html")


class ResourceListTests(TestCase):
    def setUp(cls):
        cls.resource = Resource.objects.create()
    def test_url_pattern(self):
        response = self.client.get("/learn/resources")
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        response = self.client.get(reverse("resource-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "faq/resource-list.html")

class ResourceDetailTests(TestCase):
    def setUp(cls):
        cls.resource = Resource.objects.create()
    def test_url_pattern(self):
        response = self.client.get("/learn/resources/1")
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        response = self.client.get(reverse("resource-detail"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "faq/resource-detail.html")