from django.contrib import admin

from .models import Quib

# Register your models here.


@admin.register(Quib)
class QuibAdmin(admin.ModelAdmin):
    list_display = ('title', 'quiblet', 'quibber', 'is_public', 'created_at')
    search_fields = ('title', 'quiblet__name', 'quibber__name')
