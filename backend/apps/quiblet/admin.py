from django.contrib import admin

from .models import QuibletModel


@admin.register(QuibletModel)
class QuibletModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_public', 'created_at')
    search_fields = ('name',)
