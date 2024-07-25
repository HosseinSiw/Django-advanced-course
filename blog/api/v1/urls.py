from django.urls import path
from . import views


app_name = 'api_v1'
urlpatterns = [
    path('post_list/', views.api_post_list, name='post_list'),
]
