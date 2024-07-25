from django.urls import path, include
from . import views as V


app_name = 'blog'
urlpatterns = [

    # path("", V.BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:pk>', V.BlogDetailView.as_view(), name='blog-detail'),

    path("create/", V.BlogCreationView.as_view(), name='blog-create'),

    path('api/v1/', include('blog.api.v1.urls')),  # API urls of the blog app
]
