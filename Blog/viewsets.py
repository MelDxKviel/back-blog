from typing import Type

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets, pagination, serializers

from Blog.models import Post, Comment, Category
from .serializers import PostRetrieveSerializer, PostCreateSerializer, CommentsRetrieveSerializer, \
    CommentsCreateSerializer, CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 5
    queryset = Post.objects.all()

    def get_serializer_class(self) -> Type[serializers.ModelSerializer]:
        if self.action in {'create', 'update', 'partial_update'}:
            serializer_class = PostCreateSerializer
        else:
            serializer_class = PostRetrieveSerializer
        return serializer_class

    def get_permissions(self):
        if self.action in {'create', 'update', 'partial_update', 'delete'}:
            permissions = (IsAuthenticated(),)
        else:
            permissions = ()
        return permissions


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsRetrieveSerializer

    def get_queryset(self):
        post = self.request.query_params.get('post')
        if post:
            return Comment.objects.filter(post_id=post)
        else:
            return Comment.objects.all()

    def get_serializer_class(self) -> Type[serializers.ModelSerializer]:
        if self.action in {'create', 'update', 'partial_update'}:
            serializer_class = CommentsCreateSerializer
        else:
            serializer_class = CommentsRetrieveSerializer
        return serializer_class

    def get_permissions(self):
        if self.action in {'create', 'update', 'partial_update', 'delete'}:
            permissions = (IsAuthenticated(),)
        else:
            permissions = ()
        return permissions


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in {'create', 'update', 'partial_update', 'delete'}:
            permissions = (IsAuthenticated(), IsAdminUser(),)
        else:
            permissions = ()
        return permissions
