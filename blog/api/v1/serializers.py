from rest_framework import serializers
from blog.models import Post, Category
from users.models import Profile
from django.utils.timezone import now


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(min_length=1, max_length=255)
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('id',)


class PostSerializer(serializers.ModelSerializer):
    # absolute_url = serializers.SerializerMethodField(method_name='get_absolute_url')
    slug = serializers.ReadOnlyField(source='get_slug')  # Model depended fields
    relative_url = serializers.ReadOnlyField(source='get_absolute_api_url')

    class Meta:
        model = Post
        fields = ('id', 'title', "content", "slug", "published_date", "updated_date", "status", "author",
                  "relative_url",)
        read_only_fields = ('id', 'author')  # Defining the read only fields

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
            rep.pop("slug", None)
        else:
            rep.pop("content", None)

        rep['category'] = CategorySerializer(instance=instance.category).data
        return rep

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id=self.context['request'].user.id)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['updated_time'] = now()

    # Image validation (to prevent file uploading attacks)
    # from PIL import Image
    # import io
    # def validate_image(self, value):
    #     if value:
    #         # Open the uploaded image file using PIL
    #         try:
    #             img = Image.open(value)
    #             img.verify()  # Verify that this is an image file
    #
    #             # Reopen the image (after verify() the image file needs to be reopened)
    #             value.seek(0)  # Move pointer back to the beginning of the file
    #             img = Image.open(value)
    #
    #             # Create a new image object to ensure it's saved in a standard format
    #             output = io.BytesIO()
    #             img.save(output, format='PNG')  # Save the image in the desired format
    #             output.seek(0)  # Move pointer to the beginning of the buffer
    #
    #             # Create a new Django File object to replace the old one
    #             from django.core.files.base import ContentFile
    #             value = ContentFile(output.read(), name=value.name)
    #         except (IOError, SyntaxError) as e:
    #             raise ValidationError("Invalid image file")
    #
    #     return value
