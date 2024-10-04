"""
ASGI config for educa project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator



# Initialize the Django ASGI application first
django_asgi_app = get_asgi_application()



from chat.routing import websocket_urlpatterns



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educa.settings')

# Define how to handle different protocol types (HTTP and WebSocket)
application = ProtocolTypeRouter({
    'http': django_asgi_app,  # HTTP requests handled by Django
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns  # WebSocket routes from chat app
            )
        )
    ),
})
