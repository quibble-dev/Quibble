from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Profile, User
from .forms import CustomUserAdminForm, ProfileAdminForm


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # form = CustomUserAdminForm
    add_form = CustomUserAdminForm

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser'),
            },  # , 'groups', 'user_permissions')},
        ),
        (_('Important dates'), {'fields': ('date_joined',)}),
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
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm

    fieldsets = (
        (None, {'fields': ('user', 'username')}),
        (
            _('Other details'),
            {'fields': ('color', 'avatar', 'first_name', 'last_name')},
        ),
        (_('Important dates'), {'fields': ('created_at',)}),
    )

    list_display = ('username', 'user__email', 'created_at')
    search_fields = ('username', 'user__email')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
