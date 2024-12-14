from django.contrib import admin

from .models import CommentModel

# Register your models here.


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('quibbler', 'content', 'created_at', 'deleted')
    search_fields = ('quibbler__username', 'content')
