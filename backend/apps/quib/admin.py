from django.contrib import admin

from .models import QuibModel

# Register your models here.


@admin.register(QuibModel)
class QuibModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'quiblet', 'quibber', 'is_public', 'created_at')
    search_fields = ('title', 'quiblet__name', 'quibber__name')
