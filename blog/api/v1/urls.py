from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'api_v1'
'''
urlpatterns = [
    # path('post_list/', views.api_post_list_pub, name='post_list'),

    # path('post_detail/<int:pk>/', views.api_post_detail, name='post_detail'),
    # path("post_list/", views.PostList.as_view(), name="post_list"),
    # path('post/<int:pk>/', views.PostDetailApiView.as_view(), name="post_detail"),

    # path('post/', views.PostListGeneric.as_view(), name="post_list_gen"),
    path('posts/', views.PostListViewSet.as_view(actions={"get": "list"}), name='post_list_viewset'),
    path("posts/<int:pk>/", views.PostListViewSet.as_view(actions={"get": "retrieve",
                                                                   "put": "update",
                                                                   "patch": "partial_update",
                                                                   "delete": "destroy"}),
         name='post_retrieve'),

]'''

# router = DefaultRouter()
# router.register("posts", views.PostListViewSet, basename="posts")
# urlpatterns = router.urls

router = DefaultRouter()
router.register("posts", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls
