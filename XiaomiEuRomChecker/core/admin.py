from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


# changing admin header
admin.site.site_header = "xiaomi.eu Rom Checker Admin Panel"
# changing admin title
admin.site.site_title = "xiaomi.eu Rom Checker"
# changing admin index title
admin.site.index_title = "Manage models and groups"