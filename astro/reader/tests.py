from django.test import TestCase
from django.urls import reverse
from reader.models import Document

class DocIndexTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.doc = Document.objects.create(title="", author="", pages="", cover="")

    def test_url_pattern(self):
        response = self.client.get("/read")
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        response = self.client.get(reverse("doc-index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reader/doc.html")



class DocDetailTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.doc = Document.objects.create(title="", author="", pages="", cover="")
    def test_url_pattern(self):
        response = self.client.get("/read/1")
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        response = self.client.get(reverse("doc-detail"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reader/page.html")
