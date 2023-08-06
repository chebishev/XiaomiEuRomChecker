from django import forms

from XiaomiEuRomChecker.links.models import LinksModel


class SaveLinkForm(forms.ModelForm):
    class Meta:
        model = LinksModel
        fields = ['link_name']
        widgets = {
            'link_name': forms.TextInput(attrs={'autofocus': True}),
        }


class EditLinkForm(forms.ModelForm):
    class Meta:
        model = LinksModel
        fields = ['link_name', 'link_description']
