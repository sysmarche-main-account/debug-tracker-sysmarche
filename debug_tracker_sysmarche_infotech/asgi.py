"""
ASGI config for debug_tracker_sysmarche_infotech project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'debug_tracker_sysmarche_infotech.settings')

application = get_asgi_application()
