from django.urls import path, include
from . import views


app_name = 'api_v1'
urlpatterns = [
    # path('post_list/', views.api_post_list_pub, name='post_list'),

    # path('post_detail/<int:pk>/', views.api_post_detail, name='post_detail'),
    # path("post_list/", views.PostList.as_view(), name="post_list"),
    path('post_detail/<int:pk>/', views.PostDetailApiView.as_view(), name="post_detail"),

    path('post_list/', views.PostListGeneric.as_view(), name="post_detail_gen"),
]
