from django.urls import re_path
from . import consumers



# route for the asgi server
websocket_urlpatterns = [
    re_path(r'ws/chat/room/(?P<course_id>\d+)/$',
            consumers.ChatConsumer.as_asgi()),
]