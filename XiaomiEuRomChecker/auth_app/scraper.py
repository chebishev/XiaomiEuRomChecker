from bs4 import BeautifulSoup
import requests


def scrape_config_by_url(url):
    page = requests.get(url)

    # BeautifulSoup instance that gets url and parser as arguments
    soup = BeautifulSoup(page.content, "html.parser")
    return soup
