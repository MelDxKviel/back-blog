from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from ..models import Post, Category, Comment


class HomepageTests(TestCase):
    def test_url_redirect(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/posts')

    def test_homepage_exists_at_correct_location(self):
        response = self.client.get("/posts")
        self.assertEqual(response.status_code, 200)

    def test_homepage_available_by_name(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Blog/post_list.html")


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        Category.objects.create(category_name="TestCategory")
        cls.post = Post.objects.create(title="This is a test!", content="Test test test", author_id=cls.user.id,
                                       category_id=1, slug="test-slug")
        cls.comment = Comment.objects.create(text="Test comment", author_id=cls.user.id, post_id=1)
 
    def test_homepage_contains_post_title(self):
        response = self.client.get(reverse("posts"))
        self.assertContains(response, "This is a test!")
        
    def test_homepage_contains_post_content(self):
        response = self.client.get(reverse("posts"))
        self.assertContains(response, "Test test test")

    def test_post_exists(self):
        response = self.client.get(f"/posts/{self.post.slug}")
        self.assertEqual(response.status_code, 200)
    
    def test_detail_template(self):
        response = self.client.get(f"/posts/{self.post.slug}")
        self.assertTemplateUsed(response, "Blog/post_detail.html")
  
    def test_detail_title(self):
        response = self.client.get(f"/posts/{self.post.slug}")
        self.assertContains(response, "This is a test!") 
        
    def test_detail_content(self):
        response = self.client.get(f"/posts/{self.post.slug}")
        self.assertContains(response, "Test test test")
        
    def test_detail_comment(self):
        response = self.client.get(f"/posts/{self.post.slug}")
        self.assertContains(response, "Test comment")
        
    def test_detail_category(self):
        response = self.client.get(f"/posts/{self.post.slug}")
        self.assertContains(response, "TestCategory")
