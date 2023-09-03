from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import ThreadTitle

UserModel = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel


@admin.register(UserModel)
class AuthUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ['username', 'last_login', 'is_superuser', 'is_active', 'date_joined']
    ordering = ['date_joined']
    filter_fields = ['username', 'last_login', 'is_superuser', 'is_active', 'date_joined']
    list_filter = ['is_staff']
    list_editable = ['is_active']
    # limit user fields in the panel to the following ones:
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups')}),
    )

    def save_model(self, request, obj, form, change):
        if not change:  # Check if this is a new user being created
            obj.set_password(form.cleaned_data['password1'])  # Use cleaned_data to get the password
        else:
            user = UserModel.objects.get(pk=obj.pk)
            if form.cleaned_data['password'] != user.password:
                obj.set_password(form.cleaned_data['password'])
        obj.save()


class ThreadTitleAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 20


admin.site.register(ThreadTitle, ThreadTitleAdmin)