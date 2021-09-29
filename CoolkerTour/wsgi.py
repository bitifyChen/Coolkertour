import os
os.environ["DJANGO_SETTINGS_MODULE"] = "CoolkerTour.settings"

#if Use ENV
import sys
from os.path import join,dirname,abspath
PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)
from CoolkerTour.local_settings import VIRTUALENV_PATH
sys.path.insert(0, VIRTUALENV_PATH)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
