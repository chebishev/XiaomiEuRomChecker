from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class AuthUserAdmin(UserAdmin):
    list_display = (
        'username',
        'last_login',
        'is_superuser',
        'is_active',
        'date_joined',
    )

    ordering = ('date_joined',)
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    list_editable = ('is_active',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {
            'fields': (
                'is_staff',
                'is_superuser',
                'is_active',
                'groups',
                'user_permissions',
            )
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'is_staff',
                'is_superuser',
                'is_active',
            ),
        }),
    )
