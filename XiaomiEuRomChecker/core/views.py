from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from XiaomiEuRomChecker.core.models import AvailableDevicesModel


def index(request):
    if request.method == 'POST':
        chosen_device = AvailableDevicesModel.objects.filter(pk=request.POST.get('device')).get()
        return render(request, 'device_info.html', {'chosen_device': chosen_device})

    return render(request, 'index.html')
