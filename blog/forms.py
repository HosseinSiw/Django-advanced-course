from django.forms import ModelForm

from blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', "status",]
