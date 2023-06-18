from rest_framework.routers import DefaultRouter

from .viewsets import PostViewSet, CommentsViewSet

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
