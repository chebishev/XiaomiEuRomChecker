from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class AuthUserAdmin(admin.ModelAdmin):

    list_display = ['username', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
    ordering = ['date_joined']
    filter_fields = ['username', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
    list_filter = ['is_staff']

    # in order to save the password properly when the user is added via admin panel
    # without this method, the password is not hashed can be seen as is in the admin panel and in the db
    def save_model(self, request, obj, form, change):
        obj.set_password(form.data['password'])
        obj.save()
