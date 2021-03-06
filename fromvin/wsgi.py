"""
WSGI config for fromvin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Settings required for live deployment.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fromvin.settings')

application = get_wsgi_application()
