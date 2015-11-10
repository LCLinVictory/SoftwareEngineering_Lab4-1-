import sae

from bookdb979 import wsgi


application = sae.create_wsgi_app(wsgi.application)