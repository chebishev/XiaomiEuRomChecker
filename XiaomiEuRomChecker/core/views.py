from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from XiaomiEuRomChecker.core.forms import DevicesForm
from XiaomiEuRomChecker.core.get_info_from_sourceforge import output
from XiaomiEuRomChecker.core.models import AvailableDevicesModel


def index(request):
    form = DevicesForm()
    if request.method == 'POST':
        form = DevicesForm(request.POST)
        if form.is_valid():
            current_device = AvailableDevicesModel.objects.get(market_name=form.cleaned_data)
            print(current_device)
            print(form.cleaned_data)

    return render(request, 'index.html', {'form': form})
