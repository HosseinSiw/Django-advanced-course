from django.test import TestCase
from users.models import User
from ..models import Post, Category


class TestPost(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='<EMAIL>', password='<PASSWORD>')
        self.category = Category.objects.create(name='category')

    def test_post_with_valid_data(self):

        post = Post.objects.create(title='Test', author=self.user, category=self.category, content='test_content',
                                   status=True)
        self.assertEqual(post.title, 'Test')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.category, self.category)
