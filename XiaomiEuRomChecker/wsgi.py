"""
WSGI config for XiaomiEuRomChecker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
import pathlib
import dotenv
CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_PATH = BASE_DIR / '.env'
dotenv.read_dotenv(str(ENV_PATH))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'XiaomiEuRomChecker.settings')

application = get_wsgi_application()
