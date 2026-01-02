from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from XiaomiEuRomChecker import settings
from XiaomiEuRomChecker.core.forms import ContactForm
from XiaomiEuRomChecker.core.functionality import (
    get_link_for_specific_device, get_rom_versions_names, get_devices_for_rom
    )
from XiaomiEuRomChecker.core.roms import ROMS
UserModel = get_user_model()

rom_names = ROMS.keys()

def index(request):
    # Get list of ROM versions
    rom_versions_names = list(get_rom_versions_names())
    return render(request, 'core/index.html', {'rom_versions_names': rom_versions_names})

def ajax(request):
    rom = request.GET.get("rom")
    devices = get_devices_for_rom(rom)
    return JsonResponse({"devices": devices})



def ajax_download(request):
    rom = request.GET["rom"]
    device = request.GET["device"]
    sourceforge_url = ROMS[rom]["sourceforge"]
    link = get_link_for_specific_device(rom, device, sourceforge_url)
    return JsonResponse({"download": link})

def downloads(request):
    # get required device by pk
    market_name = "Xiaomi 13"
    file_name = "HyperOS 3.0.json"
    link, rom_name = get_link_for_specific_device(file_name, market_name)

    context = {
        'download_link': link,
        'rom_name': rom_name,
        'device': market_name
    }
    print(context)

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
