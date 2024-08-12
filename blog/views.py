from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from .models import Post
from .forms import PostForm


class BlogListView(ListView):
    template_name = 'blog/posts_list.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        """
        By overwriting this method you will be able to create a personal queryset
        """
        qs = super(BlogListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by('-created_date')
        return qs


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/posts_detail.html"


class BlogCreationView(CreateView):
    template_name = 'blog/post_form.html'
    # model = Post
    success_url = '/'
    # fields = ['title', 'content', ]
    form_class = PostForm

    def form_invalid(self, form):
        form.instance.user = self.request.user.id
        return super().form_invalid(form)


class BlogIndexView(View):
    template_name = 'blog/index.html'

    def get(self, request,):
        return render(request, template_name=self.template_name)
