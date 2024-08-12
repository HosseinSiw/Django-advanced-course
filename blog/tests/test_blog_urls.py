from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from blog.views import BlogIndexView, BlogDetailView, BlogListView, BlogCreationView


class TestUrls(SimpleTestCase):
    def test_index_page(self):
        url = reverse('blog:blog-index')
        self.assertEqual(resolve(url).func.view_class, BlogIndexView)

    def test_blog_detail_page(self):
        url = reverse('blog:blog-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, BlogDetailView)

    def test_blog_list_page(self):
        url = reverse("blog:blog-list")
        self.assertEqual(resolve(url).func.view_class, BlogListView)
