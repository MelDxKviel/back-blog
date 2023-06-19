from rest_framework.routers import DefaultRouter

from .viewsets import PostViewSet, CommentsViewSet, CategoryViewSet

blog_router = DefaultRouter()

blog_router.register(
    prefix='posts',
    viewset=PostViewSet,
    basename='posts'
)

blog_router.register(
    prefix='comments',
    viewset=CommentsViewSet,
    basename='comments'
)

blog_router.register(
    prefix='categories',
    viewset=CategoryViewSet,
    basename='categories',
)
