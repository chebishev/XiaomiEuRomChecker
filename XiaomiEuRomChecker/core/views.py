from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from XiaomiEuRomChecker import settings
from XiaomiEuRomChecker.core.forms import ContactForm
from XiaomiEuRomChecker.core.functionality import (get_devices_for_rom,
                                                   get_download_link,
                                                   get_rom_versions_names)
from XiaomiEuRomChecker.core.json_loader import load_json

UserModel = get_user_model()

def index(request):
    roms = get_rom_versions_names()
    return render(request, "core/index.html", {"roms": roms})


def ajax_devices(request):
    rom = request.GET.get("rom")
    return JsonResponse({"devices": get_devices_for_rom(rom)})


def ajax_download(request):
    rom = request.GET.get("rom")
    device = request.GET.get("device")
    return JsonResponse({"download": get_download_link(rom, device)})


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
                'rom_version': f"Rom version name: {form.cleaned_data['rom_versions']}",
                'status': f"Report type: {form.cleaned_data['status']}",
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
