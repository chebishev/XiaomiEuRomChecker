from django import forms
from django.forms import Select

from XiaomiEuRomChecker.core.models import AvailableDevicesModel


class DevicesForm(forms.ModelForm):
    market_name = forms.ChoiceField(
        label='Market name',
        choices=AvailableDevicesModel.objects.values_list('market_name', 'market_name'),
        widget=forms.Select,
    )

    class Meta:
        model = AvailableDevicesModel
        fields = ['market_name', 'choice']
