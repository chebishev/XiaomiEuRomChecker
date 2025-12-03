"""
All the functions here are added as paths in django.settings -> TEMPLATES
The results from both are added to the context
"""

import django
from XiaomiEuRomChecker.core.models import AvailableDevicesModel, FoldersModel
from XiaomiEuRomChecker.core.functionality import get_last_weekly_folder, get_url, get_date_as_string
from datetime import datetime


# just returns current installed django version for the footer
def django_version(request):
    return {'django_current_version': django.__version__}


# First check current date with the last date in the database if there is difference
# we get the latest added folder in the database and compare it with the current last folder in Sourceforge
# the function returns the folder name and link to it for the section above the footer
def latest_weekly(request):
    # last_object = FoldersModel.objects.last()
    # current_folder = last_object.folder_name
    # current_date = last_object.last_modification_date
    # year, month, day = current_date.year, current_date.month, current_date.day

    # difference = datetime.now() - datetime(year, month, day)
    # if difference.days:
    #     info_from_scrapping = get_last_weekly_folder(get_url('weekly'))
    #     new_folder = info_from_scrapping[0]
    #     if new_folder not in FoldersModel.objects.values_list('folder_name', flat=True):
    #         new_date = get_date_as_string(info_from_scrapping[1])

    #         # saving this data into the database
    #         FoldersModel.objects.create(
    #             folder_name=new_folder,
    #             last_modification_date=new_date
    #         )
    #         current_folder = new_folder

    # context = {
    #     # passing the name of the folder
    #     'current_folder': current_folder,

    #     # passing xiaomi.eu link to that folder
    #     "folder_link": get_url('last_weekly', current_folder)
    # }
    context = {
        'current_folder': "24.7.28 (Final)",
        "folder_link": "https://sourceforge.net/projects/xiaomi-eu-multilang-miui-roms/files/xiaomi.eu/HyperOS-WEEKLY-RELEASES/OS1.0.24.7.28.DEV/"
    }

    return context


# It gives me access to all devices as a list in the templates. Currently used in index.html
def all_devices(request):
    device_list = AvailableDevicesModel.objects.all().order_by('market_name')
    return {'device_list': device_list}
