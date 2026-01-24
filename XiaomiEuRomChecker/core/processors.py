"""
All the functions here are added as paths in django.settings -> TEMPLATES
The results from both are added to the context
"""

import json
import random

import django

from .json_loader import load_json


# just returns current installed django version for the footer
def django_version(request):
    return {'django_current_version': django.__version__}


# First check current date with the last date in the database if there is difference
# we get the latest added folder in the database and compare it with the current last folder in Sourceforge
# the function returns the folder name and link to it for the section above the footer
def latest_hyperos_thread(request):
    context = {
        'title': "HyperOS 3.0",
        'folder_link': "https://sourceforge.net/projects/xiaomi-eu-multilang-miui-roms/files/xiaomi.eu/HyperOS-STABLE-RELEASES/HyperOS3.0/",}
    return context


# THEME COLORS
def theme_colors(request):
    # change the file to default_theme.json to load default colors
    """
    Returns a dictionary containing the colors used in the theme as a key-value pair.

    The colors are loaded from the custom_theme.json file in the theme directory.
    The returned dictionary has the key 'color' and the value is another dictionary containing all the colors used in the theme.

    The function takes a request object as an argument, but it does not use it.
    """
    return {"color": load_json("custom_theme.json")}


# TIP OF THE DAY
def tip_of_the_day(request):
    """
    Returns a random tip from the tips.json file as a dictionary with the key 'tip'

    The tips are read from the file, and a random index is generated to select one of the tips.
    The selected tip is then returned as a dictionary with the key 'tip'.
    """
    all_tips = load_json("tips.json")
    # get a random tip
    start = 0
    stop = len(all_tips) - 1
    index = random.randint(start, stop)
    tip_to_show = all_tips[index]
    return {'tip': tip_to_show}
