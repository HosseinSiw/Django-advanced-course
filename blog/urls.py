from django.urls import path
from . import views as V


app_name = 'blog'
urlpatterns = [

    path("", V.BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:pk>', V.BlogDetailView.as_view(), name='blog-detail'),

    path("create/", V.BlogCreationView.as_view(), name='blog-create'),
]
