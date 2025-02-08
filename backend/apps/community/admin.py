from django.contrib import admin

from .models import Community


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'nsfw', 'created_at')
    search_fields = ('name',)
