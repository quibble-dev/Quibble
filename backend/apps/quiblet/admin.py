from django.contrib import admin

from .models import Quib, Quiblet


@admin.register(Quiblet)
class QuibletAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_public', 'created_at')
    search_fields = ('name',)


@admin.register(Quib)
class QuibAdmin(admin.ModelAdmin):
    list_display = ('title', 'quiblet', 'quibber', 'is_public', 'created_at')
    search_fields = ('title', 'quiblet__name', 'quibber__name')
