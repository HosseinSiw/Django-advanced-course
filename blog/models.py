from django.db import models
from django.contrib.auth import get_user_model


USER_MODEL = get_user_model()


class Post(models.Model):
    """
    This class represents a single Post for the blog APP.
    """
    title = models.CharField(max_length=250)
    author = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name