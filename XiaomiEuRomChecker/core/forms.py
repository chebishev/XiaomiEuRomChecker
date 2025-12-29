from django import forms


status_choices = (("Missing", "Missing"), ("Unsupported", "Unsupported"))


class ContactForm(forms.Form):
    market_name = forms.CharField(label='Market name', required=True)
    status = forms.ChoiceField(choices=status_choices, label='Report type')
    email = forms.EmailField(label='Email address', required=True)
