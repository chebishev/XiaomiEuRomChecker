from django import forms
import requests
from bs4 import BeautifulSoup


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
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find(id="post-5137")
    return result.find_all('td')


devices = get_devices_from_url()
devices_list = []
for index in range(0, len(devices), 3):
    market_name = devices[index].text
    devices_list.append(market_name)

choices = ((name, name) for name in sorted(devices_list))


class ContactForm(forms.Form):

    market_name = forms.ChoiceField(choices=choices, label='Market name')
    rom_options = forms.ChoiceField(choices=(('stable', 'stable'), ('weekly', 'weekly'), ('both', 'both')),
                                    label='Rom options')
