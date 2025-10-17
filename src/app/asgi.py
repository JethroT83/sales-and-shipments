"""
ASGI config for orders project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

from support.helpers import env
from django.core.asgi import get_asgi_application

env('DJANGO_SETTINGS_MODULE', 'settings')

application = get_asgi_application()
