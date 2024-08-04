from django.urls import path
from . import views


app_name = 'api-v1'
urlpatterns = [
    path('register/', views.UserRegistration.as_view(), name='register'),
]
