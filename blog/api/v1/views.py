from rest_framework.response import Response
from ...models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins


'''
from rest_framework.decorators import api_view, permission_classes
@api_view(['GET', "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def api_post_list_pub(request):
    """
    A simple function based API view which can handle both GET and POST requests
    """
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        posts = PostSerializer(posts, many=True)
        return Response(posts.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
'''
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET', "PUT", "DELETE"])
def api_post_detail(request, pk):
    """
    It can be handled with several approaches, the best one is the second one.
    1. The first solution
    post = get_object_or_404(Post, id=pk)
    post = PostSerializer(post)
    return Response(post.data)
    """
    """
    2. The second solution 
    try:
        post = Post.objects.get(id=pk)
        post = PostSerializer(post)
        return Response(post.data, status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response({"details": "Post doesn't exists"}, status=status.HTTP_404_NOT_FOUND)
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "GET":
        post = PostSerializer(post)
        return Response(post.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''


'''class PostList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer

    def get(self, request):
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)'''


class PostListGeneric(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    permission_classes = (IsAuthenticatedOrReadOnly,)


'''class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = PostSerializer

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        data = request.data
        serializer = self.serializer_class(post, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.user == post.author:
            post.delete()
            return Response({"details": "Post has been deleted successfully"},
                            status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
'''
'''class PostDetail(GenericAPIView,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)'''


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
