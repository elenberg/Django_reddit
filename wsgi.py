"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
env = os.environ.get("LK_ENV", None)
if env:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.%s" % os.environ["LK_ENV"])
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
