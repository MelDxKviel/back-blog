from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from ..models import Post, Category, Comment
from ..forms import PostCreateForm, CommentForm


class TestPostForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        Category.objects.create(category_name="TestCategory")
        cls.post = Post.objects.create(title="This is a test!", content="Test test test", author_id=1, category_id=1)

    def test_valid_form(self):
        data = {"title": self.post.title, "content": self.post.content, "category": self.post.category}
        form = PostCreateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {"title": self.post.title, "category": self.post.category}
        form = PostCreateForm(data=data)
        self.assertFalse(form.is_valid())


class TestCommentForm(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        Category.objects.create(category_name="TestCategory")
        cls.post = Post.objects.create(title="This is a test!", content="Test test test", author_id=1, category_id=1)
        cls.comment = Comment.objects.create(text="Test comment", author_id=1, post_id=1)

    def test_valid_form(self):
        data = {"text": self.comment.text}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())
