# This is connection to the bit.ly API for shorten urls if the user wants

import os
import pyshorteners


def shorten_url(url):
    key = "6e4f69ed88460cc3cb3c96b6c1857c64e26ef452"

    service = pyshorteners.Shortener(api_key=key)
    short_url = service.bitly.short(url)

    return short_url
