"""
WSGI config for orders project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

from support.helpers import env
from django.core.wsgi import get_wsgi_application

env('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()
