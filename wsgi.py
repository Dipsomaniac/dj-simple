""" Init wsgi application. """

import os.path
import sys


sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'simple'))

from main.wsgi import application

import uwsgi
from uwsgidecorators import timer
from django.utils import autoreload


@timer(3)
def check_code(sig):
    """ Check for code is changed. """
    if autoreload.code_changed():
        uwsgi.reload()


from django.conf import settings
if settings.DEBUG:
    from werkzeug.debug import DebuggedApplication
    from django.views import debug

    def null_technical_500_response(request, exc_type, exc_value, tb):
        """ Populate exceptions to werkzeug. """
        raise exc_type, exc_value, tb
    debug.technical_500_response = null_technical_500_response
    application = DebuggedApplication(application, evalex=True)

# pylama:ignore=F0401,E0611
