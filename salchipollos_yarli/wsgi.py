# salchipollos_yarli/wsgi.py
"""
WSGI config for salchipollos_yarli project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'salchipollos_yarli.settings')

application = get_wsgi_application()

# No es estrictamente necesario para Whitenoise moderno,
# pero si lo quieres asegurar, esta es la línea:
# from whitenoise.django import DjangoWhiteNoise
# application = DjangoWhiteNoise(application)