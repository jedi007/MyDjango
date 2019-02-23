"""
WSGI config for MyDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
from os.path import join,dirname,abspath 
import sys

PROJECT_DIR = dirname(dirname(abspath(__file__)))   
sys.path.insert(0,PROJECT_DIR)

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyDjango.settings')

application = get_wsgi_application()