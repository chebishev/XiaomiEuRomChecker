"""
All the functions here are added as paths in django.settings -> TEMPLATES
The results from both are added to the context
"""

import django
from XiaomiEuRomChecker.core.functionality import get_last_hyperos_thread


# just returns current installed django version for the footer
def django_version(request):
    return {'django_current_version': django.__version__}


# First check current date with the last date in the database if there is difference
# we get the latest added folder in the database and compare it with the current last folder in Sourceforge
# the function returns the folder name and link to it for the section above the footer
def latest_hyperos_thread(request):
    title, url = get_last_hyperos_thread("https://xiaomi.eu/community/forums/hyperos.228/")
    print(title + "from processors.py")
    print(url + "from processors.py")
    context = {
        'title': title,
        'thread_link': url,}
    return context


# It gives me access to all devices as a list in the templates. Currently used in index.html
def all_devices(request):
    device_list = "core -> processors.py -> all_devices -> device_list"
    return {'device_list': device_list}
