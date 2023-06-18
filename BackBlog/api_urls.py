from django.urls import path, include
from Blog.routers import blog_router

urlpatterns = [
    path('', include(blog_router.urls)),
]
