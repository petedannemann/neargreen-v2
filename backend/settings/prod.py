""" Production Settings """

import os
from .dev import *

############
# SECURITY #
############

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True