from django.urls import path
from . import views


app_name = 'api-v1'
urlpatterns = [
    path('register/', views.UserRegistration.as_view(), name='register'),
    path("token/login/", views.CustomTokenObtainView.as_view(), name='token_login'),
    path("token/logout/", views.CustomTokenDiscardView.as_view(), name='token_logout'),
]
