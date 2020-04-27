import sys

from django.conf import settings
from django.conf.urls import url
from django.core.management import execute_from_command_line
from django.http import HttpResponse

SECRET_KEY = '^86k5u6-)h=#pexlot706q0--hc_j@vwdz7johmu87ixromueb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['nepdata.com','www.nepdata.com']


# Application definition

ROOT_URLCONF = sys.modules[__name__]


WSGI_APPLICATION = 'minimal.wsgi.application'


def index(request):
    return HttpResponse('<h1>A minimal Django response!</h1>')

urlpatterns = [
    url(r'^$', index),
]
