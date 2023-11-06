from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Post, Category, Comment, Tag


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class PostAdmin(ImportExportModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    resource_classes = [PostResource]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
