"""
core functionality needed for the web scrapping
reading jsons, reading sourceforge folders etc.
"""

import requests
from bs4 import BeautifulSoup

from .json_loader import load_json
from .roms import ROMS

session = requests.Session()
cache = {}

def get_soup(url):
    """
    Get the BeautifulSoup object for a given URL.

    If the URL is already cached, return the cached value.
    Otherwise, make a GET request to the URL, parse the HTML content with
    the 'html.parser' and cache the result.

    :param url: The URL to fetch
    :return: The BeautifulSoup object for the given URL
    """
    if url in cache:
        return cache[url]

    r = session.get(url, timeout=10)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, "html.parser")

    cache[url] = soup
    return soup

def get_rom_versions_names():
    return ROMS.keys()


def get_last_hyperos_thread(target_url):
    """
    Gets the title and URL of the latest HyperOS thread from a given Xiaomi EU forum URL.

    Args:
        target_url (str): The URL of the Xiaomi EU forum page from which to get the latest HyperOS thread.

    Returns:
        tuple: A tuple containing the title and URL of the latest HyperOS thread.
    """
    soup = get_soup(target_url)
    thread = soup.find("div", class_="structItem-title")
    title = thread.find("a").text
    url = f"https://xiaomi.eu{thread.find('a')['href']}"
    return (title, url)


def get_devices_for_rom(rom_name):
    """
    Returns a list of devices supported by a given rom.
    
    Parameters:
    rom_name (str): The name of the rom.
    
    Returns:
    list: A list of devices supported by the given rom.
    """
    rom = ROMS.get(rom_name)
    if not rom:
        return []
    file = load_json(rom["json"])
    return list(file.keys())


def get_download_link(rom_name, device):
    """
    Returns the download link of a given rom for a given device.
    
    Parameters:
    rom_name (str): The name of the rom.
    device (str): The device for which the download link should be returned.
    
    Returns:
    str: The download link. If the rom or device is not found, returns None.
    """
    rom = ROMS.get(rom_name)
    if not rom:
        return None

    data = load_json(rom["json"])

    rom_file_name = data[device]["rom_name"]

    soup = get_soup(rom["sourceforge"])
    for row in soup.find_all("tr", class_="file"):
        a = row.find("a", href=True)
        if a and rom_file_name in a["href"]:
            return a["href"]

    return None
