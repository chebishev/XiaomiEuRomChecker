from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from XiaomiEuRomChecker.core.models import AvailableDevicesModel

UserModel = get_user_model()


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

class ProfileEditForm(forms.ModelForm):
    devices_query = AvailableDevicesModel.objects.order_by('market_name').values_list('market_name', flat=True)
    devices_query_choices = [
                                ("", 'No Device')] + [(market_name, market_name) for market_name in devices_query]
    change_preferred_device = forms.ChoiceField(choices=devices_query_choices, required=False, widget=forms.Select)

    class Meta:
        model = UserModel
        fields = ('preferred_device', 'change_preferred_device')
        labels = {
            "preferred_device": "Current preferred device",
        }
