from rest_framework import serializers
from django.utils.text import slugify

from Blog.models import Post, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name',)


class PostRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ('id', 'slug', 'title', 'content', 'category', 'author', 'created_at',)


class PostCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), allow_null=True)

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'created_at',)

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)


class CommentsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created_at',)


class CommentsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text',)

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        validated_data['post_id'] = self.context['request'].query_params.get('post')
        return super().create(validated_data)
