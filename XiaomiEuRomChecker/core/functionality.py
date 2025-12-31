"""
core functionality needed for the web scrapping
reading jsons, reading sourceforge folders etc.
"""

import json
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

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

def get_last_hyperos_thread(target_url):
    soup = get_soup(target_url)
    thread = soup.find("div", class_="structItem-title")
    title = thread.find("a").text
    url = f"https://xiaomi.eu{thread.find("a")['href']}"
    return (title, url)


main_link = "https://sourceforge.net/projects/xiaomi-eu-multilang-miui-roms/files/xiaomi.eu/"
links_to_files = {
    "HyperOS 1.0.json": f"{main_link}HyperOS-STABLE-RELEASES/HyperOS1.0/",
    "HyperOS 2.0.json": f"{main_link}HyperOS-STABLE-RELEASES/HyperOS2.0/",
    "HyperOS 3.0.json": f"{main_link}HyperOS-STABLE-RELEASES/HyperOS3.0/",
    "MIUI 12.json": f"{main_link}MIUI-STABLE-RELEASES/MIUIv12/",
    "MIUI 13.json": f"{main_link}MIUI-STABLE-RELEASES/MIUIv13/",
    "MIUI 14.json": f"{main_link}MIUI-STABLE-RELEASES/MIUIv14/",

}
def get_link_for_specific_device(file_name, device):
    """
    :param file_name: json file name where the market names, code names and urls are stored
    :param device:  device market name which is key for the ROM name and code name
    :return: download link or None
    """
    rom_name = None
    with open(f"XiaomiEuRomChecker/core/json/{file_name}", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        rom_name = data[device]["rom_name"]

    soup = get_soup(links_to_files[file_name])
    rows = soup.find_all("tr", class_="file")

    for row in rows:
        a = row.find("a", href=True)
        if not a:
            continue
    
        current_link = a["href"]
        # skip the "Parent folder" row
        if current_link == "..":
            continue

        if rom_name not in current_link:
            continue

        return current_link
    else:
        print("no such model found")

# test json file manually
# print(get_link_for_specific_device("HyperOS 1.0.json", "Redmi Turbo 3"))