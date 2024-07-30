from rest_framework import serializers

from blog.models import Post, Category


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(min_length=1, max_length=255)

class PostSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()
    slug = serializers.ReadOnlyField(source='get_slug')
    relative_url = serializers.ReadOnlyField(source='get_absolute_api_url')

    class Meta:
        model = Post
        fields = ('id', 'title', "content", "slug", "published_date", "updated_date", "status", "author",
                  "relative_url", "absolute_url")
        read_only_fields = ('id', 'author')  # Defining the read only fields

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('id',)
