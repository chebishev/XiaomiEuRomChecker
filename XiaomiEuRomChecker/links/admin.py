from django.contrib import admin

from XiaomiEuRomChecker.links.models import LinksModel


# Register your models here.
@admin.register(LinksModel)
class LinksModelAdmin(admin.ModelAdmin):
    list_display = ['link_name']
    ordering = ['link_name']
    filter_fields = ['link_name']