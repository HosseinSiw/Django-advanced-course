from django.urls import path, include


app_name = 'users'
urlpatterns = [
    path('api/v1/', include('users.api.v1.urls')),
]
