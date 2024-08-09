from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


app_name = 'api-v1'
urlpatterns = [
    # User registration endpoint
    path('register/', views.UserRegistration.as_view(), name='register'),

    # Token Login and Logout
    path("token/login/", views.CustomTokenObtainView.as_view(), name='token_login'),
    path("token/logout/", views.CustomTokenDiscardView.as_view(), name='token_logout'),

    # login JWT
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt-verify/', TokenVerifyView.as_view(), name='jwt_verify'),
    # Password endpoints (forgot and reset)
    path("change-password/", views.ChangePasswordView.as_view(), name='change_password'),

    # User profile endpoint
    path("profile/", views.ProfileApiView.as_view(), name='profile'),

    # User activation
    path("activation/confirm/", views.ConsoleEmailView.as_view(), name='test-email'),
]
