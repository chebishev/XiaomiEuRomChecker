"""
All the functions here are added as paths in django.settings -> TEMPLATES
The results from both are added to the context
"""

import django
from XiaomiEuRomChecker.core.models import AvailableDevicesModel, FoldersModel
from XiaomiEuRomChecker.core.functionality import get_last_weekly_folder, get_driver, get_url
from datetime import datetime


# just returns current django version for the footer
def django_version(request):
    return {'django_current_version': django.__version__}


# First checks current date with the last date in the database if there is difference (4 days or more)
# gets the latest added folder in the database and compares it with the current last folder in Sourceforge
# returns the value for the section above the footer
def latest_weekly(request):
    last_object = FoldersModel.objects.last()
    current_folder = last_object.folder_name
    current_date = last_object.last_modification_date
    year, month, day = current_date.year, current_date.month, current_date.day

    difference = datetime.now() - datetime(year, month, day)
    if difference.days > 4:
        info_from_scrapping = get_last_weekly_folder(get_driver(), get_url('weekly'))
        new_folder = info_from_scrapping[1]
        if new_folder not in FoldersModel.objects.values_list('folder_name', flat=True):
            new_date = info_from_scrapping[2]
            FoldersModel.objects.create(
                folder_name=new_folder,
                last_modification_date=new_date
            )
            current_folder = new_folder
    return {'current_folder': current_folder}


# I am using it for the choices dropdown menu, but it can be replaced with form in the future
def all_devices(request):
    device_list = AvailableDevicesModel.objects.all().order_by('market_name')
    return {'device_list': device_list}
