from django.contrib import admin

from XiaomiEuRomChecker.theme.models import ThemeModel, TipOfTheDayModel


# Register your models here.
@admin.register(ThemeModel)
class ThemesAdmin(admin.ModelAdmin):
    # to display all fields
    # list_display = [field.name for field in ThemeModel._meta.get_fields()]
    fieldsets = [
        ('Main colors',
         {'fields': ['navbar', 'header', 'first_grid_icon', 'second_grid_icon', 'rom_version_container']}),

        ('Secondary colors',
         {'fields': ['navbar_hover', 'small_screens_navbar', 'small_screens_menu', 'small_screens_menu_hover',
                     'second_grid_background', 'second_grid_p_color', 'back_home_button']}),
    ]

    # To disable adding of more than one theme:
    def has_add_permission(self, request):
        return False

    # to disable deleting of the theme
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TipOfTheDayModel)
class TipOfTheDayAdmin(admin.ModelAdmin):
    # to display all fields
    # list_display = [field.name for field in TipOfTheDayModel._meta.get_fields()] or:
    list_display = ['id', 'main_text', 'additional_text']
    ordering = ['id']
