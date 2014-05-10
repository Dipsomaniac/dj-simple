""" Production settings. """

from .core import *


ENVIRONMENT_NAME = 'production'

SECRET_KEY = 'DontForgetToReplaceMe'

CACHES['KEY_PREFIX'] = '_'.join((PROJECT_NAME, ENVIRONMENT_NAME))


logging.info("Production settings are loaded.")

# pylama:ignore=W0401,W0614
