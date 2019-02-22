""" Production Settings """

import os
from .dev import *

############
# DATABASE #
############
DATABASES = {
  'default': {
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'NAME': 'neargreen',
    'HOST': os.environ.get('NEARGREENHOST'),
    'PORT': 5432,
    'USER': os.environ.get('NEARGREENUSER'),
    'PASSWORD': os.environ.get('NEARGREENPWD')
  }
}

############
# SECURITY #
############

DEBUG = False
# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
ALLOWED_HOSTS = ['*']
