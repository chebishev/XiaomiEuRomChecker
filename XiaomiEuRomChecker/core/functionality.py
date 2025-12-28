"""
core functionality needed for the web scrapping
reading jsons
"""

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


def get_last_hyperos_thread(target_url):
    page = requests.get(target_url)
    soup = BeautifulSoup(page.content, "html.parser")

    thread = soup.find("div", class_="structItem-title")
    title = thread.find("a").text
    url = f"https://xiaomi.eu{thread.find("a")['href']}"
    return (title, url)

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
    :param release: is needed for the right url to be given to the parser
    :return: download link or None
    """
    message = ""
    target_urls = get_url('stable')
    for url in target_urls:
        message =  loop_through_specific_folder(url, device)
        if message:
            break
    if not message:
        return f"Sorry, no links for device with code name {device} in the {release} folder!"
    else:
        return message
