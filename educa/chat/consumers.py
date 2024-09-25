# building the websocket

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = f'char_{self.id}'
        # join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,self.channel_name
        )
        # accept connection
        self.accept()
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,self.channel_name
        )
    # receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # send message to the group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message' : message
            }
        )
        
    # receive message from the room group
    def chat_message(self,event):
        self.send(text_data=json.dumps(event))
