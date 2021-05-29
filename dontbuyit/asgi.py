import django
django.setup()

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
# from channels.layers import get_channel_layer
import chat.routing


# channel_layer = get_channel_layer()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dontbuyit.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})