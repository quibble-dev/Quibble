from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserAdminForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # form = CustomUserAdminForm
    add_form = CustomUserAdminForm

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser'),
            },  # , 'groups', 'user_permissions')},
        ),
        (_('important dates'), {'fields': ('date_joined',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password', 'is_active', 'is_staff', 'is_superuser'),
            },
        ),
    )

    readonly_fields = ('date_joined',)
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    search_fields = ('email',)
    ordering = ('email',)
