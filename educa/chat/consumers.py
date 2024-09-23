# building the websocket

import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    # check for the connection
    def connect(self):
        self.accept()
        
    # disconnect the connection
    def disconnect(self,close_code):
        pass
    
    # get the message
    def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # send message to WebSocket
        self.send(text_data=json.dumps({'message': message}))