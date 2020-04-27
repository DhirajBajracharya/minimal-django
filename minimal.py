import sys

from django.conf import settings
from django.conf.urls import url
from django.core.management import execute_from_command_line
from django.http import HttpResponse

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
    TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates'},],
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

from django.template import engines
from django.template.loader import render_to_string

def templatetry(request):
    title = 'Tinyapp'
    author = 'Vitor Freitas'

    about_template = '''<!DOCTYPE html>
    <html>
    <head>
      <title>{{ title }}</title>
    </head>
    <body>
      <h1>About {{ title }}</h1>
      <p>This Website was developed by {{ author }}.</p>
      <p>Now using the Django's Template Engine.</p>
      <p><a href="{% url 'homepage' %}">Return to the homepage</a>.</p>
    </body>
    </html>
    '''

    django_engine = engines['django']
    template = django_engine.from_string(about_template)
    html = template.render({'title': title, 'author': author})

    return HttpResponse(html)

urlpatterns = [
    url(r'^$', index),
    url(r'^home$', home,name="homepage"),
    url(r'^tryget$', gettry),
    url(r'^trytemplate$',templatetry)
]

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
