from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
# Import WebSocket routes from the chat app
from chat.routing import websocket_urlpatterns

# Define the ASGI application for Django (HTTP requests)
django_asgi_app = get_asgi_application()

# Define how to handle different protocol types (HTTP and WebSocket)
application = ProtocolTypeRouter({
    'http': django_asgi_app,  # HTTP requests handled by Django
    'websocket': AuthMiddlewareStack(  # WebSocket requests handled by Channels
        URLRouter(
            websocket_urlpatterns  # WebSocket routes from chat app
        )
    ),
})
