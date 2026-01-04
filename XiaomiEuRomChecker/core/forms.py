from django import forms
from .roms import ROMS

status_choices = (("Missing", "Missing"), ("Unsupported", "Unsupported"))
rom_version_choices = ((rom, rom) for rom in ROMS)


class ContactForm(forms.Form):
    rom_versions = forms.ChoiceField(choices=rom_version_choices, label='Rom version to check', required=True)
    market_name = forms.CharField(label='Market name', required=True)
    status = forms.ChoiceField(choices=status_choices, label='Report type', required=True)
    email = forms.EmailField(label='Email address', required=True)
