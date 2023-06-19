from django.urls import path, include
from django.views.generic import TemplateView

from Blog.routers import blog_router
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title="Blog API")

urlpatterns = [
    path('api_schema', schema_view, name='api_schema'),
    path('', include(blog_router.urls)),
    path('swagger/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'api_schema'}
    ), name='swagger-ui'),
]
