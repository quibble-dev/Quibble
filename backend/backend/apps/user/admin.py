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

    list_display = ('username', 'user__email', 'date_created')
    search_fields = ('username', 'user__email')
    ordering = ('-date_created',)
    readonly_fields = ('date_created',)
