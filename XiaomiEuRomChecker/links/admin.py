from django.contrib import admin

from XiaomiEuRomChecker.links.models import LinksModel


# Register your models here.
@admin.register(LinksModel)
class LinksModelAdmin(admin.ModelAdmin):
    list_display = ['link_name', 'user']
    ordering = ['link_name']
    filter_fields = ['link_name', 'user']
    list_filter = ['user']
    list_per_page = 20
