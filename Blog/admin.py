from django.contrib import admin

from .models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
