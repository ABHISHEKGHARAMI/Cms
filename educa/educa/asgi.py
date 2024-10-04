"""
ASGI config for educa project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from chat.routing import websocket_urlpatterns  # Importing websocket routes

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educa.settings')

# HTTP protocol handled by Django ASGI
django_asgi_app = get_asgi_application()

# ASGI application to handle both HTTP and WebSocket
application = ProtocolTypeRouter({
    'http': django_asgi_app,  # Handle HTTP requests
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns  # Handle WebSocket routes
            )
        )
    ),
})
