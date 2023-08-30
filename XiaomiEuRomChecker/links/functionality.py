# This is connection to the bit.ly API for shorten urls if the user wants

import os
import pyshorteners


def shorten_url(url):
    key = os.getenv('BITLY_API')

    service = pyshorteners.Shortener(api_key=key)
    short_url = service.bitly.short(url)

    return short_url
