from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from XiaomiEuRomChecker.core.functionality import get_link_for_specific_device
from XiaomiEuRomChecker import settings
from XiaomiEuRomChecker.core.forms import ContactForm
from django.contrib.auth.decorators import login_required

UserModel = get_user_model()


def index(request):
    if request.method == 'POST':
        if request.POST.get('device') == "0":
            request.method = 'GET'
        else:
            chosen_device = "Тук ще има списък с устройства като го направя"
            return render(request, 'core/device_info.html', {'chosen_device': chosen_device})

    return render(request, 'core/index.html')


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
            return redirect('link_add')

    return render(request, 'core/downloads.html', context)


# in Debug=False it redirects all wrong pages (404) to index
# there is a reference to this view in XiaomiEuRomChecker\urls.py
def page_not_found(request, exception=None):
    return redirect('index')


@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Check device information"
            body = {
                'market_name': f"Device market name: {form.cleaned_data['market_name']}",
                # 'code_name': f"Device code name: {get_devices_dict()[form.cleaned_data['market_name']]}",
                'status': f"Report type: {form.cleaned_data['status']}",
                'rom_options': f"Rom option to check: {form.cleaned_data['rom_options']}",
                'email': f"Email address: {form.cleaned_data['email']}",
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_RECIPIENT])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("thank_you")

    form = ContactForm()
    return render(request, "core/contact.html", {'form': form})


def thank_you(request):
    return render(request, 'core/thank_you.html')
