"""
WSGI config for btre project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'btre.settings')

''''
  - the wsgi server sits between the client and the web app framework
  - a client makes a request, it goes to the wsgi server, the wsgi then creates a python object that is 
    digested by the django app
  - this is cool because the python web app does not have to worry about keeping up with the different requests
    or maintaining connections to the clients
  - the wsgi server creates the objects and sends it to one of multiple workers that can be configured

  - it is normal practice to place the wsgi server behind 
'''

application = get_wsgi_application()
