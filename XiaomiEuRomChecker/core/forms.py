from django import forms
import requests
from bs4 import BeautifulSoup
from functionality import get_random_user_agent


def get_devices_from_url():
    """
    With BeautifulSoup, get td elements from table with id="post-5137"
    Because there are no classes near the table, we use the id attribute
    and "td" tag to get as close as possible to the elements that we need.
    They are 3 elements in total for every "tr", but we don't need the 3rd one
    :return: 3 td elements, one element per row in format:
    "Market name"
    "Code name"
    "Unnecessary data"
    """
    url = "https://xiaomiui.net/all-xiaomi-codenames-5137/"
    headers = {'User-Agent': get_random_user_agent()}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find(id="post-5137")
    return result.find_all('td')


def get_devices_dict():
    """
    :return: dictionary with market names as keys and code names as values
    """
    devices = get_devices_from_url()
    devices_dict = {}
    for index in range(0, len(devices), 3):
        market_name = devices[index].text
        code_name = devices[index + 1].text
        devices_dict[market_name] = code_name

    return devices_dict


market_name_choices = ((name, name) for name in sorted(get_devices_dict().keys()))
status_choices = (("Missing", "Missing"), ("Unsupported", "Unsupported"))
rom_options_choices = (('stable', 'stable'), ('weekly', 'weekly'), ('both', 'both'))


class ContactForm(forms.Form):
    market_name = forms.ChoiceField(choices=market_name_choices, label='Market name')
    status = forms.ChoiceField(choices=status_choices, label='Report type')
    rom_options = forms.ChoiceField(choices=rom_options_choices, label='Rom options')
    email = forms.EmailField(label='Email address', required=True)
