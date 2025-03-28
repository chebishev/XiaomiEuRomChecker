from django.contrib import admin
from XiaomiEuRomChecker.core.models import AvailableDevicesModel, FoldersModel
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


# changing admin header
admin.site.site_header = "xiaomi.eu Rom Checker Admin Panel"
# changing admin title
admin.site.site_title = "xiaomi.eu Rom Checker"
# changing admin index title
admin.site.index_title = "Manage models and groups"

ITEMS_PER_PAGE = 20


# next 3 functions are needed to create new actions in the admin page
def change_rom_both(self, request, queryset):
    queryset.update(rom_options='both')


def change_rom_weekly(self, request, queryset):
    queryset.update(rom_options='weekly')


def change_rom_stable(self, request, queryset):
    queryset.update(rom_options='stable')


# These 3 rows will show under the "Delete selected Available Devices" action
change_rom_both.short_description = 'Change rom_options to "both"'
change_rom_weekly.short_description = 'Change rom_options to "weekly"'
change_rom_stable.short_description = 'Change rom_options to "stable"'

# necessary class for import-export module
class AvailableDevicesModelResource(resources.ModelResource):
    class Meta:
        model = AvailableDevicesModel

# Register your models here.
@admin.register(AvailableDevicesModel)
class DevicesAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['code_name', 'market_name', 'rom_name', 'rom_options', 'slug']
    filter_fields = ['code_name', 'market_name', 'rom_name', 'rom_options', 'slug']
    # ordering = ['id', 'code_name', 'market_name', 'rom_name', 'rom_options']
    list_filter = ['rom_options']
    ordering = ['code_name']
    search_fields = ['code_name', 'market_name', 'rom_name']
    actions = [change_rom_both, change_rom_weekly, change_rom_stable]
    list_per_page = ITEMS_PER_PAGE

    resource_classes = [AvailableDevicesModelResource]

@admin.register(FoldersModel)
class FoldersAdmin(admin.ModelAdmin):
    list_display = ['folder_name', 'last_modification_date']
    # To show newest folders first, because the name contains Rom version and date
    ordering = ['-last_modification_date']
    search_fields = ['folder_name']
    list_per_page = ITEMS_PER_PAGE
