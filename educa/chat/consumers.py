# building the websocket

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone


class ChatConsumer(WebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = f'char_{self.id}'
        # join room group
        await async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,self.channel_name
        )
        # accept connection
        await self.accept()
    async def disconnect(self, close_code):
        await async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,self.channel_name
        )
    # receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()
        # send message to the group
        await async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message' : message,
                'user' : self.user.username,
                'datetime': now.isoformat()
            }
        )
        
    # receive message from the room group
    async def chat_message(self,event):
        await self.send(text_data=json.dumps(event))
