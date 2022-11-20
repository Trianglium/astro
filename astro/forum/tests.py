from django.test import TestCase
from django.urls import reverse
from forum.models import Comment, Tag, Post


class ForumIndexTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.comment = Comment.objects.create()
        cls.tag = Tag.objects.create()
        cls.post = Post.objects.create()

    def test_url_pattern(self):
        response = self.client.get("/forum")
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        response = self.client.get(reverse("forum-index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "forum/index.html")
