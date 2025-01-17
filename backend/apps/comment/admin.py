from django.contrib import admin

from .models import Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter', 'content', 'created_at', 'deleted')
    search_fields = ('commenter__username', 'content')
