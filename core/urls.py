from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Django Advanced Course",
      default_version='v1',
      description="A brief description of your API",
      terms_of_service="https://yourwebsite.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="Your License Name"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls")),
    path('api-auth/', include('rest_framework.urls')),

    path('users/', include('users.urls')),
]

"""
API Documentation urls.
"""
urlpatterns += [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
