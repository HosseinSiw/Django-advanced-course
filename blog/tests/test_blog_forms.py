from django.test import TestCase, SimpleTestCase
from ..forms import PostForm
from datetime import datetime
from ..models import Category


class PostFormTests(TestCase):
    def test_form_valid_data(self):
        category = Category.objects.create(name='test')
        data = {
            "title": "title",
            "content": "content",
            "status": True,
            # "publish_date": datetime.now(),
            "category": category,
        }
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        data = {}
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
