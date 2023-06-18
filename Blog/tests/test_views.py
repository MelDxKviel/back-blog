from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from ..models import Post, Category, Comment
from ..views import spam_check


class HomepageTests(TestCase):
    def test_url_redirect(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/posts')

    def test_url_posts(self):
        response = self.client.get("/posts")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("posts"))
        self.assertTemplateUsed(response, "Blog/post_list.html")


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        Category.objects.create(category_name="TestCategory")
        cls.post = Post.objects.create(title="This is a test!", content="Test test test", author_id=cls.user.id,
                                       category_id=1, slug="test-slug")
        cls.comment = Comment.objects.create(text="Test comment", author_id=cls.user.id, post_id=1)

    def test_model_content(self):
        self.assertEqual(self.post.title, "This is a test!")
        self.assertEqual(self.post.content, "Test test test")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/posts")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Blog/post_list.html")
        self.assertContains(response, "This is a test!")
        self.assertContains(response, "Test test test")

    def test_detail_view(self):
        response = self.client.get(f"/posts/{self.post.slug}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Blog/post_detail.html")
        self.assertContains(response, "This is a test!")
        self.assertContains(response, "Test test test")
        self.assertContains(response, "Test comment")

    def test_spam_check(self):
        self.assertTrue(spam_check("normal comment"))
        self.assertTrue(spam_check(self.comment.text))
        self.assertFalse(spam_check("comment with link https://www.google.com/"))
        self.assertFalse(spam_check("comment with another link gmail.com"))
