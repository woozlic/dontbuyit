import os

from django.core.asgi import get_asgi_application
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dontbuyit.settings")
django.setup()
# django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, get_default_application
application = get_default_application()

from chat.routing import websocket_urlpatterns

# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#
#     "websocket": AuthMiddlewareStack(
#         URLRouter(websocket_urlpatterns)
#     ),
# })