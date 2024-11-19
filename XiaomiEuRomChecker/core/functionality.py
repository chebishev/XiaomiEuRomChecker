"""
core functionality needed for my web scrapping
including driver, url, date checking
"""

from datetime import datetime
import random

import requests
from bs4 import BeautifulSoup


def files_list_info(url, tag, class_name):
    # it gets url for weekly or stable folder of sourceforge server
    page = requests.get(url)

    # BeautifulSoup instance that gets url and parser as arguments
    soup = BeautifulSoup(page.content, "html.parser")

    # getting the info directly from the html by id of the table
    result = soup.find(id="files_list")

    # returns all tags with the class name provided
    return result.find_all(tag, class_=class_name)


def get_url(release, folder=''):
    """
    Gives a link for the chosen release
    if it is 'weekly' or 'stable' second parameters aren't used,
    otherwise it is used in order to concatenate it at the end of the generated link
    :return: weekly folder url or tuple with stable folder urls
    """
    static_url = 'https://sourceforge.net/projects/xiaomi-eu-multilang-miui-roms/files/xiaomi.eu/'
    stable_url = static_url + 'HyperOS-STABLE-RELEASES/'
    # at this point it can't be retrieved dynamically, because of the continuous changing of the folder contents,
    # which moves the folder with the newest content on the first position
    stable_folders = ("HyperOS2.0", "HyperOS1.0")
    stable_urls = tuple(stable_url + folder for folder in stable_folders )
    weekly_url = static_url + 'HyperOS-WEEKLY-RELEASES/'
    available_urls = {
        'stable': stable_urls,
        'weekly': weekly_url,
        'last_weekly': weekly_url + folder
    }
    return available_urls[release]


def get_date(string):
    """
    Extracts year, month and day from string in format YYYY-MM-DD
    :param string:
    :return: list of integers [2023, 06, 29]
    """
    date_for_splitting = string
    if "<" in date_for_splitting:
        date_for_splitting = datetime.today().strftime("%Y-%m-%d")
    return [int(x) for x in date_for_splitting.split("-")]


def get_date_as_string(date):
    """
    :param date: it can be a string in format "2023-06-29" or string in format "< n hours ago"
    :return: string in format "2023-06-29"
    """
    # just in case if the rom "modified" field doesn't contain date
    # it will have something like: "< 5 hours ago" so I am converting it to today's date
    # in order to have a date in the format "2023-06-29"
    if "<" in date:
        return f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}"

    return date


def get_date_difference(date):
    """
    :param date: is a string in format "2023-06-29"
    :return: timedelta in days, seconds and microseconds as kwargs
    """
    # getting the difference in days (it gave something like "2 days, 14:05:28.657927", which is translated to
    # number with ".days" in the "if" statement)
    difference = datetime.now() - datetime(*get_date(date))
    return difference

def get_last_weekly_folder(target_url):
    # getting all table rows with this class in order to get the folder name and last modification date (or hours)
    folders = files_list_info(target_url, "tr", "folder")

    # getting all the rows, but we need only the first valid one since it is the folder that we are checking
    for folder in folders:
        if "Parent" in folder.text:
            continue
        # after finding the row that contains folder name and date, we break the loop
        # and return the first two elements of the row:
        # folder name in format "OS1.0.24.1.11.DEV" and date in format "2023-04-31 or '<', because of the splitting"
        return folder.text.split()[:2]

def loop_through_specific_folder(url, device):
    device_roms = files_list_info(url, 'tr', "file")
    for rom in device_roms:
        current_rom = rom.text
        if f"_{device}_OS" in current_rom:
            return url + "/" + current_rom.split()[0]
    else:
        return False

def get_link_for_specific_device(device, release):
    """
    :param device: gets device rom name in order to search for it in the folder and to find the first match
    :param release: is needed for the right url to be given to the driver
    :return: download link or None
    """
    message = ""
    if release == "weekly":
        target_url = get_url('last_weekly', (get_last_weekly_folder(get_url('weekly'))[0]))
        message = loop_through_specific_folder(target_url, device)
    else:
        target_urls = get_url('stable')
        for url in target_urls:
            message =  loop_through_specific_folder(url, device)
            if message:
                break
    if not message:
        return f"Sorry, no links for device with code name {device} in the {release} folder!"
    else:
        return message
