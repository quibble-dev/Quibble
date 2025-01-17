from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'community', 'poster', 'is_public', 'created_at')
    search_fields = ('title', 'community__name', 'poster__name')
