from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoP.settings")
app = get_wsgi_application()

# Adaptador para serverless
def handler(request, response):
    return app(request, response)
