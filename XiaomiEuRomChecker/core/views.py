from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from XiaomiEuRomChecker.core.functionality import get_link_for_specific_device
from XiaomiEuRomChecker.core.models import AvailableDevicesModel

UserModel = get_user_model()


def index(request):
    if request.method == 'POST':
        if request.POST.get('device') == "0":
            request.method = 'GET'
        else:
            chosen_device = AvailableDevicesModel.objects.get(id=request.POST.get('device'))
            return render(request, 'core/device_info.html', {'chosen_device': chosen_device})

    return render(request, 'core/index.html')


@login_required  # TODO: remove this and ask for login on link save
def downloads(request, pk, slug):
    # get required device by pk
    device = AvailableDevicesModel.objects.get(id=pk)
    if device.rom_options == "both":
        # this dictionary saves information for both types of roms, and it is used in the template
        # as iterable in order to have more dynamic content
        roms_result = {
            'stable': get_link_for_specific_device(device.rom_name, 'stable'),
            'weekly': get_link_for_specific_device(device.rom_name, 'weekly'),
        }
    else:
        # here we dynamically get the supported rom version for the device without showing unnecessary
        # information in the template
        roms_result = {
            device.rom_options: get_link_for_specific_device(device.rom_name, device.rom_options)
        }

    context = {
        'roms': roms_result,
        'device': device
    }
    if request.method == 'POST':
        if request.POST.get('save_link'):
            request.session['uid'] = request.POST.get('save_link')
            return redirect('link_add', request.user.id)

    return render(request, 'core/downloads.html', context)


# in Debug=False it redirects all wrong pages (404) to index
# there is a reference to this view in XiaomiEuRomChecker\urls.py
def page_not_found(request, exception=None):
    return redirect('index')
