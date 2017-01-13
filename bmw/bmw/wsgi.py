"""
WSGI config for bmw project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/django/domains/bmw/bmw/bmw/')
sys.path.append('/home/django/domains/bmw/lib/python2.7/site-packages/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bmw.settings")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bmw.settings")

application = get_wsgi_application()
