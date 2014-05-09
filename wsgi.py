import os.path
import sys


sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'simple'))

from main.wsgi import application

import uwsgi
from uwsgidecorators import *
from django.utils import autoreload


@timer(3)
def check_code(sig):
    if autoreload.code_changed():
        uwsgi.reload()
