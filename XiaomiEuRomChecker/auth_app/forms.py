from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from XiaomiEuRomChecker.core.models import AvailableDevicesModel

UserModel = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2')


class AvailableDeviceModel:
    pass


class ProfileEditForm(forms.ModelForm):
    devices_query = AvailableDevicesModel.objects.values_list('market_name', flat=True).distinct()
    devices_query_choices = [
        ("", 'No Device')] + [(market_name, market_name) for market_name in devices_query]
    change_preferred_device = forms.ChoiceField(choices=devices_query_choices, required=False, widget=forms.Select)
    # change_preferred_device = forms.ModelChoiceField(
    #     queryset=AvailableDevicesModel.objects.values_list('market_name', flat=True),
    #     widget=forms.Select
    # )

    class Meta:
        model = UserModel
        fields = ('preferred_device', 'change_preferred_device')
        labels = {
            "preferred_device": "Current preferred device",
        }

