from django import forms


# Create your forms here.

class ContactForm(forms.Form):
    code_name = forms.CharField(required=False, max_length=20, label='Code name',
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'alioth, zeus, marble', 'autofocus': True}))
    market_name = forms.CharField(required=False, max_length=40, label='Market name',
                                  widget=forms.TextInput(attrs={'placeholder': 'Poco F3, Xiaomi 13, Mi 10'}))
    rom_name = forms.CharField(required=False, max_length=30, label='Rom name',
                               widget=forms.TextInput(attrs={'placeholder': 'XM12, MI10S, FUXI'}))
    rom_options = forms.ChoiceField(choices=(('stable', 'stable'), ('weekly', 'weekly'), ('both', 'both')), label='Rom options')
    email = forms.EmailField(required=False, label='E-mail',
                             widget=forms.TextInput(attrs={'placeholder': 'Fill in for feedback'}))
    message = forms.CharField(required=False, widget=forms.Textarea, label='Optional message')
