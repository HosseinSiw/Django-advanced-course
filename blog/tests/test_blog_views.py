from django.test import TestCase, Client
from django.urls import resolve, reverse

from ..models import Post, Category
from users.models import User


class TestBlogViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='<EMAIL>', password='<PASSWORD>')
        self.category = Category.objects.create(name='Test')
        self.post = Post.objects.create(title='Test', author=self.user, category=self.category, content='test_content',
                                        status=True)

    def test_list_page(self):
        url = reverse("blog:blog-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/posts_list.html")

    def test_details_page(self):
        self.client.force_login(self.user)
        url = reverse("blog:blog-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_anonymous(self):
        url = reverse("blog:blog-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
