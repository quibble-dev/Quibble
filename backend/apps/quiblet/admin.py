from django.contrib import admin
from django.db.models import Count

from .models import Quiblet


@admin.register(Quiblet)
class QuibletAdmin(admin.ModelAdmin):
    list_display = ('name', 'members_count', 'is_public', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_public',)

    def members_count(self, obj):
        return obj.members_count

    members_count.admin_order_field = 'members_count'
    members_count.short_description = 'Members Count'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(members_count=Count('members'))
        return qs
