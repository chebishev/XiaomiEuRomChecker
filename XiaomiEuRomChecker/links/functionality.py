# This is connection to the bit.ly API for shorten urls if the user wants

import pyshorteners

from XiaomiEuRomChecker.settings import get_settings

settings = get_settings()


def shorten_url(url):
    key = settings.BITLY_API

    service = pyshorteners.Shortener(api_key=key)
    short_url = service.bitly.short(url)

    return short_url
