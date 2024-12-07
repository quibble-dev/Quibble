from django.contrib import admin

from .models import Quiblet


@admin.register(Quiblet)
class QuibletAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_public', 'created_at')
    search_fields = ('name',)
