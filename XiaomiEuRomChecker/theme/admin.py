from django.contrib import admin

from XiaomiEuRomChecker.theme.models import ThemeModel


# Register your models here.
@admin.register(ThemeModel)
class ThemesAdmin(admin.ModelAdmin):
    pass
