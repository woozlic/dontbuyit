# import os
# import django
# django.setup()
# from channels.routing import get_default_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dontbuyit.settings")
#
# application = get_default_application()
from .wsgi import *  # add this line to top of your code
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing as routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
