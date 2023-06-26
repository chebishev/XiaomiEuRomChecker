from django.contrib import admin
from XiaomiEuRomChecker.core.models import AvailableDevicesModel


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


# Register your models here.
class DevicesAdmin(admin.ModelAdmin):
    list_display = ['code_name', 'market_name', 'rom_name', 'rom_options']
    filter_fields = ['code_name', 'market_name', 'rom_name', 'rom_options']
    # ordering = ['id', 'code_name', 'market_name', 'rom_name', 'rom_options']
    ordering = ['market_name']
    actions = [change_rom_both, change_rom_weekly, change_rom_stable]


admin.site.register(AvailableDevicesModel, DevicesAdmin)

# changing admin header
admin.site.site_header = "xiaomi.eu Rom Checker Admin Panel"
