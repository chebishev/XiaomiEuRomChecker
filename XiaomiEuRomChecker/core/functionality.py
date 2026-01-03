"""
core functionality needed for the web scrapping
reading jsons, reading sourceforge folders etc.
"""

import json

import requests
from bs4 import BeautifulSoup
from XiaomiEuRomChecker.core.roms import ROMS

session = requests.Session()
cache = {}

def get_soup(url):
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
    soup = get_soup(target_url)
    thread = soup.find("div", class_="structItem-title")
    title = thread.find("a").text
    url = f"https://xiaomi.eu{thread.find("a")['href']}"
    return (title, url)


def get_devices_for_rom(rom_name):
    rom = ROMS.get(rom_name)
    if not rom:
        return []

    with open(f"XiaomiEuRomChecker/core/json/{rom['json']}", encoding="utf-8") as f:
        return list(json.load(f).keys())


def get_download_link(rom_name, device):
    rom = ROMS.get(rom_name)
    if not rom:
        return None

    with open(f"XiaomiEuRomChecker/core/json/{rom['json']}", encoding="utf-8") as f:
        data = json.load(f)

    rom_file_name = data[device]["rom_name"]

    soup = get_soup(rom["link"])
    for row in soup.find_all("tr", class_="file"):
        a = row.find("a", href=True)
        if a and rom_file_name in a["href"]:
            return a["href"]

    return None
