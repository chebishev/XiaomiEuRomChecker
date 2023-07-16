from django.contrib import admin

from XiaomiEuRomChecker.auth_app.models import AuthUser


# Register your models here.
@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_login' , 'is_superuser', 'is_staff', 'is_active', 'date_joined']
    ordering = ['date_joined']
    filter_fields = ['username', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined']