from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from XiaomiEuRomChecker.core.functionality import get_url, get_link_for_specific_device
from XiaomiEuRomChecker.core.models import AvailableDevicesModel


def index(request):
    if request.method == 'POST':
        if request.POST.get('device') == "0":
            request.method = 'GET'
        else:
            chosen_device = AvailableDevicesModel.objects.get(id=request.POST.get('device'))
            return render(request, 'device_info.html', {'chosen_device': chosen_device})

    return render(request, 'index.html')


@login_required
def downloads(request, pk, slug):
    device = AvailableDevicesModel.objects.get(id=pk)
    roms_result = {
        'stable':
            {get_url('stable'): get_link_for_specific_device(device.rom_name, 'stable')},
        'weekly':
            {get_url('weekly'): get_link_for_specific_device(device.rom_name, 'weekly')},
    }
    links = {
        'roms': roms_result,
        'device': device
    }

    return render(request, 'downloads.html', links)

def page_not_found(request, exception=None):
    return redirect('index')