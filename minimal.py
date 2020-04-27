import sys

from django.conf import settings
from django.conf.urls import url
from django.core.management import execute_from_command_line
from django.http import HttpResponse

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
)


def index(request):
    return HttpResponse('<h1>A minimal Django response!</h1>')

def home(request):
    return HttpResponse('Welcome to the Tinyapp\'s Homepage!')

def gettry(request):
    color = request.GET.get('color', '')#http://127.0.0.1:8005/tryget?color=blue
    return HttpResponse(
        '<h1 style="color:' + color + '">Welcome to the Tinyapp\'s Homepage!</h1>'
    )  # don't use user input like that in real projects!

urlpatterns = [
    url(r'^$', index),
    url(r'^home$', home),
    url(r'^tryget$', gettry),
]

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
