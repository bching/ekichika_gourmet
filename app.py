from django.http import HttpResponse
from django.urls import path

'''
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
'''

'''
Settings
'''
DEBUG = True
SECRET_KEY = ')nnhtzcpgd#g9*y#&v6!5)=d2*c*4re_9d#6jzu=7d22yscley'
ROOT_URLCONF = __name__
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            './templates/'
        ],
    },
]


'''
Views
'''
from django.template import loader
import json
from leafletapikey import leafletkey
from apis.hotpper import hotpper

def call_hotppr(coords):
    nearshops = hotpper.hotpper_api(*coords)
    return nearshops

def index(request):
    # shortcut render(request, template_name, context=None, content_type=None, status=None, using=None)
    template = loader.get_template('index.html')

    centerloc = (35.6340074, 139.7135059)
    locations = call_hotppr(centerloc)

    context = {'locdata': locations, 'centerloc': centerloc}

    return HttpResponse(template.render(context, request))


'''
URL routes
'''
# path(route, view, kwargs=None, name=None)
urlpatterns = [
    path('', index),
]

