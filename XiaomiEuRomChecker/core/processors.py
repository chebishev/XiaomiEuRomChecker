import django
import XiaomiEuRomChecker.core.functionality as f
from XiaomiEuRomChecker.core.models import AvailableDevicesModel


def django_version(request):
    return {'django_current_version': django.__version__}


# def latest_weekly(request):
#     current_folder = f.get_last_weekly_folder(f.get_driver(), f.get_url('weekly'))[1]
#     return {'latest_weekly': current_folder}


def all_devices(request):
    device_list = AvailableDevicesModel.objects.all()
    return {'device_list': device_list}
