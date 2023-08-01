import json

# WebsocketConsumer is a base class provided by Django Channels 
# for handling WebSocket-related functionality
from channels.generic.websocket import WebsocketConsumer


# ChatConsumer is a custom WebSocket consumer class in Django Channels, 
# which is defined to handle WebSocket connections and events
class ChatConsumer(WebsocketConsumer):

# The connect method is a required method in the consumer class 
# that is called when a new WebSocket connection is established 
# with the server.
    def connect(self):

# the connect method accepts the WebSocket connection 
# using self.accept().
        self.accept()


        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'You are now connected!'
        }))