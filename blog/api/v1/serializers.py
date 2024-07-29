from rest_framework import serializers

from blog.models import Post


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(min_length=1, max_length=255)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', "content", "published_date", "updated_date", "status", "author")
