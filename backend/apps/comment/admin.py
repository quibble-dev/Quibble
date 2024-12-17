from django.contrib import admin

from .models import Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('quibbler', 'content', 'created_at', 'deleted')
    search_fields = ('quibbler__username', 'content')
