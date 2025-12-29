from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

UserModel = get_user_model()


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    pass


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username',)
        