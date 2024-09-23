from django.urls import path
from . import views

# url patterns for the new urls

urlpatterns = [
    path('room/<int:id>/',views.course_chat_room,name='course_chat_room'),
]