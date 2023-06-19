from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentDelete, \
    CategoryCreateView, CategoryListView, CategoryDelete, TagCreateView

urlpatterns = [
    path('posts', PostListView.as_view(), name='posts'),
    path('posts/<slug:slug>', PostDetailView.as_view()),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<slug:slug>/update', PostUpdateView.as_view(), name='post_update'),
    path('posts/<slug:slug>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('delete-comment/<pk>/', CommentDelete.as_view(), name='delete_comment'),
    path('categories', CategoryListView.as_view(), name='categories'),
    path('categories/create', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<pk>/delete', CategoryDelete.as_view(), name='delete_category'),
    path('create-tag/', TagCreateView.as_view(), name='tag_create'),
]
