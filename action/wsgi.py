"""
WSGI config for action project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "action.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()
activate_this = '/home/action/action/action/bin/activate_this.py'
exec(compile(open(activate_this,"rb").read(),activate_this, 'exec'), dict(__file__=activate_this))
