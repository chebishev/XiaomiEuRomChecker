# This is connection to the bit.ly API for shorten urls if the user wants

import os
import pyshorteners
from dotenv import load_dotenv
load_dotenv()


def shorten_url(url):
    key = os.environ.get('BITLY_API', None)

    service = pyshorteners.Shortener(api_key=key)
    short_url = service.bitly.short(url)

    return short_url
